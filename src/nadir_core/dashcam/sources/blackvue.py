from __future__ import annotations

import time
from typing import Iterator, Optional

import numpy as np

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore


def _decode_mjpeg_frames(raw: bytes, limit: int = 30):
    """Split multipart/x-mixed-replace style JPEG blobs."""
    marker = b"\xff\xd8"
    end = b"\xff\xd9"
    frames = []
    start = 0
    while len(frames) < limit:
        i = raw.find(marker, start)
        if i < 0:
            break
        j = raw.find(end, i + 2)
        if j < 0:
            break
        frames.append(raw[i : j + 2])
        start = j + 2
    return frames


class BlackVueSource(BaseSource):
    def __init__(
        self,
        host: str = "10.99.77.1",
        *,
        rear: bool = False,
        timeout_s: float = 8.0,
        max_frames: int = 40,
        session: Optional[object] = None,
    ) -> None:
        if requests is None:
            raise ImportError("requests required for BlackVueSource")
        self.base = host if host.startswith("http") else f"http://{host}"
        self.rear = rear
