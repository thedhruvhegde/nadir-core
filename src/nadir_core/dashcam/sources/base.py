from __future__ import annotations

from typing import Iterator, Optional, Protocol

from nadir_core.dashcam.types import FramePacket


class FrameSource(Protocol):
    def frames(self) -> Iterator[FramePacket]:
