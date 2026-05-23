"""
Research engine — enriches raw leads with website signals.

Usage:
    python research_engine.py                 # process latest leads file
    python research_engine.py --latest        # same as above
    python research_engine.py --all           # process all unprocessed leads files
    python research_engine.py leads_foo.jsonl # specific file

Input:   sources/prospects/leads_*.jsonl
Output:  sources/prospects/enriched_*.jsonl
         wiki/companies/<slug>.md  (stub notes written via vault.py)

Performance:
    40 concurrent website fetches → 50 leads enriched in ~8s typical.
    Instagram/Facebook skipped here — Playwright-based social enrichment is M4.
"""

from __future__ import annotations

import asyncio
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import aiohttp
import yaml
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.logger import EngineLogger
from lib.schemas import EnrichedProspect, RawProspect, SocialSignals, WebsiteSignals
from lib.utils import VAULT_ROOT, SOURCES_DIR, now_iso
from lib.vault import write_prospect_stub

# ── CONFIG ─────────────────────────────────────────────────────────────────────

MAX_CONCURRENT = 40
FETCH_TIMEOUT = aiohttp.ClientTimeout(total=8, connect=4)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Known CMS fingerprints — first match wins, order matters
CMS_FINGERPRINTS: list[tuple[str, list[str]]] = [
    ("WordPress",     ["/wp-content/", "/wp-includes/", "wp-json", "xmlrpc.php", "wp-block-"]),
    ("Wix",           ["wixsite.com", "static.wixstatic.com", "_next/static/wix"]),
    ("Squarespace",   ["squarespace.com", "static1.squarespace.com", "sqsp.net"]),
    ("Shopify",       ["cdn.shopify.com", "myshopify.com"]),
    ("Webflow",       ["webflow.io", "assets-global.website-files.com"]),
    ("Framer",        ["framer.com", "framer.website"]),
    ("GoDaddy",       ["godaddy.com", "secureserver.net", "godaddysites.com"]),
    ("HubSpot",       ["hs-sites.com", "hsforms.com", "hubspot.com"]),
    ("Joomla",        ["/components/com_", "joomla"]),
    ("Drupal",        ["drupal.js", "drupal.settings", "/sites/default/"]),
]

BOOKING_SIGNALS = [
    "book now", "book appointment", "book online", "schedule appointment",
    "schedule a visit", "request appointment", "make an appointment",
    "calendly.com", "acuityscheduling.com", "squareup.com/appointments",
    "zocdoc.com", "healthgrades.com", "doctorondemand.com", "mindbodyonline.com",
]

ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"


def _load_niche() -> dict:
    active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
    return yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))


# ── WEBSITE ENRICHMENT ─────────────────────────────────────────────────────────

def _normalize_url(url: str) -> str:
    if not url:
        return url
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url


def _detect_cms(html_lower: str) -> str | None:
    for name, patterns in CMS_FINGERPRINTS:
        if any(p.lower() in html_lower for p in patterns):
            return name
    return None


def _score_quality(soup: BeautifulSoup, text_content: str) -> str:
    words = len(text_content.split())
    has_nav = bool(soup.find("nav") or soup.find(attrs={"role": "navigation"}))
    has_images = bool(soup.find("img"))
    has_headings = bool(soup.find(["h1", "h2", "h3"]))

    score = 0
    if words > 400:
        score += 2
    elif words > 150:
        score += 1
    if has_nav:
        score += 1
    if has_images:
        score += 1
    if has_headings:
        score += 1

    if score >= 4:
        return "good"
    if score >= 2:
        return "average"
    return "poor"


_EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
)
_EMAIL_BLOCKLIST = {"example.com", "sentry.io", "wixpress.com", "squarespace.com",
                    "wordpress.com", "godaddy.com", "schema.org"}


def _extract_email(html: str, domain: str) -> str | None:
    """Extract the most relevant contact email from page HTML."""
    candidates: list[str] = []

    # mailto: links first — highest confidence
    for m in re.finditer(r'mailto:([^\'"?\s&]+)', html, re.IGNORECASE):
        candidates.append(m.group(1).lower().strip())

    # Plain text email addresses
    for m in _EMAIL_RE.finditer(html):
        candidates.append(m.group(0).lower().strip())

    seen: set[str] = set()
    for email in candidates:
        if email in seen:
            continue
        seen.add(email)
        # Skip tracking pixels, CDN addresses, blocked domains
        email_domain = email.split("@")[-1]
        if email_domain in _EMAIL_BLOCKLIST:
            continue
        if any(skip in email for skip in ("@2x", "noreply", "no-reply", ".png", ".jpg")):
            continue
        # Prefer emails on the same domain as the website
        if domain and domain in email_domain:
            return email

    # Fallback: return first valid candidate regardless of domain match
    for email in seen:
        email_domain = email.split("@")[-1]
        if email_domain not in _EMAIL_BLOCKLIST:
            if not any(skip in email for skip in ("@2x", "noreply", "no-reply", ".png", ".jpg")):
                return email

    return None


