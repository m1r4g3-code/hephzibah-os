"""
Structured JSON logging for all engines.
Writes to logs/<engine>_<date>.jsonl. Strips secrets from all values.
"""

from __future__ import annotations
import json
import re
import time
from datetime import datetime
from pathlib import Path

_VAULT_ROOT = Path(__file__).parent.parent.parent
_LOGS_DIR = _VAULT_ROOT / "logs"
_SECRET_PATTERN = re.compile(r"(key|token|secret|password|api)", re.IGNORECASE)


def _strip_secrets(obj: object) -> object:
    if isinstance(obj, dict):
        return {
            k: "[REDACTED]" if _SECRET_PATTERN.search(str(k)) else _strip_secrets(v)
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [_strip_secrets(i) for i in obj]
    return obj


class EngineLogger:
    def __init__(self, engine_name: str):
        self.engine_name = engine_name
        _LOGS_DIR.mkdir(exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        self._path = _LOGS_DIR / f"{engine_name}_{date_str}.jsonl"
        self._start: float | None = None

    def start(self, input_path: str | None = None) -> None:
        self._start = time.time()
        self._write({"event": "start", "input": input_path})

    def finish(
        self,
        items_processed: int = 0,
        items_failed: int = 0,
        output_path: str | None = None,
    ) -> None:
        duration_ms = int((time.time() - (self._start or time.time())) * 1000)
        self._write({
            "event": "finish",
            "status": "success",
            "items_processed": items_processed,
            "items_failed": items_failed,
            "duration_ms": duration_ms,
            "output": output_path,
        })

    def error(self, error_type: str, detail: str) -> None:
        self._write({
            "event": "error",
            "status": "error",
            "error_type": error_type,
            "error_detail": detail,
        })

    def info(self, message: str, **kwargs) -> None:
        self._write({"event": "info", "message": message, **kwargs})

    def _write(self, data: dict) -> None:
        entry = {
            "ts": datetime.now().isoformat(timespec="seconds"),
            "engine": self.engine_name,
            **_strip_secrets(data),
        }
        with self._path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
