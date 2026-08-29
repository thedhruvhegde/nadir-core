from __future__ import annotations

from typing import Any, Dict, Optional

from nadir_core.dashcam.health import HealthSample

try:
    import requests
except ImportError:  # pragma: no cover
