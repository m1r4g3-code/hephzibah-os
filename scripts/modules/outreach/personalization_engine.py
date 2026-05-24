"""
Personalization engine — assembles context packages for batch intel card generation.

This engine is the mechanical arm. It reads scored leads, company wikis, the active
niche config, ME.md, and relevant objection playbook entries — and assembles them into
a structured context document. Claude Code reads that document and writes the actual
intel cards (the prose, the script, the openers).

Usage:
    python personalization_engine.py                # assemble context for all tier A/B leads
    python personalization_engine.py --tier-a       # tier A only
    python personalization_engine.py <company_slug> # single company
    python personalization_engine.py --all          # all scored leads

Output:
    logs/_personalization_context.json  — context packages for Claude Code
    Prints a summary of what needs cards vs already has them.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.schemas import EnrichedProspect, LeadScoreCard
from lib.utils import VAULT_ROOT, SOURCES_DIR, WIKI_DIR, LOGS_DIR, now_iso, slugify

ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"
ME_MD_PATH = VAULT_ROOT / "ME.md"
PLAYBOOK_PATH = WIKI_DIR / "objections" / "playbook.md"
INTEL_CARDS_DIR = SOURCES_DIR / "prospects" / "intel_cards"
SCORED_DIR = SOURCES_DIR / "prospects" / "scored"


# ── LOADERS ────────────────────────────────────────────────────────────────────

def _load_niche() -> dict:
    active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
    return yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))


def _load_operator_profile() -> str:
    if ME_MD_PATH.exists():
        return ME_MD_PATH.read_text(encoding="utf-8")
    return "_ME.md not found — personalization will be generic._"


def _load_playbook_excerpts(max_entries: int = 6) -> str:
    if not PLAYBOOK_PATH.exists():
        return "_No objection playbook yet._"
    content = PLAYBOOK_PATH.read_text(encoding="utf-8")
    # Return the first N objection entries (### sections)
    entries = content.split("### ")
    if len(entries) <= 1:
        return content[:1500]
    # Take up to max_entries entries, trim whitespace
    selected = entries[1:max_entries + 1]
    return "### " + "\n---\n### ".join(e.strip() for e in selected)


def _load_company_wiki(company_name: str) -> str:
    slug = slugify(company_name)
    path = WIKI_DIR / "companies" / f"{slug}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"_No wiki entry found for {company_name}._"


def _load_contact_wiki(company_name: str) -> str:
    """Look for a contact note associated with this company."""
    slug = slugify(company_name)
    contacts_dir = WIKI_DIR / "contacts"
    if not contacts_dir.exists():
        return ""
    # Find contacts that reference this company
    for contact_file in contacts_dir.glob("*.md"):
        content = contact_file.read_text(encoding="utf-8")
        if slug in content or company_name.lower() in content.lower():
            return content
    return ""


def _load_scored_cards(tiers: set[str] | None = None) -> list[LeadScoreCard]:
    """Load all scored leads, optionally filtered by tier."""
    cards = []
    if not SCORED_DIR.exists():
        return cards
    for f in sorted(SCORED_DIR.glob("scored_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True):
        with f.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    card = LeadScoreCard.model_validate_json(line)
                    if tiers is None or card.tier in tiers:
                        cards.append(card)
                except Exception:
                    continue
    # Sort by call_priority
    cards.sort(key=lambda c: c.call_priority)
    return cards


def _card_exists(company_name: str) -> bool:
    slug = slugify(company_name)
    return (INTEL_CARDS_DIR / f"{slug}.md").exists()


# ── CONTEXT ASSEMBLY ───────────────────────────────────────────────────────────

def _assemble_context(card: LeadScoreCard, niche: dict, operator_profile: str, playbook: str) -> dict:
    """
    Assemble all context for one lead into a structured dict.
    Claude Code reads this and generates the intel card.
    """
    company_wiki = _load_company_wiki(card.company_name)
    contact_wiki = _load_contact_wiki(card.company_name)

    # Summarize dimension scores for Claude Code
    dimension_summary = []
    for dim in sorted(card.dimensions, key=lambda d: d.score * d.weight, reverse=True):
        dimension_summary.append({
            "name": dim.name,
            "score": dim.score,
            "weight": dim.weight,
            "evidence": dim.evidence,
        })

    return {
        "company_name": card.company_name,
        "company_slug": slugify(card.company_name),
        "lead_score": card.total_score,
        "tier": card.tier,
        "call_priority": card.call_priority,
        "card_exists": _card_exists(card.company_name),
        "niche": niche["niche"],
        "niche_display": niche["display_name"],
        "pain_angle": niche["pain_angle"],
        "niche_opener_templates": niche.get("opener_templates", {}),
        "niche_known_objections": niche.get("known_objections", []),
        "dimension_scores": dimension_summary,
        "company_wiki": company_wiki,
        "contact_wiki": contact_wiki if contact_wiki else None,
        "operator_profile": operator_profile,
        "objection_playbook_excerpts": playbook,
    }


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def run(
    tiers: set[str] | None = None,
    single_company: str | None = None,
) -> Path:
    logger = EngineLogger("personalization_engine")
    logger.start()

    niche = _load_niche()
    operator_profile = _load_operator_profile()
    playbook = _load_playbook_excerpts()

    if single_company:
        # Build a minimal card from wiki data if no scored card exists
        cards = _load_scored_cards()
        matching = [c for c in cards if slugify(c.company_name) == slugify(single_company)]
        if not matching:
            # Create a placeholder card so we can still assemble context
            cards_to_process = [LeadScoreCard(
                company_name=single_company,
                place_id="unknown",
                scored_at=now_iso(),
                dimensions=[],
                total_score=0,
                tier="C",
                call_priority=99,
                recommended_opener="",
            )]
        else:
            cards_to_process = matching
    else:
        cards_to_process = _load_scored_cards(tiers=tiers or {"A", "B"})

    if not cards_to_process:
        logger.info("No leads found matching criteria")
        print("  No scored leads found. Run qualification_engine.py first.")
        return LOGS_DIR / "_personalization_context.json"

    # Assemble context packages
    packages = []
    already_have_card = []
    need_cards = []

    for card in cards_to_process:
        pkg = _assemble_context(card, niche, operator_profile, playbook)
        packages.append(pkg)
        if pkg["card_exists"]:
            already_have_card.append(card.company_name)
        else:
            need_cards.append(card.company_name)

    # Write context file
    LOGS_DIR.mkdir(exist_ok=True)
    context_path = LOGS_DIR / "_personalization_context.json"
    context_path.write_text(
        json.dumps({
            "generated_at": now_iso(),
            "niche": niche["niche"],
            "total_packages": len(packages),
            "need_cards": need_cards,
            "already_have_cards": already_have_card,
            "packages": packages,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.finish(
        items_processed=len(packages),
        output_path=str(context_path),
    )
    logger.info(
        "Context assembled",
        need_cards=len(need_cards),
        already_have_cards=len(already_have_card),
    )

    return context_path


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()

    arg = sys.argv[1] if len(sys.argv) > 1 else "--tier-ab"
    single = None
    tiers = {"A", "B"}

    if arg == "--tier-a":
        tiers = {"A"}
    elif arg == "--tier-ab":
        tiers = {"A", "B"}
    elif arg == "--all":
        tiers = None
    elif not arg.startswith("--"):
        single = arg
        tiers = None

    niche = _load_niche()
    console.print(f"\n[bold]Personalization Engine[/bold] — {niche['display_name']}")

    context_path = run(tiers=tiers, single_company=single)

    # Read back and show summary
    ctx = json.loads(context_path.read_text(encoding="utf-8"))
    console.print(f"\n  Context assembled for [bold]{ctx['total_packages']}[/bold] leads")

    if ctx["need_cards"]:
        console.print(f"  [yellow]Need intel cards:[/yellow] {len(ctx['need_cards'])} leads")
        for name in ctx["need_cards"][:10]:
            console.print(f"    · {name}")

    if ctx["already_have_cards"]:
        console.print(f"  [green]Already have cards:[/green] {len(ctx['already_have_cards'])} leads")

    console.print(f"\n  Context written to [cyan]logs/_personalization_context.json[/cyan]")
    console.print(f"  Run /prep-call <company> to generate individual cards,")
    console.print(f"  or Claude Code can read the context file to batch-generate all.")
