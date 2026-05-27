"""
One-time migration: add sensitivity: public|private|sensitive to all wiki nodes.
Run from repo root: python scripts/migrate_sensitivity.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"

# Path-based sensitivity rules (evaluated in order, first match wins)
def classify(path: Path) -> str:
    rel = path.relative_to(WIKI).as_posix()

    # Sensitive — contains personal/financial data or inner circle
    if rel in (
        "me/identity.md",
        "me/goals.md",
        "outreach/contacts/cyrus.md",
        "outreach/contacts/oba.md",
        "outreach/contacts/yemi.md",
        "outreach/contacts/jennifer-labonte.md",
    ):
        return "sensitive"
    if rel.startswith("outreach/coaching/"):
        return "sensitive"

    # Private — sales intel, prospect data, personal strategy
    if rel.startswith("outreach/companies/"):
        return "private"
    if rel.startswith("outreach/contacts/"):
        return "private"
    if rel.startswith("outreach/examples/"):
        return "private"
    if rel.startswith("outreach/objections/"):
        return "private"
    if rel.startswith("outreach/scripts/"):
        return "private"
    if rel in ("me/brand.md", "me/startup.md", "me/goals.md"):
        return "private"
    if rel.startswith("clients/"):
        return "private"
    if rel.startswith("pipeline/"):
        return "private"

    # Public — concepts, tools, platforms, methodology, index files
    return "public"


def add_sensitivity(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    sensitivity = classify(path)

    if "sensitivity:" in text:
        # Already has it — skip
        return "skip"

    if text.startswith("---"):
        # Has frontmatter — inject after opening ---
        rest = text[3:]
        closing = rest.find("---")
        if closing == -1:
            return "skip"
        front = rest[:closing]
        after = rest[closing:]
        new_text = f"---\nsensitivity: {sensitivity}\n{front}{after}"
    else:
        # No frontmatter — add minimal header
        new_text = f"---\nsensitivity: {sensitivity}\n---\n\n{text}"

    path.write_text(new_text, encoding="utf-8")
    return sensitivity


def main():
    files = list(WIKI.rglob("*.md"))
    counts = {"public": 0, "private": 0, "sensitive": 0, "skip": 0}

    for f in sorted(files):
        result = add_sensitivity(f)
        counts[result] = counts.get(result, 0) + 1
        if result != "skip":
            rel = f.relative_to(WIKI)
            print(f"  [{result:9s}] {rel}")

    print(f"\nDone: {counts['public']} public, {counts['private']} private, {counts['sensitive']} sensitive, {counts['skip']} already set")


if __name__ == "__main__":
    main()
