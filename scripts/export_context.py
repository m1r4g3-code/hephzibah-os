"""
Export portable brain state from wiki/me/ + wiki/concepts/ + ME.md.
Regenerates context/os_context.md and context/system_prompt.txt.

Run: python scripts/export_context.py
"""

import sys
import re
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

VAULT_ROOT = Path(__file__).parent.parent
WIKI_ME = VAULT_ROOT / "wiki" / "me"
WIKI_CONCEPTS = VAULT_ROOT / "wiki" / "concepts"
ME_MD = VAULT_ROOT / "ME.md"
CONTEXT_DIR = VAULT_ROOT / "context"
CONTEXT_DIR.mkdir(exist_ok=True)


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].strip()
    return text.strip()


def read_file(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def extract_section(text: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""


def load_concepts() -> list[dict]:
    concepts = []
    for f in sorted(WIKI_CONCEPTS.glob("*.md")):
        raw = read_file(f)
        body = strip_frontmatter(raw)
        # First paragraph before "**Appears in:**" is the definition
        lines = body.split("\n")
        definition_lines = []
        for line in lines:
            if line.startswith("**Appears in:**"):
                break
            definition_lines.append(line)
        definition = " ".join(" ".join(definition_lines).split())
        concepts.append({
            "name": f.stem,
            "definition": definition,
        })
    return concepts


def build_os_context(identity: str, brand: str, goals: str, me: str, concepts: list[dict]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")

    concept_block = "\n\n".join(
        f"**{c['name']}** — {c['definition']}" for c in concepts
    )

    # Extract key sections
    offer_section = extract_section(me, "Offer") or extract_section(brand, "Positioning")
    voice_section = extract_section(me, "Voice & Style") or extract_section(brand, "Voice")
    nonneg_section = extract_section(me, "Non-Negotiables")
    weakness_section = extract_section(me, "Known Weaknesses to Watch") or extract_section(brand, "Real Weaknesses")

    return f"""---
type: shared-brain-state
generated_from: wiki/me/ + wiki/concepts/ + ME.md
last_updated: {today}
version: 1
---

# Operator Brain State — Hephzibah Ifeoluwa (Emmanuel Adekoya)

> Portable shared memory for this operator's AI OS.
> Load in any Claude Code project, AI system prompt, or agent to carry full context.
> Regenerate with: `python scripts/export_context.py`

---

## Identity

**Name:** Hephzibah Ifeoluwa (goes by Emmanuel Adekoya / cipher: mirage / GitHub: m1r4g3-code)
**Age:** 20 | **Location:** Lagos, Nigeria
**Faith:** Born-again Christian. Holy Ghost filled. Foundation, not label.

{strip_frontmatter(identity)}

---

## Offer & Positioning

{offer_section}

---

## Voice & Communication Style

{voice_section}

---

## Non-Negotiables

{nonneg_section}

---

## Known Patterns to Watch

{weakness_section}

---

## Current Goals (2026)

{strip_frontmatter(goals)}

---

## Concept Network (Compressed)

These atomic concepts wire together identity, sales approach, and outreach system.
Reference by name when relevant.

{concept_block}

---

## How to Use This File in Another Project

Add to the other project's `CLAUDE.md`:

```
## Shared Operator Context
Load the full operator brain state from:
C:\\Users\\HomePC\\Documents\\Cold Outreach Brain\\context\\os_context.md

Read this file at the start of any session involving operator identity,
coaching, personalization, or cross-domain reasoning.
```

Or paste `context/system_prompt.txt` as the system prompt in any AI interface.
"""


def build_system_prompt(identity: str, me: str, concepts: list[dict]) -> str:
    name_line = "Hephzibah Ifeoluwa (goes by Emmanuel Adekoya, cipher: mirage)"
    offer = extract_section(me, "Offer") or ""
    voice = extract_section(me, "Voice & Style") or ""
    nonneg = extract_section(me, "Non-Negotiables") or ""
    weaknesses = extract_section(me, "Known Weaknesses to Watch") or ""

    concept_lines = "\n".join(
        f"- {c['name']}: {c['definition'][:120]}..." if len(c['definition']) > 120 else f"- {c['name']}: {c['definition']}"
        for c in concepts
    )

    return f"""You are working with {name_line}.
Age 20, Lagos, Nigeria. Born-again Christian. Everything runs on that foundation.

OFFER:
{offer.strip()}

VOICE:
{voice.strip()}

NON-NEGOTIABLES:
{nonneg.strip()}

KNOWN PATTERNS TO WATCH:
{weaknesses.strip()}

KEY CONCEPTS:
{concept_lines}

Email signature: Emmanuel
"""


def main():
    print("Exporting brain state to context/...")

    identity_raw = read_file(WIKI_ME / "identity.md")
    brand_raw = read_file(WIKI_ME / "brand.md")
    goals_raw = read_file(WIKI_ME / "goals.md")
    me_raw = read_file(ME_MD)
    concepts = load_concepts()

    print(f"  Loaded: identity, brand, goals, ME.md, {len(concepts)} concepts")

    os_context = build_os_context(identity_raw, brand_raw, goals_raw, me_raw, concepts)
    system_prompt = build_system_prompt(identity_raw, me_raw, concepts)

    (CONTEXT_DIR / "os_context.md").write_text(os_context, encoding="utf-8")
    (CONTEXT_DIR / "system_prompt.txt").write_text(system_prompt, encoding="utf-8")

    print("  Written: context/os_context.md")
    print("  Written: context/system_prompt.txt")
    print()
    print("To use in another project, add to its CLAUDE.md:")
    print(f"  Read C:\\Users\\HomePC\\Documents\\Cold Outreach Brain\\context\\os_context.md")
    print()
    print("To use in any AI chat, paste context/system_prompt.txt as the system prompt.")


if __name__ == "__main__":
    main()
