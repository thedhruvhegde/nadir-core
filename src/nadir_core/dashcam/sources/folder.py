from __future__ import annotations

import time
from pathlib import Path
from typing import Iterator, List, Optional, Sequence

import numpy as np

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind

