from nadir_core.dashcam.sources.base import FrameSource
from nadir_core.dashcam.sources.folder import FolderSource
from nadir_core.dashcam.sources.synthetic import SyntheticSource

__all__ = ["FrameSource", "FolderSource", "SyntheticSource"]


def open_source(kind: str, **kwargs):
    kind = kind.lower().strip()
    if kind == "folder":
        return FolderSource(**kwargs)
    if kind == "viofo":
        from nadir_core.dashcam.sources.viofo import ViofoSource

        return ViofoSource(**kwargs)
    if kind == "blackvue":
        from nadir_core.dashcam.sources.blackvue import BlackVueSource

        return BlackVueSource(**kwargs)
    if kind == "rtsp":
        from nadir_core.dashcam.sources.rtsp import RtspSource

        return RtspSource(**kwargs)
    if kind == "synthetic":
        return SyntheticSource(**kwargs)
    raise ValueError(f"unknown source kind: {kind}")
