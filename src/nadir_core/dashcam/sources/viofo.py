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
