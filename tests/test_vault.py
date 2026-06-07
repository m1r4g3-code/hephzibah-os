"""
Data-integrity tests for the only writer to the brain (lib/vault.py).

These guard the guarantees that, if broken, silently corrupt or lose memory:
  - frontmatter parse/render is lossless round-trip
  - malformed input never crashes the parser
  - atomic writes never leave a partial file or a stray .tmp on failure
  - relationship merges increment, never duplicate, never drop existing edges
  - bidirectional inverses are written to the target node
"""
import os
from pathlib import Path

import pytest

from lib import vault


# ── FRONTMATTER ROUND-TRIP ────────────────────────────────────────────────────

def test_frontmatter_roundtrip_preserves_data():
    fm = {
        "entity_type": "person",
        "name": "Cyrus",
        "aliases": ["cypher125"],
        "relationships": [
            {"target": "[[identity]]", "type": "known_by", "strength": 10,
             "first_seen": "2026-05-27", "last_reinforced": "2026-06-07"},
        ],
    }
    body = "# Cyrus\n\nInner circle. Blood brother.\n"
    rendered = vault._render_frontmatter(fm, body)
    parsed_fm, parsed_body = vault._parse_frontmatter(rendered)
    assert parsed_fm == fm
    assert parsed_body == body


def test_frontmatter_roundtrip_unicode():
    fm = {"name": "Adékóyá — Hephzibah", "note": "naira ₦125k"}
    body = "Body with arrow -> and unicode ★ ₦.\n"
    rendered = vault._render_frontmatter(fm, body)
    parsed_fm, parsed_body = vault._parse_frontmatter(rendered)
    assert parsed_fm == fm
    assert parsed_body == body


def test_parse_no_frontmatter_returns_empty_dict():
    text = "# Just a body\n\nNo frontmatter here.\n"
    fm, body = vault._parse_frontmatter(text)
    assert fm == {}
    assert body == text


def test_parse_malformed_yaml_never_crashes():
    # Broken YAML in the frontmatter block must NOT raise — it degrades to ({}, text).
    text = "---\nname: : : [unbalanced\n  bad indent\n---\n\nbody\n"
    fm, body = vault._parse_frontmatter(text)
    assert fm == {}
    assert body == text  # original returned untouched, nothing lost


def test_parse_empty_frontmatter_block():
    text = "---\n---\n\nbody\n"
    fm, body = vault._parse_frontmatter(text)
    assert fm == {}
    assert body == "body\n"


# ── ATOMIC WRITE ──────────────────────────────────────────────────────────────

def test_atomic_write_creates_file(tmp_path):
    target = tmp_path / "sub" / "node.md"
    vault._atomic_write(target, "hello brain\n")
    assert target.read_text(encoding="utf-8") == "hello brain\n"


def test_atomic_write_overwrites_existing(tmp_path):
    target = tmp_path / "node.md"
    vault._atomic_write(target, "v1")
    vault._atomic_write(target, "v2")
    assert target.read_text(encoding="utf-8") == "v2"


def test_atomic_write_leaves_no_tmp_on_success(tmp_path):
    target = tmp_path / "node.md"
    vault._atomic_write(target, "content")
    leftovers = [p for p in tmp_path.iterdir() if p.suffix == ".tmp"]
    assert leftovers == []


def test_atomic_write_failure_preserves_original_and_cleans_tmp(tmp_path):
    target = tmp_path / "node.md"
    vault._atomic_write(target, "original safe content")

    # Non-str content makes f.write() raise mid-write — exercises the rollback path.
    with pytest.raises(TypeError):
        vault._atomic_write(target, 12345)  # type: ignore[arg-type]

    # Original must be intact (never truncated/corrupted)...
    assert target.read_text(encoding="utf-8") == "original safe content"
    # ...and no half-written temp file left behind.
    leftovers = [p for p in tmp_path.iterdir() if p.suffix == ".tmp"]
    assert leftovers == []


# ── RELATIONSHIP MERGE (the knowledge-graph integrity core) ───────────────────

@pytest.fixture
def brain(tmp_path, monkeypatch):
    """Point vault at a throwaway VAULT_ROOT so tests never touch the real wiki/."""
    monkeypatch.setattr(vault, "VAULT_ROOT", tmp_path)
    (tmp_path / "wiki").mkdir()
    return tmp_path


def _rel(target, type_, strength=5):
    return vault.Relationship(target=target, type=type_, strength=strength,
                              first_seen="2026-06-08", last_reinforced="2026-06-08")


def _read_fm(path: Path) -> dict:
    fm, _ = vault._parse_frontmatter(path.read_text(encoding="utf-8"))
    return fm


def test_new_relationship_creates_node(brain):
    path = vault.write_entity_relationships(
        slug="emmanuel", wiki_subpath="me", entity_type="person",
        name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses")],
    )
    fm = _read_fm(path)
    assert fm["entity_type"] == "person"
    assert fm["name"] == "Emmanuel"
    assert len(fm["relationships"]) == 1
    assert fm["relationships"][0]["target"] == "[[n8n]]"
    assert fm["relationships"][0]["type"] == "uses"


def test_repeated_relationship_increments_strength_not_duplicates(brain):
    for _ in range(3):
        vault.write_entity_relationships(
            slug="emmanuel", wiki_subpath="me", entity_type="person",
            name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses", strength=5)],
        )
    fm = _read_fm(brain / "wiki" / "me" / "emmanuel.md")
    rels = [r for r in fm["relationships"] if r["target"] == "[[n8n]]" and r["type"] == "uses"]
    assert len(rels) == 1                 # never duplicated
    assert rels[0]["strength"] == 7       # 5, then +1, +1


def test_strength_capped_at_10(brain):
    for _ in range(20):
        vault.write_entity_relationships(
            slug="emmanuel", wiki_subpath="me", entity_type="person",
            name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses", strength=9)],
        )
    fm = _read_fm(brain / "wiki" / "me" / "emmanuel.md")
    assert fm["relationships"][0]["strength"] == 10


def test_existing_relationships_never_dropped(brain):
    vault.write_entity_relationships(
        slug="emmanuel", wiki_subpath="me", entity_type="person",
        name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses")],
    )
    vault.write_entity_relationships(
        slug="emmanuel", wiki_subpath="me", entity_type="person",
        name="Emmanuel", new_relationships=[_rel("[[claude-api]]", "uses")],
    )
    fm = _read_fm(brain / "wiki" / "me" / "emmanuel.md")
    targets = {r["target"] for r in fm["relationships"]}
    assert targets == {"[[n8n]]", "[[claude-api]]"}


def test_wikilink_injected_into_body(brain):
    path = vault.write_entity_relationships(
        slug="emmanuel", wiki_subpath="me", entity_type="person",
        name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses")],
    )
    body = path.read_text(encoding="utf-8")
    assert "[[n8n]]" in body  # keeps the Obsidian graph wired


def test_bidirectional_inverse_written_to_target(brain):
    # Target node must already exist for the inverse to be wired.
    vault.write_entity_relationships(
        slug="n8n", wiki_subpath="concepts", entity_type="tool",
        name="n8n", new_relationships=[],
    )
    vault.write_entity_relationships(
        slug="emmanuel", wiki_subpath="me", entity_type="person",
        name="Emmanuel", new_relationships=[_rel("[[n8n]]", "uses")],
    )
    target_fm = _read_fm(brain / "wiki" / "concepts" / "n8n.md")
    inverses = [r for r in target_fm.get("relationships", [])
                if r["target"] == "[[emmanuel]]" and r["type"] == "used_by"]
    assert len(inverses) == 1
