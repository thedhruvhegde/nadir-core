from __future__ import annotations

from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.bridge import vision_to_readings
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources.blackvue import _decode_mjpeg_frames
from nadir_core.dashcam.sources.synthetic import SyntheticSource
from nadir_core.dashcam.types import MountEstimate
from nadir_core.dashcam.upload import build_upload_payload
from nadir_core.dashcam.health import HealthSample
from nadir_core.scoring.types import DriftTier


def test_agent_synthetic_runs(tmp_path):
    cfg = DashcamConfig(vehicle_id="t1", store_path=str(tmp_path / "h.jsonl"))
    agent = DashcamAgent(cfg)
    series = agent.run(SyntheticSource(n_frames=16, yaw_drift_deg=1.5).frames())
    assert series.summary()["n"] == 16
    assert series.latest() is not None