async def _fetch_website(
    session: aiohttp.ClientSession,
    raw_url: str,
    logger: EngineLogger,
) -> tuple[WebsiteSignals | None, str | None]:
    if not raw_url:
        return None

    url = _normalize_url(raw_url)
    has_ssl = url.startswith("https://")
    try:
        domain = url.split("/")[2].lstrip("www.")
    except IndexError:
        domain = ""

    try:
        async with session.get(url, headers=HEADERS, allow_redirects=True, ssl=False) as resp:
            if str(resp.url).startswith("https://"):
                has_ssl = True

            if resp.status >= 400:
                return WebsiteSignals(
                    fetch_status="error",
                    has_ssl=has_ssl,
                    quality_score="poor",
                ), None

            html = await resp.text(errors="replace")
            html_lower = html.lower()
            soup = BeautifulSoup(html, "html.parser")
            text_content = soup.get_text(separator=" ")

            cms = _detect_cms(html_lower)
            quality = _score_quality(soup, text_content)

            text_lower = text_content.lower()
            has_booking = any(signal in text_lower for signal in BOOKING_SIGNALS)

            copyright_year = None
            copy_match = re.search(r"©\s*(\d{4})", html)
            if not copy_match:
                copy_match = re.search(r"copyright\s+(\d{4})", html_lower)
            if copy_match:
                try:
                    yr = int(copy_match.group(1))
                    if 1990 < yr <= datetime.now().year:
                        copyright_year = yr
                except ValueError:
                    pass

            email = _extract_email(html, domain)

            return WebsiteSignals(
                quality_score=quality,
                cms_detected=cms,
                has_booking_form=has_booking,
                has_ssl=has_ssl,
                copyright_year=copyright_year,
                fetch_status="success",
            ), email

    except asyncio.TimeoutError:
        return WebsiteSignals(fetch_status="timeout", has_ssl=has_ssl), None
    except Exception:
        return WebsiteSignals(fetch_status="error", has_ssl=has_ssl), None


async def _enrich_all_websites(
    prospects: list[RawProspect],
    logger: EngineLogger,
) -> dict[str, tuple[WebsiteSignals | None, str | None]]:
    """Fetch all prospect websites concurrently. Returns {place_id: (WebsiteSignals, email)}."""
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT, ssl=False)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    async def _bounded(p: RawProspect):
        async with semaphore:
            result = await _fetch_website(session, p.website or "", logger)
            return p.place_id, result

    async with aiohttp.ClientSession(connector=connector, timeout=FETCH_TIMEOUT) as session:
        tasks = [_bounded(p) for p in prospects if p.website]
        raw_results = await asyncio.gather(*tasks, return_exceptions=True)

    out: dict[str, tuple[WebsiteSignals | None, str | None]] = {}
    for item in raw_results:
        if isinstance(item, Exception):
            continue
        pid, signals_tuple = item
        out[pid] = signals_tuple
    return out


# ── PAIN SIGNAL DETECTION ──────────────────────────────────────────────────────

def _extract_pain_signals(
    prospect: RawProspect,
    ws: WebsiteSignals | None,
    niche_name: str,
) -> list[str]:
    signals: list[str] = []
    current_year = datetime.now().year

    if ws:
        if ws.quality_score == "poor":
            signals.append("Poor website — outdated, minimal, or barely functional")

        if ws.copyright_year and ws.copyright_year < current_year - 2:
            signals.append(
                f"Website copyright {ws.copyright_year} — hasn't been updated in {current_year - ws.copyright_year}+ years"
            )

        if ws.cms_detected in ("Wix", "Squarespace", "GoDaddy") and ws.quality_score != "good":
            signals.append(f"DIY {ws.cms_detected} website — likely self-managed, limited capability")

        if not ws.has_booking_form and niche_name in ("doctors", "law_firms", "florists"):
            signals.append("No online booking or appointment scheduling visible")

        if not ws.has_ssl:
            signals.append("Website running on HTTP — no SSL certificate")

        if ws.fetch_status == "error":
            signals.append("Website returned an error — may be broken or abandoned")

        if ws.fetch_status == "timeout":
            signals.append("Website timed out — very slow or unreachable")

    if not prospect.website:
        signals.append("No website found — relies entirely on Google Maps and word-of-mouth")

    if prospect.review_count is not None and prospect.review_count < 15:
        signals.append(f"Only {prospect.review_count} Google reviews — weak social proof")

    if (
        prospect.review_count
        and prospect.review_count >= 5
        and prospect.google_rating
        and prospect.google_rating < 4.0
    ):
        signals.append(f"Google rating {prospect.google_rating:.1f}/5 — below average, reputation issue")

    return signals


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def _load_raw_prospects(jsonl_path: Path) -> list[RawProspect]:
    prospects = []
    with jsonl_path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                prospects.append(RawProspect.model_validate_json(line))
            except Exception as e:
                print(f"  Warning: skipping line {i} — {e}")
    return prospects


