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
