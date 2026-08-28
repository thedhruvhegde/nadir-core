from __future__ import annotations

from pathlib import Path

from nadir_core.dashcam.sources.viofo import ViofoSource


class _Resp:
    def __init__(self, text: str, status=200):
        self.text = text
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError("http error")


class _Sess:
