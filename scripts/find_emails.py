"""
Quick email finder — visits each B-tier company website,
scrapes homepage + /contact page for real mailto: links.
Prints what it finds. No guessing.
"""

import re
import sys
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).parent))

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 8

TARGETS = [
    ("Austin Medical Associates",    "http://www.austinmedicalassociates.com/"),
    ("Austin Medical Partners",      "http://www.austinmedicalpartners.com/"),
    ("Balcones Psychiatry",          "https://www.balconespsych.com/"),
    ("Capital Medical Clinic",       "http://www.capitalmedicalclinic.com/"),
    ("Clinic Concierge Austin",      "https://clinicconcierge.com/"),
    ("Family Medicine Austin",       "https://familymedicineaustin.com/"),
    ("Family Medicine Practice",     "http://www.keithlamymd.com/"),
    ("Hope Medical Clinic",          "http://www.hopeclinicaustin.org/"),
    ("Red River Family Practice",    "https://www.redriverfamilypractice.com/"),
    ("RiverRock Medical Clinic",     "https://riverrockmedical.com/"),
    ("Teddy Bear Pediatrics",        "https://teddybearpediatrics.com/"),
    ("Texas Direct Medical Care",    "http://txmedicalcare.com/"),
    ("Volunteer Healthcare Clinic",  "http://www.volclinic.org/"),
    ("Xenia Kempf",                  "https://yourfunctionalmednp.com/"),
]

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

def get_emails_from_url(url: str) -> set[str]:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        soup = BeautifulSoup(r.text, "html.parser")

        found = set()

        # mailto: links
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("mailto:"):
                email = href.replace("mailto:", "").split("?")[0].strip().lower()
                if email and "@" in email:
                    found.add(email)

        # text patterns (obfuscated emails sometimes)
        text = soup.get_text()
        for match in EMAIL_RE.findall(text):
            m = match.lower()
            # filter out common false positives
            if any(skip in m for skip in ["example.com", "yourdomain", "sentry.io",
                                           "@2x", ".png", ".jpg", ".svg", "wix.com",
                                           "squarespace.com", "wordpress.com"]):
                continue
            found.add(m)

        return found
    except Exception as e:
        return set()


def find_contact_page(base_url: str) -> str | None:
    """Try common contact page paths."""
    paths = ["/contact", "/contact-us", "/contact.html", "/about/contact"]
    for path in paths:
        url = urljoin(base_url, path)
        try:
            r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code == 200 and len(r.text) > 200:
                return url
        except Exception:
            continue
    return None


def main():
    print(f"\n{'='*60}")
    print("Email Finder — B-tier medical practices")
    print(f"{'='*60}\n")

    results = []

    for name, website in TARGETS:
        print(f"  Checking: {name}")
        all_emails = set()

        # Check homepage
        home_emails = get_emails_from_url(website)
        all_emails.update(home_emails)

        # Check contact page if homepage found nothing
        if not home_emails:
            contact_url = find_contact_page(website)
            if contact_url:
                contact_emails = get_emails_from_url(contact_url)
                all_emails.update(contact_emails)

        if all_emails:
            for email in sorted(all_emails):
                print(f"    FOUND: {email}")
        else:
            print(f"    NONE — use contact form or call first")

        results.append((name, website, sorted(all_emails)))
        time.sleep(0.8)

    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    found_count = sum(1 for _, _, emails in results if emails)
    print(f"  Found real emails: {found_count}/{len(results)}")
    print(f"  No email found:    {len(results) - found_count}/{len(results)} — contact form or call first\n")

    return results


if __name__ == "__main__":
    main()
