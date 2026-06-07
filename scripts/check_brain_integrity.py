#!/usr/bin/env python3
"""
Brain integrity guard.

Scans every node in wiki/ and reports corruption BEFORE it spreads through
sync (the brain is shared across OS instances — one bad node propagates).

Standalone: depends only on PyYAML. Run it anytime, or before a brain push.

    python scripts/check_brain_integrity.py
    python scripts/check_brain_integrity.py --strict   # warnings also fail

Exit codes:
    0  clean (no errors; warnings allowed unless --strict)
    1  corruption found (ERROR-level), or --strict with warnings
"""
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

WIKI = Path(__file__).parent.parent / "wiki"

# Mirrors schemas.RELATIONSHIP_TYPES (kept inline so this guard stays standalone).
VALID_REL_TYPES = {
    "uses", "built", "knows", "works_at", "sells_to", "competes_with",
    "pain_signal", "identity_on", "part_of", "embodies", "reinforces",
    "opposes", "teaches", "mentioned_in",
    "relates_to", "informs", "extends", "targets",
    "used_by", "built_by", "known_by", "employs", "targeted_by",
    "competed_by", "has_pain", "hosted_at", "contains", "embodied_by",
    "reinforced_by", "opposed_by", "taught_by", "references",
    "informed_by", "extended_by",
}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

errors: list[str] = []
warnings: list[str] = []


def err(node: str, msg: str) -> None:
    errors.append(f"  [ERROR] {node}: {msg}")


def warn(node: str, msg: str) -> None:
    warnings.append(f"  [warn]  {node}: {msg}")


def parse_frontmatter(text: str):
    """Return (fm_dict_or_None, ok). ok=False means the block exists but is broken."""
    if not text.startswith("---"):
        return None, True  # no frontmatter — legal for prose-only nodes
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, False
    try:
        return (yaml.safe_load(parts[1]) or {}), True
    except yaml.YAMLError:
        return None, False


def valid_date(s) -> bool:
    if not isinstance(s, str) or not s:
        return False
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def check_relationship(node: str, rel, seen: set) -> None:
    if not isinstance(rel, dict):
        err(node, f"relationship is not a mapping: {rel!r}")
        return
    target = rel.get("target")
    rtype = rel.get("type")
    if not target:
        err(node, "relationship missing 'target'")
    if not rtype:
        err(node, "relationship missing 'type'")
    elif rtype not in VALID_REL_TYPES:
        err(node, f"unknown relationship type '{rtype}'")

    strength = rel.get("strength")
    if not isinstance(strength, int) or not (1 <= strength <= 10):
        err(node, f"strength out of range (1-10): {strength!r} -> {target}")

    if target and rtype:
        key = (target, rtype)
        if key in seen:
            warn(node, f"duplicate relationship {rtype} -> {target}")
        seen.add(key)

    for field in ("first_seen", "last_reinforced"):
        if field in rel and not valid_date(rel[field]):
            warn(node, f"{field} not YYYY-MM-DD: {rel.get(field)!r} ({target})")


def main() -> int:
    strict = "--strict" in sys.argv
    if not WIKI.exists():
        print(f"No wiki/ directory at {WIKI}")
        return 1

    md_files = sorted(WIKI.rglob("*.md"))
    known_slugs = {p.stem for p in md_files}
    checked = 0

    for path in md_files:
        node = path.relative_to(WIKI).as_posix()
        checked += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as e:
            err(node, f"cannot read file: {e}")
            continue

        fm, ok = parse_frontmatter(text)
        if not ok:
            err(node, "frontmatter block present but YAML is broken (corruption)")
            continue
        if fm is None:
            continue  # prose-only node, nothing more to check

        rels = fm.get("relationships")
        if rels is not None:
            if not isinstance(rels, list):
                err(node, f"'relationships' is not a list: {type(rels).__name__}")
            else:
                seen: set = set()
                for rel in rels:
                    check_relationship(node, rel, seen)

        # Broken wikilinks — warn only (Obsidian tolerates dangling links).
        for link in WIKILINK_RE.findall(text):
            slug = link.split("|")[0].split("#")[0].strip()
            if slug and slug not in known_slugs:
                warn(node, f"wikilink [[{slug}]] has no matching node file")

    print(f"Scanned {checked} nodes in {WIKI}")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        print("\n".join(warnings))
    if errors:
        print(f"\n{len(errors)} ERROR(s) — brain integrity compromised:")
        print("\n".join(errors))
        return 1
    if strict and warnings:
        print("\n--strict: warnings treated as failure.")
        return 1
    print("\nBrain integrity OK." if not warnings else "\nNo corruption (warnings only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
