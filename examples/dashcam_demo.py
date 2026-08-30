from __future__ import annotations

from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources.synthetic import SyntheticSource


def main() -> None:
    cfg = DashcamConfig(vehicle_id="demo-dash", store_path="out/demo_dashcam.jsonl")
    agent = DashcamAgent(cfg)
    src = SyntheticSource(n_frames=24, yaw_drift_deg=1.1, roll_drift_deg=0.6)
    series = agent.run(src.frames())
    print(series.summary())
    last = series.latest()
    if last:
        print(last.explanation)


if __name__ == "__main__":
    main()

