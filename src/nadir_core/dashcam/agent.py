from __future__ import annotations

from typing import Iterator, Optional

from nadir_core.dashcam.bridge import score_mount_estimate
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.health import HealthSample, HealthSeries
from nadir_core.dashcam.store import JsonlStore
from nadir_core.dashcam.types import FramePacket
from nadir_core.dashcam.upload import upload_sample
from nadir_core.dashcam.vision.explain import explain_mount
from nadir_core.dashcam.vision.mount import MountTracker


class DashcamAgent:
    def __init__(self, config: Optional[DashcamConfig] = None) -> None:
        self.config = config or DashcamConfig.from_env()
        self.tracker = MountTracker(max_width=self.config.max_width)
        self.series = HealthSeries()
        self.store = JsonlStore(self.config.store_path)
