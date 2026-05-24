"""
Daily brief engine — generates the operator's prioritized call sheet.

Reads all wiki/contacts/ and wiki/companies/ frontmatter, buckets leads
by urgency (callbacks due, warm pipeline, cold by score), loads openers
from intel cards when available, and writes a formatted call sheet.

Usage:
    python daily_brief_engine.py          # generate today's brief
    python daily_brief_engine.py --dry    # print without saving

Output: daily/<YYYY-MM-DD>.md
        Returns structured context for Claude Code to display/enhance via /daily-brief
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.utils import VAULT_ROOT, SOURCES_DIR, WIKI_DIR, LOGS_DIR, now_iso, slugify
from lib.vault import write_daily_brief

ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"
INTEL_CARDS_DIR = SOURCES_DIR / "prospects" / "intel_cards"
TODAY = date.today().isoformat()


# ── DATA READERS ───────────────────────────────────────────────────────────────

def _read_frontmatter(path: Path) -> dict:
    try:
        content = path.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1]) or {}
    except Exception:
        pass
    return {}


def _load_all_contacts() -> list[dict]:
    contacts_dir = WIKI_DIR / "contacts"
    if not contacts_dir.exists():
        return []
    contacts = []
    for f in contacts_dir.glob("*.md"):
        fm = _read_frontmatter(f)
        if fm.get("stage") == "dead":
            continue
        fm["_file"] = f.stem
        contacts.append(fm)
    return contacts


def _load_all_companies() -> dict[str, dict]:
    """Returns {slug: frontmatter} for quick lookup."""
    companies_dir = WIKI_DIR / "companies"
    if not companies_dir.exists():
        return {}
    out = {}
    for f in companies_dir.glob("*.md"):
        fm = _read_frontmatter(f)
        out[f.stem] = fm
    return out


def _load_niche_openers() -> dict:
    try:
        active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
        niche = yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))
        return niche.get("opener_templates", {})
    except Exception:
        return {}


def _get_opener(company_name: str, niche_openers: dict) -> str:
    """Load opener from intel card if available, else use niche default."""
    slug = slugify(company_name or "")
    card_path = INTEL_CARDS_DIR / f"{slug}.md"
    if card_path.exists():
        content = card_path.read_text(encoding="utf-8")
        # Extract the OPENER section
        import re
        m = re.search(r"OPENER:\s*\n\s*\"?(.+?)\"?\n━", content, re.DOTALL)
        if m:
            opener = m.group(1).strip().replace("\n   ", " ").replace("\n", " ")
            return opener[:140]
    # Fallback to niche template
    default = niche_openers.get("default", "Introduce yourself and mention your automation services.")
    # Strip YAML block scalar indicators
    return default.strip().replace("\n", " ")[:140]


def _days_since(date_str: str | None) -> int | None:
    if not date_str:
        return None
    try:
        d = datetime.strptime(str(date_str), "%Y-%m-%d").date()
        return (date.today() - d).days
    except ValueError:
        return None


def _is_overdue(follow_up_date: str | None) -> bool:
    if not follow_up_date:
        return False
    try:
        d = datetime.strptime(str(follow_up_date), "%Y-%m-%d").date()
        return d <= date.today()
    except ValueError:
        return False


# ── BUCKETING ──────────────────────────────────────────────────────────────────

def _bucket_contacts(contacts: list[dict], companies: dict[str, dict]) -> dict:
    """
    Sort contacts into call buckets.

    Bucket A — Call today (non-negotiable):
        follow_up_date <= today OR stage in (callback_scheduled, booked)

    Bucket B — Strong pipeline:
        stage in (nurturing, contacted, interested) OR (cold AND tier A/B)
        No follow_up_date set (not yet scheduled)

    Bucket C — Fill time:
        stage == cold, tier C, or no tier
    """
    bucket_a: list[dict] = []
    bucket_b: list[dict] = []
    bucket_c: list[dict] = []
    going_cold: list[dict] = []

    for contact in contacts:
        stage = (contact.get("stage") or "cold").lower()
        follow_up = contact.get("follow_up_date")
        last_contact_str = contact.get("last_contact")
        company_name = contact.get("company") or ""
        company_slug = slugify(company_name)
        co = companies.get(company_slug, {})
        tier = co.get("tier") or contact.get("tier") or "D"
        score = co.get("lead_score") or 0

        days_since_contact = _days_since(str(last_contact_str) if last_contact_str else None)
        overdue = _is_overdue(str(follow_up) if follow_up else None)

        enriched = {**contact, "_tier": tier, "_score": score, "_overdue": overdue}

        if stage in ("callback_scheduled", "booked") or overdue:
            bucket_a.append(enriched)
        elif stage in ("nurturing", "interested", "contacted"):
            if days_since_contact and days_since_contact > 14:
                going_cold.append(enriched)
            else:
                bucket_b.append(enriched)
        elif stage == "cold":
            if tier in ("A", "B"):
                bucket_b.append(enriched)
            else:
                bucket_c.append(enriched)

    # Sort buckets
    bucket_a.sort(key=lambda c: (not c["_overdue"], str(c.get("follow_up_date") or "")))
    bucket_b.sort(key=lambda c: (-c["_score"], c.get("_tier", "D")))
    bucket_c.sort(key=lambda c: (-c["_score"], c.get("_tier", "D")))

    return {
        "bucket_a": bucket_a,
        "bucket_b": bucket_b[:7],   # Cap at 7 for focus
        "bucket_c": bucket_c[:5],
        "going_cold": going_cold,
    }


# ── RENDERING ──────────────────────────────────────────────────────────────────

def _render_brief(buckets: dict, niche_openers: dict, companies: dict) -> str:
    today_str = datetime.now().strftime("%A, %B %d %Y")
    a = buckets["bucket_a"]
    b = buckets["bucket_b"]
    c = buckets["bucket_c"]
    cold = buckets["going_cold"]

    total_calls = len(a) + len(b)
    overdue_count = sum(1 for x in a if x.get("_overdue"))
    hot_count = sum(1 for x in a if x.get("stage") in ("callback_scheduled", "booked"))

    lines = [
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        f"DAILY BRIEF — {today_str}",
        f"{total_calls} calls · {overdue_count} overdue · {hot_count} hot",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "",
    ]

    # Today's priority
    priority = a[0] if a else (b[0] if b else None)
    if priority:
        pname = priority.get("name") or "Unknown"
        pco = priority.get("company") or ""
        flags = []
        if priority.get("_overdue"):
            flags.append("⚠️ OVERDUE")
        if priority.get("stage") in ("callback_scheduled", "booked"):
            flags.append("🔥 HOT")
        flag_str = "  " + " ".join(flags) if flags else ""
        lines += [
            "TODAY'S PRIORITY",
            f"-> {pco} ({pname}){flag_str}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        ]

    # Bucket A
    if a:
        lines += ["", "🔴 CALL TODAY", ""]
        for i, contact in enumerate(a[:5], 1):
            name = contact.get("name") or "Unknown"
            company = contact.get("company") or ""
            phone = contact.get("phone") or "—"
            stage = contact.get("stage") or "cold"
            last = contact.get("last_contact") or "never"
            follow_up = contact.get("follow_up_date") or ""
            flags = []
            if contact.get("_overdue"):
                flags.append("⚠️ OVERDUE")
            if stage in ("callback_scheduled", "booked"):
                flags.append("🔥 HOT")
            flag_str = "  " + " ".join(flags) if flags else ""
            opener = _get_opener(company, niche_openers)

            lines += [
                f"{i}. {name} — {company}{flag_str}",
                f"   📞 {phone}  ·  Stage: {stage}  ·  Last contact: {last}",
                f"   Open with: \"{opener}\"",
            ]
            if follow_up:
                lines.append(f"   Follow-up was due: {follow_up}")
            lines.append("")
    else:
        lines += ["", "🔴 CALL TODAY", "   No urgent callbacks. Start with pipeline work.", ""]

    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Bucket B
    if b:
        lines += ["", "🟡 PIPELINE WORK", ""]
        for i, contact in enumerate(b, len(a) + 1):
            name = contact.get("name") or "Unknown"
            company = contact.get("company") or ""
            phone = contact.get("phone") or "—"
            tier = contact.get("_tier") or "?"
            score = contact.get("_score") or 0
            opener = _get_opener(company, niche_openers)
            lines += [
                f"{i}. {name} — {company}  Tier {tier} · Score {score}",
                f"   📞 {phone}",
                f"   Open with: \"{opener}\"",
                "",
            ]

    # Going cold
    if cold:
        lines += [
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "❄️ GOING COLD",
            "",
        ]
        for contact in cold[:4]:
            name = contact.get("name") or "Unknown"
            company = contact.get("company") or ""
            last = contact.get("last_contact") or "unknown"
            days = _days_since(str(last) if last else None)
            days_str = f"{days} days ago" if days else f"last: {last}"
            lines.append(f"   · {company} ({name}) — {days_str}. Follow up or mark dead.")
        lines.append("")

    # Pipeline snapshot
    all_contacts = buckets["bucket_a"] + buckets["bucket_b"] + buckets["bucket_c"] + buckets["going_cold"]
    stage_counts: dict[str, int] = {}
    for co in all_contacts:
        s = co.get("stage") or "cold"
        stage_counts[s] = stage_counts.get(s, 0) + 1

    lines += [
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "",
        "PIPELINE SNAPSHOT",
        "  " + "  |  ".join(f"{k}: {v}" for k, v in sorted(stage_counts.items())),
        "",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    ]

    # Today's target
    if a:
        target = a[0]
        target_co = target.get("company") or target.get("name") or "your top lead"
        lines += [
            f"TODAY'S TARGET: {target_co} — this is your highest-priority call.",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        ]
    elif b:
        target = b[0]
        target_co = target.get("company") or target.get("name") or "your top lead"
        tier = target.get("_tier") or "B"
        lines += [
            f"TODAY'S TARGET: {target_co} (Tier {tier}) — highest scored cold lead.",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        ]

    return "\n".join(lines)


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def run(dry: bool = False) -> tuple[Path, dict]:
    logger = EngineLogger("daily_brief_engine")
    logger.start()

    contacts = _load_all_contacts()
    companies = _load_all_companies()
    niche_openers = _load_niche_openers()
    buckets = _bucket_contacts(contacts, companies)

    brief_md = _render_brief(buckets, niche_openers, companies)
    output_path = write_daily_brief(brief_md)

    # Also write structured context for /daily-brief Claude Code enhancement
    context = {
        "generated_at": now_iso(),
        "today": TODAY,
        "bucket_a_count": len(buckets["bucket_a"]),
        "bucket_b_count": len(buckets["bucket_b"]),
        "going_cold_count": len(buckets["going_cold"]),
        "total_contacts": len(contacts),
        "total_companies": len(companies),
        "buckets": {
            k: [
                {
                    "name": c.get("name"),
                    "company": c.get("company"),
                    "phone": c.get("phone"),
                    "stage": c.get("stage"),
                    "tier": c.get("_tier"),
                    "score": c.get("_score"),
                    "follow_up_date": str(c.get("follow_up_date") or ""),
                    "last_contact": str(c.get("last_contact") or ""),
                    "overdue": c.get("_overdue", False),
                }
                for c in v
            ]
            for k, v in buckets.items()
        },
    }

    LOGS_DIR.mkdir(exist_ok=True)
    ctx_path = LOGS_DIR / "_daily_brief_context.json"
    ctx_path.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")

    logger.finish(
        items_processed=len(contacts),
        output_path=str(output_path),
    )

    return output_path, context


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()
    dry = "--dry" in sys.argv

    console.print("\n[bold]Daily Brief Engine[/bold]")
    output_path, ctx = run(dry=dry)

    console.print(f"  Contacts loaded:    [bold]{ctx['total_contacts']}[/bold]")
    console.print(f"  🔴 Call today:      [bold]{ctx['bucket_a_count']}[/bold]")
    console.print(f"  🟡 Pipeline work:   [bold]{ctx['bucket_b_count']}[/bold]")
    console.print(f"  ❄️  Going cold:      {ctx['going_cold_count']}")

    if not dry:
        console.print(f"\n  Brief saved -> [cyan]{output_path}[/cyan]")

    console.print("\n" + "─" * 50)
    console.print(output_path.read_text(encoding="utf-8")[:1000])
    if len(output_path.read_text(encoding="utf-8")) > 1000:
        console.print("  [dim]... (truncated — open in Obsidian for full view)[/dim]")
