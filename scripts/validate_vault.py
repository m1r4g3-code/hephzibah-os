"""
Validates wiki/ against the node schema every Claude session is supposed to follow
by convention (CLAUDE.md templates, lib/schemas.py) but that nothing previously
checked mechanically.

Checks per file:
  - sensitivity present and one of public/private/sensitive (ERROR if invalid,
    WARNING if missing - push_public.py already fails closed to "private" on
    missing/malformed sensitivity, so a missing tag is a hygiene issue, not a
    leak risk; a WRONG tag is not something either script can catch)
  - a node living under a private-by-nature path (outreach/contacts, companies,
    coaching, me/) marked sensitivity:public - WARNING, likely a mistake
  - entity_type, if present, is one of ENTITY_TYPES (ERROR if not)
  - relationships[].type, if present, is one of RELATIONSHIP_TYPES (ERROR if not)
  - relationships[].target resolves to a real file somewhere in wiki/ (ERROR if not)
  - every [[wikilink]] in the body resolves to a real file somewhere in wiki/
    (ERROR if not - this is the broken-graph-edge check)

Usage:
  python scripts/validate_vault.py            # human report
  python scripts/validate_vault.py --json      # machine-readable, for CI/hooks

Exit code 1 if any ERROR-level finding exists, 0 otherwise. Never touches
sensitive content itself - reads structure only.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

from lib.utils import VAULT_ROOT, parse_frontmatter
from lib.schemas import ENTITY_TYPES, RELATIONSHIP_TYPES

WIKI_ROOT = VAULT_ROOT / "wiki"
VALID_SENSITIVITY = {"public", "private", "sensitive"}
VALID_ENTITY_TYPES = set(ENTITY_TYPES.__args__)
VALID_RELATIONSHIP_TYPES = set(RELATIONSHIP_TYPES.__args__)

# Paths where content is inherently private-ish - public here is almost always a mistake.
# Deliberately narrow: me/platforms/* is legitimately public-facing, so "me/" as a
# blanket prefix produced false positives - only flag the specific sensitive files.
LIKELY_PRIVATE_PREFIXES = (
    "outreach/contacts", "outreach/companies", "outreach/coaching",
    "me/identity.md", "me/goals.md",
)

# Root-level files (outside wiki/) that are legitimately linkable - ME.md is
# CLAUDE.md's documented operator profile, not a wiki node, but [[me]] is a real link.
EXTRA_LINKABLE_ROOT_FILES = ("ME.md",)

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def find_all_files() -> list[Path]:
    return sorted(WIKI_ROOT.rglob("*.md"))


def build_slug_index(files: list[Path]) -> dict[str, Path]:
    """Map every resolvable name -> file. A node resolves by filename stem
    (matches how _resolve_wiki_path / Obsidian actually resolve links)."""
    index: dict[str, Path] = {}
    for f in files:
        index[f.stem.lower()] = f
    for name in EXTRA_LINKABLE_ROOT_FILES:
        p = VAULT_ROOT / name
        if p.exists():
            index[p.stem.lower()] = p
    return index


def strip_link_target(raw: str) -> str:
    return raw.strip().strip("[]")


def validate_file(path: Path, slug_index: dict[str, Path]) -> list[dict]:
    findings: list[dict] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    rel_path = path.relative_to(WIKI_ROOT).as_posix()

    def add(level: str, msg: str):
        findings.append({"file": rel_path, "level": level, "message": msg})

    # sensitivity
    sensitivity = fm.get("sensitivity")
    if sensitivity is None:
        add("WARNING", "missing sensitivity field (push_public.py defaults this to 'private' - safe, but should be explicit)")
    elif sensitivity not in VALID_SENSITIVITY:
        add("ERROR", f"invalid sensitivity value {sensitivity!r} - must be one of {sorted(VALID_SENSITIVITY)}")
    elif sensitivity == "public" and rel_path.startswith(LIKELY_PRIVATE_PREFIXES):
        add("WARNING", f"sensitivity:public on a path that's normally private-ish ({rel_path}) - double-check this is intentional")

    # entity_type
    entity_type = fm.get("entity_type")
    if entity_type is not None and entity_type not in VALID_ENTITY_TYPES:
        add("ERROR", f"invalid entity_type {entity_type!r} - must be one of {sorted(VALID_ENTITY_TYPES)}")

    # relationships
    for i, rel in enumerate(fm.get("relationships") or []):
        if not isinstance(rel, dict):
            add("ERROR", f"relationships[{i}] is not a mapping")
            continue
        rtype = rel.get("type")
        if rtype and rtype not in VALID_RELATIONSHIP_TYPES:
            add("ERROR", f"relationships[{i}] invalid type {rtype!r} - must be one of {sorted(VALID_RELATIONSHIP_TYPES)}")
        target = rel.get("target")
        if target:
            target_slug = strip_link_target(target).lower()
            if target_slug not in slug_index:
                add("ERROR", f"relationships[{i}] target [[{target_slug}]] does not resolve to any file in wiki/")

    # body wikilinks — skip underscore-prefixed meta/index files (_CONTEXT.md etc.),
    # which document the wikilink syntax itself using illustrative, non-real examples
    if path.stem.startswith("_"):
        return findings

    for match in WIKILINK_RE.finditer(body):
        target_slug = strip_link_target(match.group(1)).lower()
        if target_slug not in slug_index:
            add("ERROR", f"broken wikilink [[{target_slug}]] in body - no matching file in wiki/")

    return findings


def main():
    as_json = "--json" in sys.argv
    files = find_all_files()
    slug_index = build_slug_index(files)

    all_findings: list[dict] = []
    for f in files:
        all_findings.extend(validate_file(f, slug_index))

    errors = [f for f in all_findings if f["level"] == "ERROR"]
    warnings = [f for f in all_findings if f["level"] == "WARNING"]

    if as_json:
        print(json.dumps({
            "files_scanned": len(files),
            "errors": errors,
            "warnings": warnings,
        }, indent=2))
    else:
        print(f"Scanned {len(files)} wiki nodes\n")
        if errors:
            print(f"ERRORS ({len(errors)}):")
            for e in errors:
                print(f"  [{e['file']}] {e['message']}")
            print()
        if warnings:
            print(f"WARNINGS ({len(warnings)}):")
            for w in warnings:
                print(f"  [{w['file']}] {w['message']}")
            print()
        if not errors and not warnings:
            print("Clean - no schema or link issues found.")
        else:
            print(f"{len(errors)} error(s), {len(warnings)} warning(s).")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
