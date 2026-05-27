"""
One-time migration: upgrade all existing wiki nodes to the entity schema.

For each .md file in wiki/:
  1. Infer entity_type from folder location
  2. Parse existing [[wikilinks]] from body
  3. Add entity_type, name, aliases to frontmatter (additive — never overwrites)
  4. Convert wikilinks to relationships[] with type=mentioned_in, strength=1
  5. Write back

Run: python scripts/migrate_to_graph.py
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import yaml
from lib.utils import VAULT_ROOT, today_iso

WIKI_ROOT = VAULT_ROOT / "wiki"

FOLDER_ENTITY_TYPE = {
    "outreach/companies": "company",
    "outreach/contacts": "person",
    "outreach/examples": "person",
    "outreach/coaching": "domain",
    "outreach/scripts": "domain",
    "outreach/objections": "domain",
    "concepts": "concept",
    "me": "person",
    "me/platforms": "platform",
    "clients": "company",
    "startup": "domain",
    "learning": "domain",
    "content": "domain",
    "disciplines": "domain",
    "daily": "domain",
}

ME_FILES = {
    "identity": ("person", "Emmanuel Adekoya Hephzibah Ifeoluwa"),
    "brand": ("domain", "Brand Identity"),
    "goals": ("domain", "Goals"),
    "startup": ("domain", "Startup Vision"),
}

PLATFORM_FILES = {
    "github": ("platform", "GitHub"),
    "contra": ("platform", "Contra"),
    "linkedin": ("platform", "LinkedIn"),
}


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


def _extract_wikilinks(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]", text)


def _infer_entity_type(rel_path: str, stem: str) -> tuple[str, str]:
    """Return (entity_type, display_name) for a given wiki file."""
    parts = rel_path.replace("\\", "/")

    if parts.startswith("me/platforms/"):
        info = PLATFORM_FILES.get(stem)
        return info if info else ("platform", stem.title())

    if parts.startswith("me/"):
        info = ME_FILES.get(stem)
        return info if info else ("domain", stem.replace("-", " ").title())

    for prefix, etype in FOLDER_ENTITY_TYPE.items():
        if parts.startswith(prefix + "/") or parts == prefix:
            return etype, stem.replace("-", " ").title()

    return "concept", stem.replace("-", " ").title()


def migrate_file(path: Path) -> bool:
    """Migrate a single wiki file. Returns True if changed."""
    rel = path.relative_to(WIKI_ROOT)
    subpath = str(rel.parent).replace("\\", "/")
    stem = path.stem

    if stem in ("README", "_index", "playbook", "master_script", "pattern_log", "latest_roast"):
        return False

    text = path.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)

    entity_type, display_name = _infer_entity_type(str(rel), stem)

    changed = False

    if "entity_type" not in fm:
        fm["entity_type"] = entity_type
        changed = True

    if "name" not in fm:
        existing_name = fm.get("company") or fm.get("name") or display_name
        fm["name"] = existing_name
        changed = True

    if "aliases" not in fm:
        fm["aliases"] = []
        changed = True

    # Convert existing [[wikilinks]] in body to relationships[]
    links = _extract_wikilinks(body)
    if links:
        existing_rels: list[dict] = fm.get("relationships") or []
        existing_targets = {r["target"] for r in existing_rels}

        for link in set(links):
            target = f"[[{link}]]"
            if target not in existing_targets:
                existing_rels.append({
                    "target": target,
                    "type": "mentioned_in",
                    "strength": 1,
                    "first_seen": today_iso(),
                    "last_reinforced": today_iso(),
                })
                existing_targets.add(target)
                changed = True

        if changed:
            fm["relationships"] = existing_rels

    if not changed:
        return False

    path.write_text(_render_frontmatter(fm, body), encoding="utf-8")
    return True


def main():
    md_files = [p for p in WIKI_ROOT.rglob("*.md") if p.name != "README.md"]
    total = len(md_files)
    updated = 0

    print(f"Migrating {total} wiki nodes to entity schema...")

    for path in sorted(md_files):
        rel = path.relative_to(WIKI_ROOT)
        if migrate_file(path):
            print(f"  + {rel}")
            updated += 1
        else:
            print(f"  . {rel} (skipped)")

    print(f"\nDone. {updated}/{total} nodes upgraded.")
    print("Open Obsidian graph view to see the new connections.")


if __name__ == "__main__":
    main()
