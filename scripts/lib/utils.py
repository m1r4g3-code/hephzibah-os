"""
Shared utilities: path resolution, .env loader, manifest R/W, date helpers.
"""

from __future__ import annotations
import json
import os
from datetime import datetime
from pathlib import Path

# Load .env at import time if present
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent.parent / ".env")
except ImportError:
    pass

VAULT_ROOT = Path(__file__).parent.parent.parent

# Domain-aware path registry
DOMAIN_PATHS = {
    "outreach": {
        "sources": VAULT_ROOT / "sources" / "outreach",
        "wiki":    VAULT_ROOT / "wiki" / "outreach",
        "config":  VAULT_ROOT / "config" / "outreach",
    },
    "content": {
        "sources": VAULT_ROOT / "sources" / "content",
        "wiki":    VAULT_ROOT / "wiki" / "content",
    },
    "learning": {
        "sources": VAULT_ROOT / "sources" / "learning",
        "wiki":    VAULT_ROOT / "wiki" / "learning",
    },
    "startup": {
        "sources": VAULT_ROOT / "sources" / "startup",
        "wiki":    VAULT_ROOT / "wiki" / "startup",
    },
}

# Legacy aliases — all outreach engines use these unchanged
SOURCES_DIR = DOMAIN_PATHS["outreach"]["sources"]
WIKI_DIR    = DOMAIN_PATHS["outreach"]["wiki"]
LOGS_DIR    = VAULT_ROOT / "logs"
MANIFEST_PATH = SOURCES_DIR / "prospects" / ".processed_manifest.json"


def get_env(key: str, required: bool = False) -> str | None:
    val = os.environ.get(key)
    if required and not val:
        raise EnvironmentError(
            f"Required environment variable '{key}' is not set. "
            f"Add it to {VAULT_ROOT / '.env'}"
        )
    return val


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"processed_place_ids": [], "processed_transcripts": [], "processed_leads": []}


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


def mark_transcript_processed(filename: str) -> None:
    m = load_manifest()
    if filename not in m["processed_transcripts"]:
        m["processed_transcripts"].append(filename)
    save_manifest(m)


def is_transcript_processed(filename: str) -> bool:
    return filename in load_manifest().get("processed_transcripts", [])


def mark_place_id_processed(place_id: str) -> None:
    m = load_manifest()
    if place_id not in m["processed_place_ids"]:
        m["processed_place_ids"].append(place_id)
    save_manifest(m)


def is_place_id_processed(place_id: str) -> bool:
    return place_id in load_manifest().get("processed_place_ids", [])


def get_processed_place_ids() -> set:
    return set(load_manifest().get("processed_place_ids", []))


def today_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def slugify(text: str) -> str:
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text


def most_recent_transcript() -> Path | None:
    calls_dir = SOURCES_DIR / "calls"
    txts = sorted(calls_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)
    return txts[0] if txts else None
