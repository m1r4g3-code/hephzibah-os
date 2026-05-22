"""
Call Intelligence Engine.

Reads a transcript file, extracts structured CallAnalysis objects
(one per distinct call found), writes wiki entries via vault.py.

Usage:
  python scripts/engines/call_intelligence_engine.py sources/calls/FkgGv2iMjEo.txt
  python scripts/engines/call_intelligence_engine.py --batch   # all unprocessed
"""

from __future__ import annotations
import json
import sys
import argparse
from pathlib import Path

# Allow running from vault root or scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.logger import EngineLogger
from lib.utils import (
    SOURCES_DIR, VAULT_ROOT,
    is_transcript_processed, mark_transcript_processed,
    most_recent_transcript, now_iso,
)
from lib.vault import write_contact_note, write_company_note, append_objection
from lib.schemas import CallAnalysis, CallOutcome, ObjectionInstance, CoachingFlag

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
except ImportError:
    console = None

log = EngineLogger("call_intelligence_engine")


# ── TRANSCRIPT SPLITTING ──────────────────────────────────────────────────────

def split_into_calls(text: str) -> list[str]:
    """
    Heuristically split a multi-call transcript into individual calls.
    Splits on patterns like "All right" / "Okay" after a clear call-end phrase.
    Falls back to treating the whole transcript as one call block.
    """
    import re
    # Look for natural call boundaries: "Bye. Bye." or "Thank you. Bye." followed
    # by new-call setup language
    boundary_pattern = re.compile(
        r"(?:Bye\.\s+Bye|Thank you\.\s+Bye|Take care\.\s+Bye)"
        r"(?:\s+.*?)"
        r"(?=(?:All right|Alright|Okay|Here we go|Let me|I'm gonna|I'm going to)\b)",
        re.IGNORECASE | re.DOTALL,
    )
    splits = boundary_pattern.split(text)
    # If no meaningful split found, return whole text
    if len(splits) <= 1:
        return [text]

    # Re-attach the matched boundary to each preceding segment
    calls = []
    matches = boundary_pattern.findall(text)
    pos = 0
    for match in boundary_pattern.finditer(text):
        calls.append(text[pos:match.end()])
        pos = match.end()
    calls.append(text[pos:])
    return [c.strip() for c in calls if len(c.strip()) > 200]


# ── STRUCTURED EXTRACTION ─────────────────────────────────────────────────────

_ANALYSIS_PROMPT = """You are an elite sales intelligence analyst. Analyze this cold call transcript segment and extract a precise, structured analysis.

TRANSCRIPT:
{transcript}

SOURCE FILE: {source_file}

Extract the following — be exact, cite real quotes, do not invent:

1. PROSPECT: name, company name, phone (if mentioned)
2. OUTCOME: one of [voicemail, hung_up, gatekeeper_blocked, interested, callback_scheduled, booked, rejected, dead]
3. OUTCOME_CONFIDENCE: 0.0–1.0
4. OBJECTIONS: list each objection with:
   - exact_quote: the verbatim words the prospect used
   - category: budget | timing | no_need | trust | competitor | other
   - caller_response: what the caller actually said back
   - response_quality: folded | weak_pivot | strong_pivot | closed
5. WINNING_PHRASES: exact phrases the caller used that kept the prospect engaged
6. RAPPORT_MOMENTS: specific moments where genuine connection happened
7. COACHING_FLAGS: problems in the caller's delivery:
   - flag_type: let_go_moment | filler_density | pitch_rushed | close_vague | over_explained | lost_frame
   - exact_quote: the specific line where the problem occurred
   - severity: minor | moderate | critical
   - coaching_note: precisely what was wrong and what to do instead
8. FILLER_WORD_COUNT: count of um/uh/like/you know/sort of
9. CLOSE_ATTEMPTED: true/false
10. CLOSE_TYPE: specific_datetime | vague | no_attempt
11. FOLLOW_UP_DATE: ISO date if a specific date was mentioned
12. FOLLOW_UP_ACTION: what the caller promised to do next
13. ONE_LINE_SUMMARY: one sentence, outcome + prospect name + key signal
14. FULL_ANALYSIS: 3–5 sentences. What happened, why it went that way, what the decisive moment was.

Return ONLY valid JSON matching this exact structure:
{{
  "transcript_file": "{source_file}",
  "prospect_name": null,
  "company_name": null,
  "phone": null,
  "outcome": "voicemail",
  "outcome_confidence": 0.9,
  "objections": [],
  "winning_phrases": [],
  "rapport_moments": [],
  "coaching_flags": [],
  "filler_word_count": null,
  "close_attempted": false,
  "close_type": null,
  "follow_up_date": null,
  "follow_up_action": null,
  "one_line_summary": "",
  "full_analysis": ""
}}"""


def extract_call_analysis(transcript_chunk: str, source_file: str) -> CallAnalysis | None:
    """
    Claude Code calls this function — it prints the prompt for me to analyze
    and reads back the JSON I output. In automated/CLI mode it parses
    the JSON from my stdout response written to a temp file.

    In interactive Claude Code sessions this is handled by the /analyze-call
    command which reads my analysis directly.
    """
    prompt = _ANALYSIS_PROMPT.format(
        transcript=transcript_chunk[:80000],
        source_file=source_file,
    )

    # Write prompt to a temp file Claude Code can read
    prompt_path = VAULT_ROOT / "logs" / "_current_analysis_prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")
    return None  # Claude Code reads the prompt and returns structured analysis


