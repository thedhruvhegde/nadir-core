from __future__ import annotations

from typing import List

from nadir_core.dashcam.types import MountEstimate
from nadir_core.scoring.types import DriftTier


def explain_mount(estimate: MountEstimate, tier: DriftTier) -> str:
    parts: List[str] = []
