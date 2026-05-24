"""
Qualification engine — scores enriched leads 0-100, assigns tier and priority.

Usage:
    python qualification_engine.py                 # score latest enriched file
    python qualification_engine.py --latest        # same
    python qualification_engine.py --all           # all unscored enriched files
    python qualification_engine.py enriched_foo.jsonl

Input:   sources/prospects/enriched_*.jsonl
Output:  sources/prospects/scored/scored_<batch>.jsonl  (LeadScoreCard per lead)
         wiki/companies/<slug>.md  frontmatter updated: lead_score, tier, call_priority

Scoring:
    Each niche config defines dimension names + weights.
    This engine maps those names to deterministic scoring functions
    that work from available EnrichedProspect signals.
    All scores are 1–10 per dimension; weighted average → 0–100 total.
    recommended_opener is left blank — Claude Code fills it via /prep-call.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.schemas import EnrichedProspect, LeadScoreCard, ScoreDimension
from lib.utils import VAULT_ROOT, SOURCES_DIR, now_iso
from lib.vault import update_lead_score

ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"


# ── NICHE CONFIG ───────────────────────────────────────────────────────────────

def _load_niche() -> dict:
    active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
    return yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))


# ── DIMENSION SCORING FUNCTIONS ────────────────────────────────────────────────
#
# Each function takes an EnrichedProspect and returns (score: int 1-10, evidence: str).
# Higher score = higher opportunity (not quality of the business).

def _score_website_gap(p: EnrichedProspect) -> tuple[int, str]:
    """No or broken website = huge opportunity."""
    if not p.website:
        return 9, "No website — entirely dependent on word-of-mouth"
    ws = p.website_signals
    if not ws or ws.fetch_status == "error":
        return 8, "Website broken or unreachable"
    if ws.fetch_status == "timeout":
        return 7, "Website very slow or down"
    quality_scores = {"poor": 8, "average": 5, "good": 2}
    return quality_scores[ws.quality_score], f"Website quality: {ws.quality_score}"


def _score_website_quality(p: EnrichedProspect) -> tuple[int, str]:
    """Proxy for tech adoption: good website = more tech-savvy buyer."""
    if not p.website:
        return 2, "No website"
    ws = p.website_signals
    if not ws or ws.fetch_status in ("error", "timeout"):
        return 3, f"Website fetch failed ({ws.fetch_status if ws else 'unknown'})"
    quality_scores = {"poor": 3, "average": 6, "good": 9}
    return quality_scores[ws.quality_score], f"Website quality: {ws.quality_score}"


def _score_booking_gap(p: EnrichedProspect) -> tuple[int, str]:
    """No online booking on a service business = concrete automatable pain."""
    if not p.website:
        return 9, "No website — no booking possible"
    ws = p.website_signals
    if not ws or ws.fetch_status in ("error", "timeout"):
        return 7, "Website issues — booking unknown"
    if not ws.has_booking_form:
        return 8, "No booking form or scheduling link on website"
    return 3, "Booking form present"


def _score_pain_signals(p: EnrichedProspect) -> tuple[int, str]:
    """More detected pain signals = more obvious opportunity."""
    n = len(p.pain_signals)
    if n == 0:
        return 1, "No pain signals detected"
    if n == 1:
        return 4, f"1 signal: {p.pain_signals[0][:50]}"
    if n == 2:
        return 6, f"2 signals detected"
    if n == 3:
        return 8, f"3 signals: strong indicators"
    return 10, f"{n} signals: multiple clear pain points"


def _score_volume_sweet_spot(p: EnrichedProspect) -> tuple[int, str]:
    """
    Review count as a proxy for business size.
    Sweet spot: 10–80 reviews = established but not a large chain with IT staff.
    """
    rc = p.review_count
    if not rc:
        return 5, "Review count unknown"
    if rc < 5:
        return 3, f"{rc} reviews — very new or quiet, uncertain viability"
    if 5 <= rc <= 15:
        return 7, f"{rc} reviews — small but established"
    if 16 <= rc <= 80:
        return 9, f"{rc} reviews — sweet spot (real business, feels the pain)"
    if 81 <= rc <= 200:
        return 6, f"{rc} reviews — mid-size, may have some infrastructure"
    return 3, f"{rc} reviews — large operation, likely has staff/IT"


def _score_reachability(p: EnrichedProspect) -> tuple[int, str]:
    """Can we actually get to the decision maker?"""
    has_phone = bool(p.phone and len(p.phone.strip()) > 5)
    has_website = bool(p.website)
    if has_phone:
        return 9, f"Direct phone: {p.phone}"
    if has_website:
        return 6, "Website contact form (no direct phone)"
    return 2, "No contact method found"


def _score_independence(p: EnrichedProspect) -> tuple[int, str]:
    """
    Small independent operation = decision maker is on-site, budget is personal.
    Use review count + chain signals as proxy.
    """
    rc = p.review_count or 0
    name_lower = p.company_name.lower()
    chain_keywords = ["corp", "group", "holdings", "llc", "partners", "associates", "national"]
    likely_chain = any(kw in name_lower for kw in chain_keywords)

    if likely_chain:
        return 4, "Name suggests group/chain structure — may not be independent"
    if rc < 50:
        return 8, "Small review footprint — likely single-location independent"
    if rc < 150:
        return 6, "Mid-size — independence uncertain"
    return 3, "Large operation — likely not independent owner-operator"


def _score_social_gap(p: EnrichedProspect) -> tuple[int, str]:
    """Missing or weak social = opportunity to pitch content/social automation."""
    has_ig = bool(p.instagram_handle)
    has_fb = bool(p.facebook_url)
    if not has_ig and not has_fb:
        return 8, "No social presence found — clear opportunity"
    if not has_ig or not has_fb:
        return 5, "Partial social presence"
    return 3, "Has both Instagram and Facebook"


def _score_copyright_age(p: EnrichedProspect) -> tuple[int, str]:
    """Old copyright year = neglected website = opportunity."""
    from datetime import datetime
    current_year = datetime.now().year
    ws = p.website_signals
    if not ws or not ws.copyright_year:
        return 5, "Copyright year unknown"
    age = current_year - ws.copyright_year
    if age >= 3:
        return 8, f"Website copyright {ws.copyright_year} — {age} years old"
    if age >= 1:
        return 5, f"Website copyright {ws.copyright_year}"
    return 3, f"Website updated recently ({ws.copyright_year})"


# Dimension name → scorer function
_SCORERS: dict[str, callable] = {
    # Website / digital presence
    "website_quality":            _score_website_quality,
    "website_gap":                _score_website_gap,
    "digital_maturity":           _score_website_quality,
    "tech_sophistication":        _score_website_quality,
    "booking_gap":                _score_booking_gap,
    "intake_automation_gap":      _score_booking_gap,

    # Pain / manual ops
    "admin_pain_signals":         _score_pain_signals,
    "manual_ops_signals":         _score_pain_signals,
    "pain_signal_count":          _score_pain_signals,
    "document_volume_practice_area": _score_pain_signals,
    "reporting_automation":       _score_pain_signals,

    # Size / volume sweet spot
    "patient_volume_sweet_spot":  _score_volume_sweet_spot,
    "team_size_sweet_spot":       _score_volume_sweet_spot,
    "review_volume_sweet_spot":   _score_volume_sweet_spot,
    "firm_size_sweet_spot":       _score_volume_sweet_spot,
    "client_count_signal":        _score_volume_sweet_spot,
    "order_volume_signal":        _score_volume_sweet_spot,

    # Reachability
    "decision_maker_reachable":   _score_reachability,
    "contact_accessibility":      _score_reachability,

    # Independence
    "practice_independence":      _score_independence,

    # Social
    "social_presence_gap":        _score_social_gap,
    "social_media_gap":           _score_social_gap,

    # Funding (unknown from Maps — neutral)
    "funding_stage":              lambda p: (5, "Funding stage unknown from Maps data"),

    # Geography (neutral — all prospects are in target market by definition)
    "geography_rpm":              lambda p: (7, "Target market"),
}


def _score_dimension(name: str, p: EnrichedProspect) -> tuple[int, str]:
    fn = _SCORERS.get(name)
    if fn:
        return fn(p)
    # Fallback: pain signal proxy
    return _score_pain_signals(p)


# ── SCORING ────────────────────────────────────────────────────────────────────

def _assign_tier(score: int, thresholds: dict) -> str:
    for tier in ("A", "B", "C"):
        if score >= thresholds.get(tier, {"A": 80, "B": 60, "C": 40}[tier]):
            return tier
    return "D"


def score_prospect(p: EnrichedProspect, niche: dict, priority_rank: int = 1) -> LeadScoreCard:
    dimensions_config = niche.get("dimensions", [])
    tier_thresholds = niche.get("tiers", {"A": 80, "B": 60, "C": 40, "D": 0})

    scored_dims: list[ScoreDimension] = []
    total_weight = 0.0
    weighted_sum = 0.0

    for dim_cfg in dimensions_config:
        name = dim_cfg["name"]
        weight = float(dim_cfg.get("weight", 0.1))
        raw_score, evidence = _score_dimension(name, p)

        scored_dims.append(ScoreDimension(
            name=name,
            score=raw_score,
            weight=weight,
            evidence=evidence,
        ))
        weighted_sum += raw_score * weight
        total_weight += weight

    if total_weight > 0:
        # Normalize to 0-100
        total_score = int(round((weighted_sum / total_weight) * 10))
    else:
        total_score = 50

    # Cap at 100
    total_score = min(100, max(0, total_score))
    tier = _assign_tier(total_score, tier_thresholds)

    return LeadScoreCard(
        company_name=p.company_name,
        place_id=p.place_id,
        scored_at=now_iso(),
        dimensions=scored_dims,
        total_score=total_score,
        tier=tier,
        call_priority=priority_rank,
        recommended_opener="",  # Filled by Claude Code via /prep-call
        skip_reason=None,
    )


def score_batch(prospects: list[EnrichedProspect], niche: dict) -> list[LeadScoreCard]:
    """Score all prospects, sort by total_score desc, assign priority ranks."""
    cards = [score_prospect(p, niche) for p in prospects]
    cards.sort(key=lambda c: c.total_score, reverse=True)
    for rank, card in enumerate(cards, 1):
        card.call_priority = rank
    return cards


# ── I/O ────────────────────────────────────────────────────────────────────────

def _load_enriched(path: Path) -> list[EnrichedProspect]:
    out = []
    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append(EnrichedProspect.model_validate_json(line))
            except Exception as e:
                print(f"  Warning: skipping line {i} — {e}")
    return out


def run(input_path: Path) -> tuple[Path, list[LeadScoreCard]]:
    niche = _load_niche()
    logger = EngineLogger("qualification_engine")
    logger.start(input_path=str(input_path))

    prospects = _load_enriched(input_path)
    if not prospects:
        raise ValueError(f"No valid enriched prospects in {input_path.name}")

    logger.info(f"Scoring {len(prospects)} prospects", niche=niche["niche"])

    cards = score_batch(prospects, niche)

    # Write scored JSONL
    scored_dir = SOURCES_DIR / "prospects" / "scored"
    scored_dir.mkdir(parents=True, exist_ok=True)
    out_name = input_path.name.replace("enriched_", "scored_", 1)
    if not out_name.startswith("scored_"):
        out_name = "scored_" + out_name
    output_path = scored_dir / out_name

    with output_path.open("w", encoding="utf-8") as f:
        for card in cards:
            f.write(card.model_dump_json() + "\n")

    # Update wiki/companies/ frontmatter
    wiki_updated = 0
    for card in cards:
        try:
            update_lead_score(
                company_name=card.company_name,
                score=card.total_score,
                tier=card.tier,
                call_priority=card.call_priority,
            )
            wiki_updated += 1
        except Exception as e:
            logger.error("wiki_update_error", f"{card.company_name}: {e}")

    logger.finish(
        items_processed=len(cards),
        output_path=str(output_path),
    )
    logger.info(f"Wiki frontmatter updated for {wiki_updated} companies")

    return output_path, cards


def _find_targets(arg: str | None) -> list[Path]:
    enriched_dir = SOURCES_DIR / "prospects"
    scored_dir = enriched_dir / "scored"

    if not arg or arg == "--latest":
        files = sorted(enriched_dir.glob("enriched_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
        return [files[0]] if files else []

    if arg == "--all":
        files = sorted(enriched_dir.glob("enriched_*.jsonl"), key=lambda p: p.stat().st_mtime)
        out = []
        for f in files:
            scored_name = f.name.replace("enriched_", "scored_", 1)
            if not (scored_dir / scored_name).exists():
                out.append(f)
        return out

    p = Path(arg)
    if not p.is_absolute():
        p = enriched_dir / p
    return [p] if p.exists() else []


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console
    from rich.table import Table

    console = Console()
    arg = sys.argv[1] if len(sys.argv) > 1 else "--latest"
    targets = _find_targets(arg)

    if not targets:
        console.print(f"[red]No enriched leads found for:[/red] {arg}")
        console.print("  Run research_engine.py first.")
        sys.exit(1)

    niche = _load_niche()
    console.print(f"\n[bold]Qualification Engine[/bold] — {niche['display_name']}")

    all_cards: list[LeadScoreCard] = []
    for t in targets:
        console.print(f"  Scoring: [cyan]{t.name}[/cyan]")
        output_path, cards = run(t)
        all_cards.extend(cards)

    # Summary table — top 15
    table = Table(show_header=True, header_style="bold")
    table.add_column("Priority", style="dim", width=4)
    table.add_column("Company", min_width=28)
    table.add_column("Score", justify="right", width=6)
    table.add_column("Tier", width=5)
    table.add_column("Top Pain Signal", min_width=36)

    all_cards.sort(key=lambda c: c.total_score, reverse=True)
    for card in all_cards[:15]:
        tier_style = {"A": "bold green", "B": "green", "C": "yellow", "D": "red"}.get(card.tier, "")
        # Find top dimension by score
        top_dim = max(card.dimensions, key=lambda d: d.score * d.weight, default=None)
        signal = top_dim.evidence[:40] if top_dim else "—"
        table.add_row(
            str(card.call_priority),
            card.company_name[:30],
            str(card.total_score),
            f"[{tier_style}]{card.tier}[/{tier_style}]",
            signal,
        )

    console.print(f"\n  Scored [bold]{len(all_cards)}[/bold] leads -> output in [cyan]sources/prospects/scored/[/cyan]\n")
    console.print(table)
    console.print(f"\n  Wiki frontmatter updated for all companies.")
    console.print(f"  Next: /prep-call <company> or python personalization_engine.py")
