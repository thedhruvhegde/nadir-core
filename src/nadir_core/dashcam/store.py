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
