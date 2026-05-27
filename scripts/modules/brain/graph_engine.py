"""
Brain graph engine — extracts entities and typed relationships from any text,
then wires them into the wiki as a growing knowledge graph.

Entry points:
  process_text(text)          — extract from any raw text
  process_conversation(text)  — optimized for call/chat transcripts
  enrich_node(slug)           — re-process all wiki sources for a given node
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from anthropic import Anthropic
from lib.utils import VAULT_ROOT, slugify, today_iso
from lib.vault import write_entity_relationships
from lib.schemas import Relationship

client = Anthropic()

WIKI_ROOT = VAULT_ROOT / "wiki"

RELATIONSHIP_VOCAB = [
    "uses", "built", "knows", "works_at", "sells_to", "competes_with",
    "pain_signal", "identity_on", "part_of", "embodies", "reinforces",
    "opposes", "teaches", "mentioned_in",
]

ENTITY_TYPES = ["person", "company", "tool", "concept", "platform", "skill", "place", "domain"]

# Map folder paths to default entity_type
FOLDER_ENTITY_TYPE = {
    "outreach/companies": "company",
    "outreach/contacts": "person",
    "outreach/examples": "person",
    "concepts": "concept",
    "me": "person",
    "me/platforms": "platform",
    "clients": "company",
    "startup": "domain",
    "learning": "domain",
    "content": "domain",
    "disciplines": "domain",
}


def _get_existing_nodes() -> dict[str, dict]:
    """Return {slug: {entity_type, name, wiki_subpath}} for all nodes in wiki/."""
    nodes = {}
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        slug = md_file.stem
        rel = md_file.relative_to(WIKI_ROOT)
        subpath = str(rel.parent).replace("\\", "/")
        entity_type = FOLDER_ENTITY_TYPE.get(subpath, "concept")
        nodes[slug] = {"entity_type": entity_type, "wiki_subpath": subpath, "name": slug.replace("-", " ").title()}
    return nodes


def _extract_graph(text: str, existing_nodes: dict, mode: str = "general") -> dict:
    """Call Claude to extract entities and relationships from text."""
    node_list = "\n".join(f"- {slug} ({v['entity_type']})" for slug, v in list(existing_nodes.items())[:120])

    mode_hint = (
        "This is a sales call transcript. Focus on: company names, contact names, pain points, tools they use, objections, and outcomes."
        if mode == "conversation"
        else "This is general text. Extract all named entities and their relationships."
    )

    prompt = f"""You are a knowledge graph extraction engine for a personal AI OS brain.

{mode_hint}

EXISTING BRAIN NODES (slug — entity_type):
{node_list}

RELATIONSHIP TYPES (use only these):
{", ".join(RELATIONSHIP_VOCAB)}

ENTITY TYPES (use only these):
{", ".join(ENTITY_TYPES)}

TEXT TO ANALYZE:
{text[:6000]}

Extract ALL entities and relationships. For entities already in the brain, enrich them.
For new entities, create them.

Return ONLY valid JSON in this exact format:
{{
  "entities": [
    {{"slug": "node-slug", "entity_type": "person|company|tool|concept|platform|skill|place|domain", "name": "Display Name", "aliases": [], "is_new": true|false}}
  ],
  "relationships": [
    {{"from_slug": "source-slug", "to_slug": "target-slug", "type": "relationship_type", "strength": 1}}
  ]
}}

Rules:
- slugs must be lowercase-hyphenated (e.g. "emmanuel-adekoya", "n8n", "balcones-psychiatry")
- Only use relationship types from the list above
- strength 1-3 for inferred/weak, 4-6 for confirmed, 7-10 for core/defining
- For call transcripts: extract company→pain_signal, contact→works_at→company, caller→sells_to→company
- Always include the operator node "emmanuel-adekoya" as from_slug when the text is about them
- Return only the JSON, no explanation"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def _write_graph_result(result: dict, existing_nodes: dict) -> list[str]:
    """Write extracted entities and relationships to wiki/."""
    written = []

    # Index new entities so we can look them up when writing relationships
    entity_index: dict[str, dict] = dict(existing_nodes)
    for ent in result.get("entities", []):
        slug = ent.get("slug", "")
        if not slug:
            continue
        if slug not in entity_index:
            # Determine wiki subpath from entity_type
            type_to_subpath = {
                "company": "outreach/companies",
                "person": "outreach/contacts",
                "tool": "concepts",
                "concept": "concepts",
                "platform": "concepts",
                "skill": "concepts",
                "place": "concepts",
                "domain": "concepts",
            }
            subpath = type_to_subpath.get(ent.get("entity_type", "concept"), "concepts")
            entity_index[slug] = {
                "entity_type": ent.get("entity_type", "concept"),
                "wiki_subpath": subpath,
                "name": ent.get("name", slug.replace("-", " ").title()),
            }

    # Group relationships by from_slug
    from_map: dict[str, list[dict]] = {}
    for rel in result.get("relationships", []):
        fs = rel.get("from_slug", "")
        if fs:
            from_map.setdefault(fs, []).append(rel)

    # Write each entity's relationships
    for from_slug, rels in from_map.items():
        info = entity_index.get(from_slug)
        if not info:
            continue
        relationships = []
        for rel in rels:
            to_slug = rel.get("to_slug", "")
            if not to_slug:
                continue
            relationships.append(Relationship(
                target=f"[[{to_slug}]]",
                type=rel.get("type", "mentioned_in"),
                strength=min(10, max(1, rel.get("strength", 1))),
                first_seen=today_iso(),
                last_reinforced=today_iso(),
            ))
        if not relationships:
            continue
        path = write_entity_relationships(
            slug=from_slug,
            wiki_subpath=info["wiki_subpath"],
            entity_type=info["entity_type"],
            name=info["name"],
            new_relationships=relationships,
        )
        written.append(str(path))

    return written


def process_text(text: str) -> list[str]:
    """Extract entities and relationships from any raw text. Returns list of written paths."""
    if not text.strip():
        return []
    existing = _get_existing_nodes()
    result = _extract_graph(text, existing, mode="general")
    return _write_graph_result(result, existing)


def process_conversation(text: str) -> list[str]:
    """Optimized for call transcripts and conversation logs."""
    if not text.strip():
        return []
    existing = _get_existing_nodes()
    result = _extract_graph(text, existing, mode="conversation")
    return _write_graph_result(result, existing)


def enrich_node(slug: str) -> list[str]:
    """
    Re-process all wiki sources that mention this slug to enrich its relationships.
    Scans every wiki file for [[slug]] mentions and re-extracts context.
    """
    written = []
    existing = _get_existing_nodes()
    for md_file in WIKI_ROOT.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if f"[[{slug}]]" in content or slug in content:
            result = _extract_graph(content, existing, mode="general")
            written.extend(_write_graph_result(result, existing))
    return list(set(written))


if __name__ == "__main__":
    # Quick test: pipe text via stdin or pass as arg
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read()

    print("Processing text through graph engine...")
    written = process_text(text)
    print(f"Written/updated {len(written)} nodes:")
    for p in written:
        print(f"  {p}")
