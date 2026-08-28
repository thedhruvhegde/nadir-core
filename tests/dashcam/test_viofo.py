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
    def __init__(self, mapping):
        self.mapping = mapping

    def get(self, url, timeout=8.0):
        for key, body in self.mapping.items():
            if key in url:
                return _Resp(body)
        return _Resp("", status=404)


def test_viofo_html_listing():
    html = Path("tests/fixtures/dashcam/viofo_movie_listing.html").read_text()
    sess = _Sess({"/DCIM/Movie": html})
    src = ViofoSource("http://cam.test", session=sess, use_html=True)
    urls = src.list_recordings()
    assert len(urls) == 2
    assert urls[0].endswith(".MP4")

