"""
The only writer to wiki/. All engines write through this.
Implements: create-or-merge (never overwrite), atomic writes,
YAML frontmatter parsing, Obsidian wikilink format.
"""

from __future__ import annotations
import re
import tempfile
import os
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from filelock import FileLock

from .utils import WIKI_DIR, slugify, today_iso
from .schemas import CallAnalysis, CallOutcome, ObjectionInstance


# ── FRONTMATTER ───────────────────────────────────────────────────────────────

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a markdown file into (frontmatter_dict, body_str)."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                return fm, parts[2].lstrip("\n")
            except yaml.YAMLError:
                pass
    return {}, text


def _render_frontmatter(fm: dict, body: str) -> str:
    return f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}"


def _atomic_write(path: Path, content: str) -> None:
    """Write to a temp file then rename — prevents partial writes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = FileLock(str(path) + ".lock")
    with lock:
        fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(content)
            os.replace(tmp, path)
        except Exception:
            os.unlink(tmp)
            raise


# ── CONTACT NOTES ─────────────────────────────────────────────────────────────

def write_contact_note(analysis: CallAnalysis) -> Path:
    name = analysis.prospect_name or "Unknown"
    slug = slugify(name)
    path = WIKI_DIR / "contacts" / f"{slug}.md"

    fm, body = _parse_frontmatter(path.read_text(encoding="utf-8")) if path.exists() else ({}, "")

    # Merge frontmatter — never downgrade an existing value
    fm.setdefault("name", name)
    fm.setdefault("company", analysis.company_name)
    fm.setdefault("phone", analysis.phone)
    fm.setdefault("stage", "contacted")
    fm["last_contact"] = today_iso()
    if analysis.follow_up_date:
        fm["follow_up_date"] = analysis.follow_up_date
    fm.setdefault("tags", ["prospect"])

    # Build call history row
    outcome_str = analysis.outcome.value
    objections_str = "; ".join(o.exact_quote[:60] for o in analysis.objections) or "none"
    follow_up_str = analysis.follow_up_action or "—"
    call_row = (
        f"| {today_iso()} | {outcome_str} | {objections_str} | {follow_up_str} |"
    )

    # Build body if new file
    company_link = f"[[{slugify(analysis.company_name)}]]" if analysis.company_name else "_unknown_"
    if not body.strip():
        body = f"""**Company:** {company_link}

## Pain Signals
_To be filled after research engine runs._

## Personalized Pitch Angle
_To be filled by personalization engine._

## Call History
| Date | Outcome | Objections | Follow-up |
|------|---------|------------|-----------|
{call_row}

## Analysis
{analysis.full_analysis}

## Coaching Flags
"""
        for flag in analysis.coaching_flags:
            body += f"\n- **[{flag.severity.upper()}]** {flag.coaching_note}\n  > \"{flag.exact_quote}\"\n"
    else:
        # Append call row to existing table
        if "| Date | Outcome |" in body:
            body = re.sub(
                r"(\| Date \| Outcome \|.*?\n(?:\|[-|]+\|\n)?)",
                lambda m: m.group(0) + call_row + "\n",
                body,
                count=1,
                flags=re.DOTALL,
            )
        else:
            body += f"\n## Call History\n| Date | Outcome | Objections | Follow-up |\n|------|---------|------------|----------|\n{call_row}\n"

    _atomic_write(path, _render_frontmatter(fm, body))
    return path


# ── COMPANY NOTES ─────────────────────────────────────────────────────────────

def write_company_note(
    company_name: str,
    stage: str | None = None,
    last_contact: str | None = None,
    extra_fm: dict | None = None,
    summary: str | None = None,
) -> Path:
    slug = slugify(company_name)
    path = WIKI_DIR / "companies" / f"{slug}.md"

    fm, body = _parse_frontmatter(path.read_text(encoding="utf-8")) if path.exists() else ({}, "")

    fm.setdefault("company", company_name)
    fm.setdefault("tags", [])
    if stage:
        fm["stage"] = stage
    if last_contact:
        fm["last_contact"] = last_contact
    if extra_fm:
        fm.update(extra_fm)

    if not body.strip():
        body = f"""## Summary
{summary or "_Awaiting research engine enrichment._"}

## Opportunities
_To be identified by research engine._

## Red Flags
_To be identified by research engine._

## Call History
| Date | Contact | Outcome | Follow-up |
|------|---------|---------|-----------|

## Objections Reference
See [[playbook]] for all known objections and responses.
"""

    _atomic_write(path, _render_frontmatter(fm, body))
    return path


# ── OBJECTION PLAYBOOK ────────────────────────────────────────────────────────

def append_objection(objection: ObjectionInstance, source_file: str) -> Path:
    path = WIKI_DIR / "objections" / "playbook.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    existing = path.read_text(encoding="utf-8") if path.exists() else ""

    quote_clean = objection.exact_quote.strip().strip('"')

    # Update frequency counter if already present
    freq_pattern = re.compile(
        rf'(### "{re.escape(quote_clean[:40])}.*?\*\*Frequency:\*\* )(\d+)',
        re.DOTALL,
    )
    match = freq_pattern.search(existing)
    if match:
        new_freq = int(match.group(2)) + 1
        updated = freq_pattern.sub(lambda m: m.group(1) + str(new_freq), existing, count=1)
        # Also append source file reference
        updated = updated.replace(
            f"**Source calls:** {source_file}",
            f"**Source calls:** {source_file}",
        )
        _atomic_write(path, updated)
        return path

    # New objection entry
    response_quality_map = {
        "folded": "_No effective response — caller accepted objection._",
        "weak_pivot": objection.caller_response,
        "strong_pivot": objection.caller_response,
        "closed": objection.caller_response,
    }

    entry = f"""
### "{quote_clean}"
**Category:** {objection.category}
**Frequency:** 1
**Caller response quality:** {objection.response_quality}
**Best response:** {response_quality_map.get(objection.response_quality, objection.caller_response)}
**Source calls:** {source_file}

---
"""
    header = "# Objection Playbook\n_Ranked by frequency. Auto-updated after every call analysis._\n\n"
    if not existing:
        content = header + entry
    else:
        content = existing + entry

    _atomic_write(path, content)
    return path


# ── COACHING ──────────────────────────────────────────────────────────────────

def write_coaching_report(content: str, date: str | None = None) -> Path:
    d = date or today_iso()
    path = WIKI_DIR / "coaching" / f"roast_{d}.md"
    latest = WIKI_DIR / "coaching" / "latest_roast.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write(path, content)
    _atomic_write(latest, content)
    return path


# ── PIPELINE ──────────────────────────────────────────────────────────────────

def update_pipeline_stage(company_name: str, stage: str) -> None:
    write_company_note(company_name, stage=stage, last_contact=today_iso())


# ── DAILY BRIEF ───────────────────────────────────────────────────────────────

def write_daily_brief(content: str) -> Path:
    path = WIKI_DIR.parent / "daily" / f"{today_iso()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write(path, content)
    return path
