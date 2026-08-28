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


def test_bridge_readings():
    est = MountEstimate(
        yaw_deg=0.5,
        pitch_deg=0.1,
        roll_deg=0.2,
        horizon_y_norm=0.45,
        flow_yaw_rate_dps=0.0,
        confidence=0.7,
    )
    readings = vision_to_readings(est)
    assert readings.camera_rotation_matrix is not None
    assert len(readings.camera_rotation_matrix) == 9


def test_mjpeg_split():
    # minimal jpeg markers
    blob = b"xx\xff\xd8abc\xff\xd9yy\xff\xd8def\xff\xd9"
    parts = _decode_mjpeg_frames(blob, limit=5)
    assert len(parts) == 2


def test_upload_payload_shape():
    est = MountEstimate(0.1, 0.0, 0.0, 0.45, 0.0, 0.5, ())
    sample = HealthSample(1.0, est, DriftTier.NOMINAL, 0.2, 0.9, "ok")
    payload = build_upload_payload("v", sample)
    assert payload["claim_boundary"] == "vision_mount_health_only"
    assert payload["source"] == "dashcam_open_core"
