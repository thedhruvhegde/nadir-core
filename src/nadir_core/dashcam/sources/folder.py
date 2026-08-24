from __future__ import annotations

import time
from pathlib import Path
from typing import Iterator, List, Optional, Sequence

import numpy as np

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind

_VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".ts"}
_IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def _need_cv2():
    try:
        import cv2  # noqa: F401
    except ImportError as exc:
        raise ImportError("opencv-python-headless required for folder video/image decode") from exc
    import cv2

    return cv2


class FolderSource(BaseSource):
    def __init__(
        self,
        root: str,
        *,
        recursive: bool = True,
        max_frames_per_file: Optional[int] = 120,
        stride: int = 5,
    ) -> None:
        self.root = Path(root)
        self.recursive = recursive
        self.max_frames_per_file = max_frames_per_file
        self.stride = max(1, stride)

    def list_media(self) -> List[Path]:
        if not self.root.exists():
            return []
        pattern = "**/*" if self.recursive else "*"
        files = [p for p in self.root.glob(pattern) if p.is_file()]
