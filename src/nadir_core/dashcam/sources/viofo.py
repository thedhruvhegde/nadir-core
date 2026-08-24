from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from typing import Iterator, List, Optional
from urllib.parse import urljoin

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore


class ViofoSource(BaseSource):
    """VIOFO A229-style local HTTP listing (station / hotspot LAN)."""

    def __init__(
        self,
        host: str,
        *,
        timeout_s: float = 8.0,
        use_html: bool = True,
        session: Optional[object] = None,
    ) -> None:
        if requests is None:
            raise ImportError("requests required for ViofoSource")
        self.base = host if host.startswith("http") else f"http://{host}"
        self.timeout_s = timeout_s
        self.use_html = use_html
        self.session = session or requests.Session()

    def list_recordings(self) -> List[str]:
        if self.use_html:
            urls = self._list_html("/DCIM/Movie")
            if urls:
                return urls
        return self._list_xml()

    def _list_xml(self) -> List[str]:
        url = f"{self.base}/?custom=1&cmd=3015&par=1"
        r = self.session.get(url, timeout=self.timeout_s)
        r.raise_for_status()
        root = ET.fromstring(r.text)
        out: List[str] = []
        for node in root.iter():
            text = (node.text or "").strip()
            if text.lower().endswith((".mp4", ".mov", ".ts")):
                out.append(urljoin(self.base + "/", text.lstrip("/")))
        return out

    def _list_html(self, path: str) -> List[str]:
        url = urljoin(self.base + "/", path.lstrip("/"))
        try:
            r = self.session.get(url, timeout=self.timeout_s)
            r.raise_for_status()
        except Exception:
            return []
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', r.text, flags=re.I)
        out: List[str] = []
        for href in hrefs:
            if href.lower().endswith((".mp4", ".mov", ".ts")):