async def _run_async(input_path: Path, logger: EngineLogger) -> tuple[Path, int, int]:
    niche = _load_niche()

    prospects = _load_raw_prospects(input_path)
    if not prospects:
        logger.error("no_input", f"No valid prospects in {input_path.name}")
        raise ValueError(f"No valid prospects in {input_path.name}")

    logger.info(f"Loaded {len(prospects)} prospects", file=input_path.name)

    # Concurrent website enrichment
    t0 = time.time()
    website_results = await _enrich_all_websites(prospects, logger)
    elapsed = round(time.time() - t0, 1)
    logger.info(
        f"Website enrichment complete",
        enriched=len(website_results),
        elapsed_s=elapsed,
    )

    # Build EnrichedProspect list
    enriched: list[EnrichedProspect] = []
    for p in prospects:
        result = website_results.get(p.place_id, (None, None))
        ws, contact_email = result if isinstance(result, tuple) else (result, None)
        pain_signals = _extract_pain_signals(p, ws, niche["niche"])

        ep = EnrichedProspect(
            **p.model_dump(),
            website_signals=ws,
            social_signals=None,
            pain_signals=pain_signals,
            contact_email=contact_email,
            enriched_at=now_iso(),
        )
        enriched.append(ep)

    # Write enriched JSONL
    out_name = input_path.name.replace("leads_", "enriched_", 1)
    if not out_name.startswith("enriched_"):
        out_name = "enriched_" + out_name
    output_path = input_path.parent / out_name

    with output_path.open("w", encoding="utf-8") as f:
        for ep in enriched:
            f.write(ep.model_dump_json() + "\n")

    # Write stub wiki/companies/ entries
    stubs_ok = 0
    stubs_fail = 0
    for ep in enriched:
        try:
            write_prospect_stub(ep)
            stubs_ok += 1
        except Exception as e:
            logger.error("vault_write_error", f"{ep.company_name}: {e}")
            stubs_fail += 1

    logger.info(f"Wiki stubs written: {stubs_ok} ok, {stubs_fail} failed")
    return output_path, len(enriched), stubs_fail


def run(input_path: Path) -> tuple[Path, int]:
    """
    Enrich a leads JSONL file. Returns (output_path, enriched_count).
    """
    logger = EngineLogger("research_engine")
    logger.start(input_path=str(input_path))

    output_path, count, failed = asyncio.run(_run_async(input_path, logger))

    logger.finish(
        items_processed=count,
        items_failed=failed,
        output_path=str(output_path),
    )
    return output_path, count


# ── CLI ────────────────────────────────────────────────────────────────────────

def _find_targets(arg: str | None) -> list[Path]:
    leads_dir = SOURCES_DIR / "prospects"

    if not arg or arg == "--latest":
        files = sorted(leads_dir.glob("leads_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
        return [files[0]] if files else []

    if arg == "--all":
        files = sorted(leads_dir.glob("leads_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
        # Skip files that already have a corresponding enriched_ file
        out = []
        for f in files:
            enriched_name = f.name.replace("leads_", "enriched_", 1)
            if not (f.parent / enriched_name).exists():
                out.append(f)
        return out

    # Specific filename
    p = Path(arg)
    if not p.is_absolute():
        p = leads_dir / p
    return [p] if p.exists() else []


if __name__ == "__main__":
    from rich.console import Console

    console = Console()
    arg = sys.argv[1] if len(sys.argv) > 1 else "--latest"
    targets = _find_targets(arg)

    if not targets:
        console.print(f"[red]No leads files found for argument:[/red] {arg}")
        console.print("  Run lead_engine.py first to generate leads.")
        sys.exit(1)

    console.print(f"\n[bold]Research Engine[/bold] — enriching {len(targets)} file(s)")

    total = 0
    for t in targets:
        console.print(f"  -> [cyan]{t.name}[/cyan]")
        output_path, count = run(t)
        total += count
        console.print(f"     [green]{count} leads enriched[/green] -> {output_path.name}")

    console.print(f"\n[bold green]Done.[/bold green] {total} total leads enriched.")
    console.print("  Wiki stubs written to [cyan]wiki/companies/[/cyan]")
    console.print("  Next: /prep-call <company> or wait for M3 qualification engine")
