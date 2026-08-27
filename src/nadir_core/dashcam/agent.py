from __future__ import annotations

from typing import Iterator, Optional

from nadir_core.dashcam.bridge import score_mount_estimate
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.health import HealthSample, HealthSeries
from nadir_core.dashcam.store import JsonlStore
from nadir_core.dashcam.types import FramePacket
from nadir_core.dashcam.upload import upload_sample
