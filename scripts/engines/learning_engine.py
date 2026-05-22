"""
Learning engine — aggregates call patterns and evolves the master call script.

Reads all call history from wiki/contacts/ and the objection playbook.
When 5+ calls are recorded, identifies what's working and what isn't,
then writes a learning brief to logs/_learning_context.json.

Claude Code reads the learning context and updates wiki/scripts/master_script.md.

Usage:
    python learning_engine.py          # analyze all available call data
    python learning_engine.py --force  # rewrite script even if < 5 calls

Trigger: automatically called by /analyze-call when total_calls % 5 == 0
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.logger import EngineLogger
from lib.utils import VAULT_ROOT, SOURCES_DIR, WIKI_DIR, LOGS_DIR, now_iso

ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"
ME_MD_PATH = VAULT_ROOT / "ME.md"
PLAYBOOK_PATH = WIKI_DIR / "objections" / "playbook.md"
MASTER_SCRIPT_PATH = WIKI_DIR / "scripts" / "master_script.md"
PATTERN_LOG_PATH = WIKI_DIR / "scripts" / "pattern_log.md"
MIN_CALLS_TO_LEARN = 5


# ── DATA EXTRACTION ────────────────────────────────────────────────────────────

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


def _parse_call_rows(contacts_dir: Path) -> list[dict]:
    """
    Extract all call history rows from wiki/contacts/*.md.
    Row format: | Date | Outcome | Objections | Follow-up |
    """
    if not contacts_dir.exists():
        return []

    rows = []
    row_re = re.compile(
        r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|"
    )
    for contact_file in contacts_dir.glob("*.md"):
        fm = _read_frontmatter(contact_file)
        content = contact_file.read_text(encoding="utf-8")
        for m in row_re.finditer(content):
            date, outcome, objections, follow_up = (x.strip() for x in m.groups())
            if outcome and outcome not in ("Outcome", "---", ""):
                rows.append({
                    "contact": fm.get("name", contact_file.stem),
                    "company": fm.get("company", ""),
                    "date": date,
                    "outcome": outcome,
                    "objections_raw": objections,
                    "follow_up": follow_up,
                })
    return sorted(rows, key=lambda r: r["date"])


def _parse_playbook_entries(playbook_path: Path) -> list[dict]:
    """
    Extract objection entries from the playbook.
    Returns list of {quote, category, frequency, response_quality, best_response}.
    """
    if not playbook_path.exists():
        return []

    content = playbook_path.read_text(encoding="utf-8")
    entries = []

    # Split on ### headers
    blocks = re.split(r"### ", content)
    for block in blocks[1:]:  # Skip header block
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        quote = lines[0].strip().strip('"')

        freq_match = re.search(r"\*\*Frequency:\*\*\s*(\d+)", block)
        cat_match = re.search(r"\*\*Category:\*\*\s*(\w+)", block)
        qual_match = re.search(r"\*\*Caller response quality:\*\*\s*(\w+)", block)
        resp_match = re.search(r"\*\*Best response:\*\*\s*(.+?)(?:\n\*\*|$)", block, re.DOTALL)

        entries.append({
            "quote": quote,
            "category": cat_match.group(1) if cat_match else "other",
            "frequency": int(freq_match.group(1)) if freq_match else 1,
            "response_quality": qual_match.group(1) if qual_match else "unknown",
            "best_response": resp_match.group(1).strip() if resp_match else "",
        })

    return sorted(entries, key=lambda e: e["frequency"], reverse=True)


def _extract_coaching_flags(contacts_dir: Path) -> list[dict]:
    if not contacts_dir.exists():
        return []

    flags = []
    flag_re = re.compile(
        r"\*\*\[(CRITICAL|MODERATE|MINOR)\]\*\*\s+(.+?)\n\s*>\s+\"(.+?)\"",
        re.DOTALL,
    )
    for f in contacts_dir.glob("*.md"):
        fm = _read_frontmatter(f)
        content = f.read_text(encoding="utf-8")
        for m in flag_re.finditer(content):
            severity, note, quote = m.groups()
            flags.append({
                "severity": severity.lower(),
                "note": note.strip(),
                "quote": quote.strip()[:100],
                "company": fm.get("company", ""),
            })
    return flags


# ── PATTERN ANALYSIS ───────────────────────────────────────────────────────────

def _analyze_patterns(rows: list[dict], flags: list[dict]) -> dict:
    """Pure Python pattern counting — no LLM needed."""
    total = len(rows)
    if total == 0:
        return {"total_calls": 0}

    # Outcome distribution
    outcome_counts = Counter(r["outcome"] for r in rows)

    # Positive outcomes (booked, callback_scheduled, interested)
    positive = {"booked", "callback_scheduled", "interested"}
    negative = {"rejected", "dead", "hung_up"}
    positive_count = sum(outcome_counts.get(o, 0) for o in positive)
    negative_count = sum(outcome_counts.get(o, 0) for o in negative)
    voicemail_count = outcome_counts.get("voicemail", 0)

    conversion_rate = round(positive_count / total * 100, 1) if total > 0 else 0.0

    # Coaching flag frequency
    flag_counts = Counter(f["note"][:50] for f in flags)
    top_flags = flag_counts.most_common(5)

    # Severity distribution
    critical_flags = [f for f in flags if f["severity"] == "critical"]
    moderate_flags = [f for f in flags if f["severity"] == "moderate"]

    return {
        "total_calls": total,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "voicemail_count": voicemail_count,
        "conversion_rate_pct": conversion_rate,
        "outcome_counts": dict(outcome_counts.most_common()),
        "top_coaching_flags": [{"issue": note, "count": count} for note, count in top_flags],
        "critical_flags_count": len(critical_flags),
        "critical_flag_examples": [f["quote"] for f in critical_flags[:3]],
        "has_enough_data": total >= MIN_CALLS_TO_LEARN,
    }


def _load_niche() -> dict:
    try:
        active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
        return yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))
    except Exception:
        return {"niche": "unknown", "display_name": "Unknown"}


# ── MASTER SCRIPT INIT ────────────────────────────────────────────────────────

def _ensure_master_script() -> None:
    """Create master_script.md template if it doesn't exist."""
    if MASTER_SCRIPT_PATH.exists():
        return

    MASTER_SCRIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    niche = _load_niche()

    template = f"""---
version: 1
niche: {niche['niche']}
last_updated: {now_iso()[:10]}
calls_used: 0
---

# Master Call Script — {niche['display_name']}

> Auto-updated by learning_engine when 5+ calls are analyzed.
> Version history in [[pattern_log]].

---

## HOOK (Opening)

_Evolves based on which openers got the best engagement rate._

"[Opener to be populated after first 5 calls are analyzed]"

---

## BRIDGE (Confirming the pain)

"[Bridge questions to be populated after first 5 calls]"

---

## PIVOT (Connecting pain → offer)

"[Pivot line to be populated after first 5 calls]"

---

## VALUE FRAME

"[Value frame to be populated after first 5 calls]"

---

## SOFT CLOSE

"[Close to be populated after first 5 calls]"

---

## OBJECTION RESPONSES

_Ranked by frequency. See [[playbook]] for full detail._

_To be populated after first 5 calls are analyzed._

---

## WHAT'S WORKING

_Winning phrases identified from real calls._

_To be populated after first 5 calls are analyzed._

---

## WHAT'S KILLING CALLS

_Patterns that consistently lose the call._

_To be populated after first 5 calls are analyzed._
"""
    MASTER_SCRIPT_PATH.write_text(template, encoding="utf-8")


def _ensure_pattern_log() -> None:
    if PATTERN_LOG_PATH.exists():
        return
    PATTERN_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    PATTERN_LOG_PATH.write_text(
        "# Script Pattern Log\n\n"
        "> Auto-appended by learning_engine after each script evolution.\n\n"
        "---\n",
        encoding="utf-8",
    )


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def run(force: bool = False) -> tuple[Path, dict]:
    logger = EngineLogger("learning_engine")
    logger.start()

    _ensure_master_script()
    _ensure_pattern_log()

    contacts_dir = WIKI_DIR / "contacts"
    rows = _parse_call_rows(contacts_dir)
    playbook_entries = _parse_playbook_entries(PLAYBOOK_PATH)
    flags = _extract_coaching_flags(contacts_dir)
    patterns = _analyze_patterns(rows, flags)
    niche = _load_niche()

    operator_profile = ME_MD_PATH.read_text(encoding="utf-8") if ME_MD_PATH.exists() else ""
    current_script = MASTER_SCRIPT_PATH.read_text(encoding="utf-8") if MASTER_SCRIPT_PATH.exists() else ""

    learning_context = {
        "generated_at": now_iso(),
        "niche": niche["niche"],
        "patterns": patterns,
        "top_objections": playbook_entries[:8],
        "all_call_rows": rows[-30:],  # Last 30 calls for context
        "coaching_flag_summary": flags[-20:],
        "current_master_script": current_script,
        "operator_profile": operator_profile,
        "should_update_script": patterns.get("has_enough_data", False) or force,
        "instructions": (
            "Claude Code: review patterns, top_objections, coaching_flag_summary, and all_call_rows. "
            "If should_update_script is true, rewrite wiki/scripts/master_script.md using actual "
            "winning phrases and evidence-based objection responses from the data. "
            "Update the version number and calls_used count in frontmatter. "
            "Append a changelog entry to wiki/scripts/pattern_log.md explaining what changed and why. "
            "Base every change on real evidence from the call data — no generic advice."
        ),
    }

    LOGS_DIR.mkdir(exist_ok=True)
    out_path = LOGS_DIR / "_learning_context.json"
    out_path.write_text(
        json.dumps(learning_context, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.finish(
        items_processed=patterns.get("total_calls", 0),
        output_path=str(out_path),
    )

    return out_path, patterns


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console
    from rich.table import Table

    console = Console()
    force = "--force" in sys.argv

    console.print("\n[bold]Learning Engine[/bold]")
    out_path, patterns = run(force=force)

    total = patterns.get("total_calls", 0)
    console.print(f"  Total calls analyzed: [bold]{total}[/bold]")
    console.print(f"  Conversion rate:      [bold]{patterns.get('conversion_rate_pct', 0)}%[/bold]")
    console.print(f"  Positive outcomes:    {patterns.get('positive_count', 0)}")
    console.print(f"  Voicemails:           {patterns.get('voicemail_count', 0)}")
    console.print(f"  Critical flags:       {patterns.get('critical_flags_count', 0)}")

    if patterns.get("top_coaching_flags"):
        console.print("\n  Top coaching issues:")
        for item in patterns["top_coaching_flags"][:3]:
            console.print(f"    [{item['count']}×] {item['issue'][:60]}")

    if patterns.get("has_enough_data") or force:
        console.print(f"\n  [green]Enough data to update script.[/green]")
        console.print(f"  Context written to [cyan]logs/_learning_context.json[/cyan]")
        console.print("  Claude Code will update wiki/scripts/master_script.md on next run.")
    else:
        remaining = MIN_CALLS_TO_LEARN - total
        console.print(f"\n  [yellow]{remaining} more call(s) needed before script evolution triggers.[/yellow]")
        console.print(f"  Context still written for reference → [cyan]logs/_learning_context.json[/cyan]")
