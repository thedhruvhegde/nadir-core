from __future__ import annotations

from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources.synthetic import SyntheticSource


def main() -> None:
    cfg = DashcamConfig(vehicle_id="demo-dash", store_path="out/demo_dashcam.jsonl")
    agent = DashcamAgent(cfg)
