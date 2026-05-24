"""
Lead engine — scrapes Google Maps for business leads.

Usage:
    python lead_engine.py <city> <state_or_country>
    python lead_engine.py Boston MA
    python lead_engine.py "New York" NY
    python lead_engine.py London UK

Output:
    sources/prospects/leads_<niche>_<city>_<YYYY-MM-DD>.jsonl

Dedup:
    Already-seen place_ids are tracked in sources/prospects/.processed_manifest.json
    Re-running the same city skips results already scraped.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote_plus

import yaml
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.schemas import RawProspect
from lib.utils import (
    VAULT_ROOT, SOURCES_DIR, now_iso, slugify,
    get_processed_place_ids, mark_place_id_processed, load_manifest, save_manifest,
)

# ── CONFIG ─────────────────────────────────────────────────────────────────────

SELECTORS_PATH = VAULT_ROOT / "config" / "selectors.yaml"
ACTIVE_NICHE_PATH = VAULT_ROOT / "config" / "active_niche.yaml"
NICHES_DIR = VAULT_ROOT / "config" / "niches"


def _load_selectors() -> dict:
    return yaml.safe_load(SELECTORS_PATH.read_text(encoding="utf-8"))["maps_search"]


def _load_niche() -> dict:
    active = yaml.safe_load(ACTIVE_NICHE_PATH.read_text(encoding="utf-8"))["active_niche"]
    return yaml.safe_load((NICHES_DIR / f"{active}.yaml").read_text(encoding="utf-8"))


# ── HELPERS ────────────────────────────────────────────────────────────────────

def _human_delay(lo: float = 0.8, hi: float = 2.2) -> None:
    import random
    time.sleep(random.uniform(lo, hi))


def _extract_place_id(url: str, fallback_seed: str = "") -> str:
    """
    Extract a stable unique ID from a Google Maps detail URL.
    Tries ChIJ format first (standard place_id), then hex CID, then hashes the URL path.
    """
    for pattern in [r"!1s(ChIJ[A-Za-z0-9_-]+)", r"!1s(0x[0-9a-fA-F]+:[0-9a-fA-F]+)"]:
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    seed = fallback_seed or url
    return "hash_" + hashlib.md5(seed.encode()).hexdigest()[:14]


def _parse_city_state(address: str) -> tuple[str, str]:
    """
    Extract city and state from a Google Maps address string.
    '123 Main St, Boston, MA 02101'  →  ('Boston', 'MA')
    '10 Downing St, London, UK'      →  ('London', 'UK')
    """
    if not address:
        return "", ""
    parts = [p.strip() for p in address.split(",")]
    if len(parts) >= 3:
        city = parts[-2].strip()
        state = parts[-1].strip().split()[0]
        return city, state
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip().split()[0]
    return parts[0].strip(), ""


def _build_search_url(query: str, sel: dict) -> str:
    return sel["url_template"].format(query=quote_plus(query))


# ── SCRAPING ───────────────────────────────────────────────────────────────────

def _scroll_feed(page, sel: dict, max_scrolls: int = 20) -> None:
    """Scroll the results sidebar until end-of-list or no new results."""
    prev_count = 0
    end_text = sel.get("end_of_list", "end of the list").lower()

    for _ in range(max_scrolls):
        # Check for end-of-list message
        try:
            if end_text in page.inner_text("body").lower():
                break
        except Exception:
            pass

        # Count current cards
        try:
            cards = page.query_selector_all(sel["result_cards"])
            current = len(cards)
        except Exception:
            break

        if current == prev_count and current > 0:
            break
        prev_count = current

        # Scroll the feed container
        try:
            feed = page.query_selector(sel["results_feed"])
            if feed:
                feed.evaluate("el => el.scrollTop += 2500")
        except Exception:
            pass

        _human_delay(1.5, 2.8)


def _collect_hrefs(page, sel: dict) -> list[str]:
    """Collect all place-detail hrefs from the current results page."""
    try:
        hrefs = page.eval_on_selector_all(
            sel["result_cards"],
            "els => els.map(el => el.href).filter(Boolean)",
        )
    except Exception:
        hrefs = []

    out = []
    for href in hrefs:
        if not href:
            continue
        if not href.startswith("http"):
            href = "https://www.google.com" + href
        if href not in out:
            out.append(href)
    return out


def _scrape_detail(page, href: str, sel: dict, logger: EngineLogger) -> dict | None:
    """
    Navigate to a place detail URL and extract all available fields.
    Returns a raw dict or None on hard failure.
    """
    from playwright.sync_api import TimeoutError as PWTimeout

    try:
        page.goto(href, wait_until="domcontentloaded", timeout=18000)
        _human_delay(1.0, 2.0)

        def _text(selector: str) -> str | None:
            try:
                el = page.query_selector(selector)
                return el.inner_text().strip() if el else None
            except Exception:
                return None

        def _attr(selector: str, attribute: str) -> str | None:
            try:
                el = page.query_selector(selector)
                return el.get_attribute(attribute) if el else None
            except Exception:
                return None

        name = _text(sel["detail_name"])
        if not name:
            return None

        # Phone — aria-label contains "Phone: (xxx) xxx-xxxx"
        phone = None
        try:
            phone_el = page.query_selector(sel["detail_phone_button"])
            if phone_el:
                aria = phone_el.get_attribute("aria-label") or ""
                # "Phone: (617) 555-0100" → "(617) 555-0100"
                phone_match = re.search(r"Phone:\s*(.+)", aria, re.IGNORECASE)
                if phone_match:
                    phone = phone_match.group(1).strip()
                else:
                    phone = phone_el.inner_text().strip() or None
        except Exception:
            pass

        # Website
        website = None
        try:
            website_el = page.query_selector(sel["detail_website"])
            if website_el:
                website = website_el.get_attribute("href")
        except Exception:
            pass

        # Address
        address = _text(sel["detail_address"])

        # Category
        category = _text(sel["detail_category"])

        # Rating
        rating = None
        rating_raw = _text(sel["detail_rating"])
        if rating_raw:
            try:
                rating = float(rating_raw.replace(",", "."))
            except ValueError:
                pass

        # Review count
        review_count = None
        try:
            rc_el = page.query_selector(sel["detail_review_count"])
            if rc_el:
                aria = rc_el.get_attribute("aria-label") or rc_el.inner_text()
                nums = re.findall(r"[\d,]+", aria)
                if nums:
                    review_count = int(nums[0].replace(",", ""))
        except Exception:
            pass

        # Social handles from page links
        instagram_handle = None
        facebook_url = None
        try:
            ig_el = page.query_selector(sel.get("detail_instagram", "a[href*='instagram.com']"))
            if ig_el:
                ig_href = ig_el.get_attribute("href") or ""
                m = re.search(r"instagram\.com/([^/?]+)", ig_href)
                if m:
                    instagram_handle = m.group(1)
        except Exception:
            pass
        try:
            fb_el = page.query_selector(sel.get("detail_facebook", "a[href*='facebook.com']"))
            if fb_el:
                facebook_url = fb_el.get_attribute("href")
        except Exception:
            pass

        # Email — mailto: links in the Maps detail panel
        contact_email = None
        try:
            email_el = page.query_selector("a[href^='mailto:']")
            if email_el:
                href_val = email_el.get_attribute("href") or ""
                raw_email = href_val.replace("mailto:", "").split("?")[0].strip().lower()
                if raw_email and "@" in raw_email:
                    contact_email = raw_email
        except Exception:
            pass

        city, state = _parse_city_state(address or "")
        place_id = _extract_place_id(page.url, fallback_seed=f"{name}|{address}")

        return {
            "place_id": place_id,
            "name": name,
            "phone": phone or "",
            "website": website,
            "address": address,
            "category": category,
            "rating": rating,
            "review_count": review_count,
            "city": city,
            "state": state,
            "instagram_handle": instagram_handle,
            "facebook_url": facebook_url,
            "contact_email": contact_email,
            "maps_url": page.url,
        }

    except Exception as e:
        logger.error("detail_scrape_error", f"{href[:80]}: {type(e).__name__}: {str(e)[:120]}")
        return None


def _is_captcha(page) -> bool:
    try:
        body_text = page.inner_text("body").lower()
        return any(s in body_text for s in [
            "are you a robot", "unusual traffic", "recaptcha", "captcha"
        ])
    except Exception:
        return False


# ── MAIN ENGINE ────────────────────────────────────────────────────────────────

def run(city: str, state: str, max_per_query: int = 60) -> Path:
    from playwright.sync_api import sync_playwright

    niche = _load_niche()
    sel = _load_selectors()
    logger = EngineLogger("lead_engine")

    seen_ids = get_processed_place_ids()
    initial_seen = len(seen_ids)

    output_dir = SOURCES_DIR / "prospects"
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = now_iso()[:10]
    city_slug = slugify(city)
    output_path = output_dir / f"leads_{niche['niche']}_{city_slug}_{date_str}.jsonl"

    # Build search queries for this location
    queries = [
        q.format(city=city, state=state)
        for q in niche.get("search_queries", [f"{niche['display_name']} {city} {state}"])
    ]

    logger.start(input_path=f"{city}, {state}")
    logger.info(f"Niche: {niche['niche']} | Queries: {len(queries)} | Max per query: {max_per_query}")

    all_prospects: list[RawProspect] = []
    failed = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        ctx = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            timezone_id="America/New_York",
        )
        page = ctx.new_page()

        for query in queries:
            search_url = _build_search_url(query, sel)
            logger.info(f"Searching: {query}")

            try:
                page.goto(search_url, wait_until="domcontentloaded", timeout=25000)
                _human_delay(2.5, 4.0)
            except Exception as e:
                logger.error("navigate_failed", str(e)[:120])
                continue

            if _is_captcha(page):
                logger.error("captcha_detected", f"CAPTCHA on query: {query}")
                print("\n  [!] CAPTCHA detected. Solve it in the browser window, then press Enter to continue...")
                input()

            _scroll_feed(page, sel)
            hrefs = _collect_hrefs(page, sel)
            logger.info(f"Found {len(hrefs)} result links for: {query}")

            query_count = 0
            for href in hrefs[:max_per_query]:
                # Quick dedup: extract place_id from href before navigating
                pid_from_href = _extract_place_id(href)
                if pid_from_href != "hash_" + hashlib.md5(href.encode()).hexdigest()[:14]:
                    # Reliable ID extracted — check dedup before clicking
                    if pid_from_href in seen_ids:
                        logger.info(f"Skip duplicate (pre-nav): {pid_from_href[:20]}")
                        continue

                detail = _scrape_detail(page, href, sel, logger)
                if not detail:
                    failed += 1
                    continue

                place_id = detail["place_id"]
                if place_id in seen_ids:
                    logger.info(f"Skip duplicate: {detail['name']}")
                    continue

                if not detail.get("phone") and not detail.get("website"):
                    logger.info(f"Skip no-contact: {detail['name']}")
                    continue

                try:
                    prospect = RawProspect(
                        place_id=place_id,
                        company_name=detail["name"],
                        phone=detail["phone"],
                        website=detail.get("website"),
                        google_maps_url=detail["maps_url"],
                        city=detail.get("city", city),
                        state=detail.get("state", state),
                        address=detail.get("address"),
                        google_rating=detail.get("rating"),
                        review_count=detail.get("review_count"),
                        instagram_handle=detail.get("instagram_handle"),
                        facebook_url=detail.get("facebook_url"),
                        contact_email=detail.get("contact_email"),
                        scraped_at=now_iso(),
                        source_query=query,
                        niche=niche["niche"],
                    )
                    all_prospects.append(prospect)
                    seen_ids.add(place_id)
                    query_count += 1
                    logger.info(f"Scraped: {detail['name']} | {detail.get('city', '')}")
                except Exception as e:
                    logger.error("model_error", f"{detail['name']}: {e}")
                    failed += 1

                _human_delay(0.6, 1.4)

            logger.info(f"Query complete: {query_count} new leads from '{query}'")
            _human_delay(3.0, 6.0)  # Pause between queries

        browser.close()

    # Write JSONL output
    with output_path.open("w", encoding="utf-8") as f:
        for p in all_prospects:
            f.write(p.model_dump_json() + "\n")

    # Persist dedup manifest
    manifest = load_manifest()
    manifest["processed_place_ids"] = list(seen_ids)
    save_manifest(manifest)

    new_count = len(seen_ids) - initial_seen
    logger.finish(
        items_processed=new_count,
        items_failed=failed,
        output_path=str(output_path),
    )

    return output_path


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()

    if len(sys.argv) < 3:
        console.print("[red]Usage:[/red] python lead_engine.py <city> <state>")
        console.print("  Example: python lead_engine.py Boston MA")
        console.print("  Example: python lead_engine.py London UK")
        sys.exit(1)

    city_arg = " ".join(sys.argv[1:-1]) if len(sys.argv) > 3 else sys.argv[1]
    state_arg = sys.argv[-1]

    niche = _load_niche()

    console.print(f"\n[bold]Lead Engine — {city_arg}, {state_arg}[/bold]")
    console.print(f"  Niche:   [cyan]{niche['display_name']}[/cyan]")
    console.print(f"  Queries: {len(niche.get('search_queries', []))}")
    console.print(f"  Output:  sources/prospects/")
    console.print()
    console.print("  [dim]Browser will open. Do not close it.[/dim]")
    console.print("  [dim]If a CAPTCHA appears, solve it and press Enter in this terminal.[/dim]")
    console.print()

    output = run(city_arg, state_arg)

    count = sum(1 for line in output.open(encoding="utf-8") if line.strip())
    console.print(f"\n[bold green]Done.[/bold green] {count} leads -> [cyan]{output.name}[/cyan]")
    console.print(f"  Next: python research_engine.py --latest")
