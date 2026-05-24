"""
One-time migration: add ## Key Contacts wikilinks to all existing company notes
where owner_name is set in frontmatter but no Key Contacts section exists yet.

Run once: python scripts/migrate_contact_links.py
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from lib.utils import WIKI_DIR, slugify


def _parse_frontmatter(text: str) -> tuple[dict, str]:
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


def migrate():
    companies_dir = WIKI_DIR / "companies"
    if not companies_dir.exists():
        print("No companies/ dir found.")
        return

    files = list(companies_dir.glob("*.md"))
    updated = 0
    skipped_no_owner = 0
    skipped_already_linked = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(text)

        owner = fm.get("owner")
        if not owner or str(owner).strip().lower() in ("null", "none", ""):
            skipped_no_owner += 1
            continue

        owner_slug = slugify(str(owner))
        contact_link = f"[[{owner_slug}]]"

        if contact_link in body or "## Key Contacts" in body:
            skipped_already_linked += 1
            continue

        section = f"## Key Contacts\n- {contact_link}\n\n"
        if "## Objections Reference" in body:
            body = body.replace("## Objections Reference", section + "## Objections Reference", 1)
        elif "## Call History" in body:
            body = body.replace("## Call History", section + "## Call History", 1)
        else:
            body = section + body

        path.write_text(_render_frontmatter(fm, body), encoding="utf-8")
        updated += 1
        print(f"  + linked [[{owner_slug}]] in {path.name}")

    print(f"\nDone. Updated: {updated} | No owner: {skipped_no_owner} | Already linked: {skipped_already_linked}")


if __name__ == "__main__":
    migrate()
