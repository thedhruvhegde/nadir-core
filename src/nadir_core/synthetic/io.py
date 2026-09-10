"""JSONL and summary metadata writers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Mapping

from .types import GenerationSummary


def write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> int:
    """Write one JSON object per line; returns record count."""
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, separators=(",", ":"), sort_keys=False))
            handle.write("\n")
            count += 1
    return count


def write_summary(path: Path, summary: GenerationSummary) -> None:
    """Write generation summary metadata as indented JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(summary.to_dict(), handle, indent=2, sort_keys=False)
        handle.write("\n")
