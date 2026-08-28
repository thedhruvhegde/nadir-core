from __future__ import annotations

from pathlib import Path

from nadir_core.dashcam.sources.viofo import ViofoSource


class _Resp:
    def __init__(self, text: str, status=200):
