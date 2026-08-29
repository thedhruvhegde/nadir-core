from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from nadir_core.dashcam.health import HealthSample


class JsonlStore:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, sample: HealthSample) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(sample.as_dict()) + "\n")

    def read_all(self) -> List[dict]:
        if not self.path.exists():
            return []
        out: List[dict] = []
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
        return out

    def extend(self, samples: Iterable[HealthSample]) -> None:
        for s in samples:
            self.append(s)
