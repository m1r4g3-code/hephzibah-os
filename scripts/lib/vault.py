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
from .schemas import CallAnalysis, CallOutcome, EnrichedProspect, ObjectionInstance


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


# ── RESEARCH ENGINE OUTPUT ────────────────────────────────────────────────────

def write_prospect_stub(prospect: EnrichedProspect) -> Path:
    """
    Write or update a company note from research engine output.
    Preserves existing call history and manual edits — only updates
    frontmatter fields and pain signal section.
    """
    slug = slugify(prospect.company_name)
    path = WIKI_DIR / "companies" / f"{slug}.md"

    fm, body = _parse_frontmatter(path.read_text(encoding="utf-8")) if path.exists() else ({}, "")

    # Update frontmatter — setdefault for fields the operator may have edited manually
    fm["company"] = prospect.company_name
    fm.setdefault("owner", prospect.owner_name)
    fm.setdefault("phone", prospect.phone)
    fm.setdefault("website", prospect.website)
    fm.setdefault("google_maps_url", prospect.google_maps_url)
    fm["city"] = prospect.city
    fm["state"] = prospect.state
    fm.setdefault("country", prospect.country)
    fm.setdefault("stage", "cold")
    fm.setdefault("lead_score", None)
    fm.setdefault("tier", None)
    if prospect.google_rating is not None:
        fm["google_rating"] = prospect.google_rating
    if prospect.review_count is not None:
        fm["review_count"] = prospect.review_count

    existing_tags = set(fm.get("tags") or [])
    existing_tags.update({"prospect", prospect.niche})
    fm["tags"] = sorted(existing_tags)

    if not body.strip():
        # New file — build full body
        summary_parts = []
        if prospect.address:
            summary_parts.append(prospect.address)
        if prospect.google_rating:
            rating_str = f"Rating: {prospect.google_rating}"
            if prospect.review_count:
                rating_str += f" ({prospect.review_count} reviews)"
            summary_parts.append(rating_str)
        summary = " · ".join(summary_parts) if summary_parts else "_Scraped — awaiting qualification._"

        pain_section = ""
        if prospect.pain_signals:
            pain_section = "## Pain Signals\n" + "\n".join(f"- {s}" for s in prospect.pain_signals) + "\n\n"

        website_section = ""
        if prospect.website_signals and prospect.website_signals.fetch_status == "success":
            ws = prospect.website_signals
            website_section = (
                "## Website Signals\n"
                f"- Quality: {ws.quality_score}\n"
                f"- CMS: {ws.cms_detected or 'unknown'}\n"
                f"- SSL: {'yes' if ws.has_ssl else 'no'}\n"
                f"- Booking form: {'yes' if ws.has_booking_form else 'no'}\n"
                f"- Copyright year: {ws.copyright_year or 'unknown'}\n\n"
            )

        body = (
            f"## Summary\n{summary}\n\n"
            f"{pain_section}"
            f"{website_section}"
            "## Opportunities\n_To be identified by qualification engine._\n\n"
            "## Red Flags\n_To be identified by qualification engine._\n\n"
            "## Call History\n| Date | Contact | Outcome | Follow-up |\n|------|---------|---------|----------|\n\n"
            "## Objections Reference\nSee [[playbook]] for all known objections and responses.\n"
        )
    else:
        # Existing file — refresh pain signals section only
        if prospect.pain_signals:
            new_pain = "## Pain Signals\n" + "\n".join(f"- {s}" for s in prospect.pain_signals)
            if "## Pain Signals" in body:
                body = re.sub(
                    r"## Pain Signals\n.*?(?=\n## |\Z)",
                    new_pain + "\n\n",
                    body,
                    count=1,
                    flags=re.DOTALL,
                )
            else:
                body = new_pain + "\n\n" + body

    _atomic_write(path, _render_frontmatter(fm, body))
    return path


# ── SCORING ───────────────────────────────────────────────────────────────────

def update_lead_score(
    company_name: str,
    score: int,
    tier: str,
    call_priority: int,
) -> Path:
    """Update lead_score, tier, call_priority in an existing company note frontmatter."""
    slug = slugify(company_name)
    path = WIKI_DIR / "companies" / f"{slug}.md"

    fm, body = _parse_frontmatter(path.read_text(encoding="utf-8")) if path.exists() else ({}, "")

    fm.setdefault("company", company_name)
    fm["lead_score"] = score
    fm["tier"] = tier
    fm["call_priority"] = call_priority

    _atomic_write(path, _render_frontmatter(fm, body))
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
