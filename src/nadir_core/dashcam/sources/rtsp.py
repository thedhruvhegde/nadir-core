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

    def frames(self) -> Iterator[FramePacket]:
        from nadir_core.dashcam.sources.folder import _need_cv2

        cv2 = _need_cv2()
        cap = cv2.VideoCapture(self.url)
        if not cap.isOpened():
            raise RuntimeError(f"could not open rtsp url: {self.url}")
        idx = 0
        emitted = 0
        t0 = time.time()
        try:
            while emitted < self.max_frames:
                ok, frame = cap.read()
                if not ok:
                    break
                if idx % self.stride == 0:
                    yield FramePacket(
                        image=frame,
                        timestamp_s=t0 + emitted / 15.0,
                        source=SourceKind.RTSP,
                        path=self.url,
                        meta={"index": idx},
                    )
                    emitted += 1
                idx += 1
        finally:
            cap.release()
