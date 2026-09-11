
from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources.synthetic import SyntheticSource
from nadir_core.dashcam.sim.scenarios import frames_scenario_3
from nadir_core.dashcam.analytics.report import render_text_report

def test_deeper_pipeline(tmp_path):
    cfg = DashcamConfig(vehicle_id="depth", store_path=str(tmp_path/"h.jsonl"))
    agent = DashcamAgent(cfg)
    series = agent.run(SyntheticSource(n_frames=12, yaw_drift_deg=2.0, roll_drift_deg=1.0).frames())
    assert series.summary()["n"] == 12
    text = render_text_report(series)
    assert "vision mount" in text.lower() or "boundary" in text.lower()
    assert len(frames_scenario_3()) >= 10
