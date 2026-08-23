from nadir_core.dashcam.sources.base import FrameSource
from nadir_core.dashcam.sources.folder import FolderSource
from nadir_core.dashcam.sources.synthetic import SyntheticSource

__all__ = ["FrameSource", "FolderSource", "SyntheticSource"]


def open_source(kind: str, **kwargs):
    kind = kind.lower().strip()
