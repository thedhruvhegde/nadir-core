from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources import open_source


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nadir-dashcam",
        description="Vision mount health from dashcam footage (shadow mode, local-first)",
    )