# ── MANUAL/BATCH PROCESSING ───────────────────────────────────────────────────

def process_transcript(path: Path, force: bool = False) -> list[dict]:
    """
    Process a transcript file. Returns list of raw analysis dicts
    that Claude Code will populate when invoked via /analyze-call.
    """
    filename = path.name
    if not force and is_transcript_processed(filename):
        if console:
            console.print(f"[yellow]Already processed:[/] {filename} — use --force to reprocess")
        return []

    log.start(str(path))
    text = path.read_text(encoding="utf-8")

    if console:
        console.print(f"\n[bold cyan]Processing:[/] {filename} ({len(text):,} chars)")

    # Split into individual calls
    chunks = split_into_calls(text)
    if console:
        console.print(f"[dim]Found {len(chunks)} call segment(s)[/]")

    # Write the full prompt context for Claude Code to analyze
    context_path = VAULT_ROOT / "logs" / "_analysis_context.json"
    context = {
        "transcript_file": filename,
        "transcript_path": str(path),
        "total_chunks": len(chunks),
        "chunks": [{"index": i, "text": c[:3000] + "..." if len(c) > 3000 else c}
                   for i, c in enumerate(chunks)],
        "full_transcript": text,
        "requested_at": now_iso(),
    }
    context_path.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")

    if console:
        console.print(f"[dim]Analysis context written to logs/_analysis_context.json[/]")
        console.print("[bold]Ready for Claude Code analysis[/]")

    log.finish(items_processed=len(chunks), output_path=str(context_path))
    return chunks


def write_analysis_results(analyses: list[CallAnalysis], source_file: str) -> dict:
    """
    Takes a list of CallAnalysis objects (produced by Claude Code analysis)
    and writes all vault entries. Returns a summary dict.
    """
    contacts_written = []
    companies_written = []
    objections_added = 0
    coaching_flags_total = 0

    for analysis in analyses:
        # Write contact note
        if analysis.prospect_name or analysis.company_name:
            if analysis.prospect_name:
                contact_path = write_contact_note(analysis)
                contacts_written.append(contact_path.stem)

            if analysis.company_name:
                stage = "contacted" if analysis.outcome not in [
                    CallOutcome.VOICEMAIL, CallOutcome.GATEKEEPER_BLOCKED
                ] else "attempted"
                company_path = write_company_note(
                    analysis.company_name,
                    stage=stage,
                    last_contact=analysis.call_date,
                )
                companies_written.append(company_path.stem)

        # Append objections to playbook
        for objection in analysis.objections:
            append_objection(objection, source_file)
            objections_added += 1

        coaching_flags_total += len(analysis.coaching_flags)

    mark_transcript_processed(source_file)

    return {
        "contacts_written": contacts_written,
        "companies_written": companies_written,
        "objections_added": objections_added,
        "coaching_flags": coaching_flags_total,
    }


# ── DISPLAY ───────────────────────────────────────────────────────────────────

def display_analysis(analysis: CallAnalysis) -> None:
    if not console:
        print(f"\n{analysis.one_line_summary}")
        return

    console.print()
    console.rule(f"[bold]{analysis.company_name or 'Unknown'} — {analysis.prospect_name or '?'}")

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(style="dim", width=18)
    table.add_column()
    table.add_row("Outcome", f"[bold]{analysis.outcome.value}[/] ({analysis.outcome_confidence:.0%} confidence)")
    table.add_row("Summary", analysis.one_line_summary)
    if analysis.follow_up_date:
        table.add_row("Follow-up", f"{analysis.follow_up_date} — {analysis.follow_up_action or ''}")
    if analysis.close_type:
        table.add_row("Close", analysis.close_type)
    console.print(table)

    if analysis.coaching_flags:
        console.print("\n[bold red]Coaching Flags:[/]")
        for flag in analysis.coaching_flags:
            color = {"critical": "red", "moderate": "yellow", "minor": "dim"}.get(flag.severity, "white")
            console.print(f"  [{color}][{flag.severity.upper()}][/] {flag.coaching_note}")
            console.print(f"  [dim]  → \"{flag.exact_quote[:80]}\"[/]")

    if analysis.objections:
        console.print("\n[bold yellow]Objections:[/]")
        for obj in analysis.objections:
            console.print(f"  [{obj.response_quality}] \"{obj.exact_quote[:70]}\"")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Call Intelligence Engine")
    parser.add_argument("transcript", nargs="?", help="Path to transcript .txt file")
    parser.add_argument("--batch", action="store_true", help="Process all unprocessed transcripts")
    parser.add_argument("--force", action="store_true", help="Reprocess even if already done")
    args = parser.parse_args()

    calls_dir = SOURCES_DIR / "calls"

    if args.batch:
        files = sorted(calls_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime)
        if not files:
            print("No transcript files found in sources/calls/")
            sys.exit(0)
        for f in files:
            process_transcript(f, force=args.force)
    elif args.transcript:
        path = Path(args.transcript)
        if not path.is_absolute():
            # Try relative to vault root first, then calls dir
            if (VAULT_ROOT / path).exists():
                path = VAULT_ROOT / path
            elif (calls_dir / path.name).exists():
                path = calls_dir / path.name
        if not path.exists():
            print(f"File not found: {args.transcript}")
            sys.exit(1)
        process_transcript(path, force=args.force)
    else:
        # Default: most recent transcript
        recent = most_recent_transcript()
        if not recent:
            print("No transcripts in sources/calls/")
            sys.exit(1)
        process_transcript(recent, force=args.force)


if __name__ == "__main__":
    main()
