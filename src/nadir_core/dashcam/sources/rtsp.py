from __future__ import annotations

import time
from typing import Iterator, Optional

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind


class RtspSource(BaseSource):
    def __init__(
        self,
        url: str,
        *,
        max_frames: int = 120,
        stride: int = 2,
    ) -> None:
        self.url = url
        self.max_frames = max_frames
        self.stride = max(1, stride)
