"""
Coaching engine — assembles multi-call context for /roast-me analysis.

Reads transcripts, wiki call history, the objection playbook, and ME.md
into a structured context package at logs/_coaching_context.json.
Claude Code reads this context and generates the CoachingReport prose.

Usage:
    python coaching_engine.py                   # last transcript
    python coaching_engine.py --all             # every call ever
    python coaching_engine.py --last-5          # last 5 transcripts
    python coaching_engine.py call_2026.txt     # specific file
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.utils import VAULT_ROOT, SOURCES_DIR, WIKI_DIR, LOGS_DIR, now_iso

ME_MD_PATH = VAULT_ROOT / "ME.md"
PLAYBOOK_PATH = WIKI_DIR / "objections" / "playbook.md"
CALLS_DIR = SOURCES_DIR / "calls"


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


def _extract_call_history_from_contacts() -> list[dict]:
    """
    Parse call history tables from all wiki/contacts/*.md files.
    Returns list of {contact, company, date, outcome, objections, follow_up} dicts.
    """
    contacts_dir = WIKI_DIR / "contacts"
    if not contacts_dir.exists():
        return []

    rows = []
    row_pattern = re.compile(
        r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]*)\s*\|"
    )

    for contact_file in contacts_dir.glob("*.md"):
        fm = _read_frontmatter(contact_file)
        name = fm.get("name", contact_file.stem)
        company = fm.get("company", "")
        content = contact_file.read_text(encoding="utf-8")

        for match in row_pattern.finditer(content):
            date, outcome, objections, follow_up = match.groups()
            outcome = outcome.strip()
            objections = objections.strip()
            follow_up = follow_up.strip()
            if outcome and outcome not in ("Outcome", "---"):
                rows.append({
                    "contact": name,
                    "company": company,
                    "date": date,
                    "outcome": outcome,
                    "objections": objections,
                    "follow_up": follow_up,
                })
    return sorted(rows, key=lambda r: r["date"], reverse=True)


def _extract_coaching_flags_from_contacts() -> list[dict]:
    """Pull coaching flags from all contact notes."""
    contacts_dir = WIKI_DIR / "contacts"
    if not contacts_dir.exists():
        return []

    flags = []
    flag_pattern = re.compile(
        r"\*\*\[(CRITICAL|MODERATE|MINOR)\]\*\*\s+(.+?)\n\s*>\s+\"(.+?)\"",
        re.DOTALL,
    )

    for f in contacts_dir.glob("*.md"):
        fm = _read_frontmatter(f)
        content = f.read_text(encoding="utf-8")
        for match in flag_pattern.finditer(content):
            severity, note, quote = match.groups()
            flags.append({
                "severity": severity.lower(),
                "note": note.strip(),
                "quote": quote.strip(),
                "contact": fm.get("name", f.stem),
                "company": fm.get("company", ""),
            })
    return flags


def _load_playbook() -> str:
    if not PLAYBOOK_PATH.exists():
        return "_No objection playbook yet._"
    return PLAYBOOK_PATH.read_text(encoding="utf-8")


def _load_operator_profile() -> str:
    if ME_MD_PATH.exists():
        return ME_MD_PATH.read_text(encoding="utf-8")
    return "_ME.md not found._"


def _find_transcript_files(mode: str) -> list[Path]:
    if not CALLS_DIR.exists():
        return []

    files = sorted(CALLS_DIR.glob("*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)

    if mode == "--all":
        return files
    if mode.startswith("--last-"):
        try:
            n = int(mode.split("-")[-1])
            return files[:n]
        except (ValueError, IndexError):
            return files[:5]
    if not mode.startswith("--"):
        # Specific filename
        p = Path(mode)
        if not p.is_absolute():
            p = CALLS_DIR / p
        return [p] if p.exists() else []

    # Default: last one
    return files[:1]


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def run(mode: str = "--latest") -> Path:
    logger = EngineLogger("coaching_engine")
    logger.start()

    transcript_files = _find_transcript_files(mode)
    call_history = _extract_call_history_from_contacts()
    coaching_flags = _extract_coaching_flags_from_contacts()
    playbook = _load_playbook()
    operator_profile = _load_operator_profile()

    # Load transcript content
    transcripts = []
    for tf in transcript_files:
        try:
            content = tf.read_text(encoding="utf-8")
            transcripts.append({
                "filename": tf.name,
                "content": content,
                "size_chars": len(content),
            })
        except Exception as e:
            logger.error("read_error", f"{tf.name}: {e}")

    # Compute outcome distribution
    outcome_counts: dict[str, int] = {}
    for row in call_history:
        outcome_counts[row["outcome"]] = outcome_counts.get(row["outcome"], 0) + 1

    # Coaching flag frequency
    flag_counts: dict[str, int] = {}
    for flag in coaching_flags:
        note_key = flag["note"][:40]
        flag_counts[note_key] = flag_counts.get(note_key, 0) + 1

    context = {
        "generated_at": now_iso(),
        "mode": mode,
        "transcripts": transcripts,
        "call_history_rows": call_history[:50],  # Last 50 calls
        "outcome_distribution": outcome_counts,
        "total_calls_tracked": len(call_history),
        "coaching_flags": coaching_flags,
        "flag_frequency": flag_counts,
        "objection_playbook": playbook,
        "operator_profile": operator_profile,
        "instructions": (
            "Claude Code: read transcripts above, call_history_rows, and coaching_flags. "
            "Generate a CoachingReport with: overall_grade, recurring_patterns (with example quotes), "
            "top_3_wins, top_3_kills, drills, and a full roast_text that cites specific quotes. "
            "No softening. Write as if you watched every call and are telling the operator exactly "
            "what's costing them money. Reference the operator_profile known_weaknesses."
        ),
    }

    LOGS_DIR.mkdir(exist_ok=True)
    out_path = LOGS_DIR / "_coaching_context.json"
    out_path.write_text(
        json.dumps(context, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.finish(
        items_processed=len(transcripts),
        output_path=str(out_path),
    )
    return out_path


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()
    mode = sys.argv[1] if len(sys.argv) > 1 else "--latest"

    console.print(f"\n[bold]Coaching Engine[/bold] — mode: {mode}")
    ctx_path = run(mode)

    ctx = json.loads(ctx_path.read_text(encoding="utf-8"))
    console.print(f"  Transcripts loaded: [bold]{len(ctx['transcripts'])}[/bold]")
    console.print(f"  Call history rows:  [bold]{ctx['total_calls_tracked']}[/bold]")
    console.print(f"  Coaching flags:     [bold]{len(ctx['coaching_flags'])}[/bold]")
    console.print()
    if ctx["outcome_distribution"]:
        console.print("  Outcome distribution:")
        for outcome, count in sorted(ctx["outcome_distribution"].items(), key=lambda x: -x[1]):
            console.print(f"    {outcome:<25} {count}")
    console.print(f"\n  Context -> [cyan]logs/_coaching_context.json[/cyan]")
    console.print("  Run /roast-me to generate the coaching report.")
