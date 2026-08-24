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
        media = [p for p in files if p.suffix.lower() in _VIDEO_EXT | _IMAGE_EXT]
        return sorted(media)

    def frames(self) -> Iterator[FramePacket]:
        cv2 = _need_cv2()
        t0 = time.time()
        for path in self.list_media():
            ext = path.suffix.lower()
            if ext in _IMAGE_EXT:
                img = cv2.imread(str(path))
                if img is None:
                    continue
                yield FramePacket(
                    image=img,
                    timestamp_s=t0,
                    source=SourceKind.FOLDER,
                    path=str(path),
                )
                t0 += 0.25
                continue
            cap = cv2.VideoCapture(str(path))
            if not cap.isOpened():
                continue
            idx = 0
            emitted = 0
            try:
                while True:
                    ok, frame = cap.read()
                    if not ok:
                        break
                    if idx % self.stride == 0:
                        yield FramePacket(
                            image=frame,
                            timestamp_s=t0 + emitted / 4.0,
                            source=SourceKind.FOLDER,
                            path=str(path),
                            meta={"frame_index": idx},
                        )
                        emitted += 1
                        if self.max_frames_per_file and emitted >= self.max_frames_per_file:
                            break
                    idx += 1
            finally:
                cap.release()
