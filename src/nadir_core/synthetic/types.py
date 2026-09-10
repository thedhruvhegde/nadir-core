"""Types for synthetic telemetry generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from nadir_core.__about__ import __version__

GENERATOR_VERSION = f"nadir-synthetic-telemetry/{__version__}"

SCENARIO_IDS: Tuple[str, ...] = (
    "normal_route",
    "yaw_drift",
    "pitch_drift",
    "radar_camera_mismatch",
    "radar_camera_desync",
    "imu_bias",
    "time_sync_offset",
    "post_calibration_recovery",
)


class ScenarioId(str, Enum):
    """Built-in synthetic drift scenarios."""

    NORMAL_ROUTE = "normal_route"
    YAW_DRIFT = "yaw_drift"
    PITCH_DRIFT = "pitch_drift"
    RADAR_CAMERA_MISMATCH = "radar_camera_mismatch"
    RADAR_CAMERA_DESYNC = "radar_camera_desync"
    IMU_BIAS = "imu_bias"
    TIME_SYNC_OFFSET = "time_sync_offset"
    POST_CALIBRATION_RECOVERY = "post_calibration_recovery"

    @classmethod
    def all(cls) -> Tuple["ScenarioId", ...]:
        return (
            cls.NORMAL_ROUTE,
            cls.YAW_DRIFT,
            cls.PITCH_DRIFT,
            cls.RADAR_CAMERA_MISMATCH,
            cls.IMU_BIAS,
            cls.TIME_SYNC_OFFSET,
            cls.POST_CALIBRATION_RECOVERY,
        )

    @classmethod
    def from_string(cls, value: str) -> "ScenarioId":
        aliases = {
            "radar_camera_desync": cls.RADAR_CAMERA_MISMATCH,
        }
        if value in aliases:
            return aliases[value]
        try:
            return cls(value)
        except ValueError as exc:
            valid = ", ".join(s.value for s in cls.all()) + ", radar_camera_desync"
            raise ValueError(f"Unknown scenario {value!r}. Choose from: {valid}") from exc


@dataclass(frozen=True)
class ScenarioSpec:
    """Human-readable scenario definition."""

    scenario_id: ScenarioId
    title: str
    description: str
    primary_fault: str
    expected_tier_progression: str


SCENARIO_SPECS: Dict[ScenarioId, ScenarioSpec] = {
    ScenarioId.NORMAL_ROUTE: ScenarioSpec(
        ScenarioId.NORMAL_ROUTE,
        "Normal route driving",
        "Highway commute with nominal calibration and progressing GPS route context.",
        "none",
        "NOMINAL throughout",
    ),
    ScenarioId.YAW_DRIFT: ScenarioSpec(
        ScenarioId.YAW_DRIFT,
        "Yaw extrinsic drift",
        "Progressive camera yaw misalignment while radar/lidar stay near nominal.",
        "camera_extrinsics",
        "NOMINAL → CAUTION → possible CRITICAL at end",
    ),
    ScenarioId.PITCH_DRIFT: ScenarioSpec(
        ScenarioId.PITCH_DRIFT,
        "Pitch extrinsic drift",
        "Camera pitch grows over the drive; translation bias increases slightly.",
        "camera_extrinsics",
        "NOMINAL → CAUTION",
    ),
    ScenarioId.RADAR_CAMERA_MISMATCH: ScenarioSpec(
        ScenarioId.RADAR_CAMERA_MISMATCH,
        "Radar–camera mismatch",
        "Camera stays factory-nominal while radar range and azimuth biases grow.",
        "radar_alignment",
        "NOMINAL → CAUTION",
    ),
    ScenarioId.IMU_BIAS: ScenarioSpec(
        ScenarioId.IMU_BIAS,
        "IMU bias growth",
        "Accelerometer and gyro bias drift with elevated vibration index.",
        "imu_bias",
        "NOMINAL → CAUTION",
    ),
    ScenarioId.TIME_SYNC_OFFSET: ScenarioSpec(
        ScenarioId.TIME_SYNC_OFFSET,
        "Time sync degradation",
        "PTP offset and jitter grow; timestamp quality moves to degraded/unsynced.",
        "time_sync",
        "NOMINAL → CAUTION (via sync quality)",
    ),
    ScenarioId.POST_CALIBRATION_RECOVERY: ScenarioSpec(
        ScenarioId.POST_CALIBRATION_RECOVERY,
        "Post-calibration recovery",
        "Multi-modal drift through mid-drive service calibration, then convergence to nominal.",
        "post_repair_calibration",
        "CAUTION/CRITICAL → NOMINAL after calibration event",
    ),
}


@dataclass
class GenerationConfig:
    """Controls synthetic stream length, timing, and output layout."""

    output_dir: Path = field(default_factory=lambda: Path("NADIR_SDK/data/telemetry/generated"))
    scenarios: Sequence[ScenarioId] = field(default_factory=ScenarioId.all)
    frames_per_scenario: int = 120
    sample_rate_hz: float = 10.0
    seed: int = 42
    vehicle_prefix: str = "SYN-GEN"
    fleet_id: str = "pilot-fleet-synthetic"
    organization_id: str = "org-nadir-pilot"
    platform: str = "BEV-SUV-2025"
    start_time: Optional[datetime] = None
    validate_schema: bool = True
    score_frames: bool = True
    include_perception_tracks: bool = False
    perception_track_frames: int = 500
    run_id: Optional[str] = None
    combined_frame_count: Optional[int] = None
    write_per_scenario_jsonl: bool = True

    def __post_init__(self) -> None:
        if self.frames_per_scenario < 1:
            raise ValueError("frames_per_scenario must be >= 1")
        if self.sample_rate_hz <= 0:
            raise ValueError("sample_rate_hz must be positive")
        self.output_dir = Path(self.output_dir)
        if self.start_time is None:
            self.start_time = datetime(2026, 6, 3, 14, 0, 0, tzinfo=timezone.utc)
        if self.run_id is None:
            self.run_id = self.start_time.strftime("%Y%m%dT%H%M%SZ")
        if self.combined_frame_count is not None and self.combined_frame_count < 1:
            raise ValueError("combined_frame_count must be >= 1 when set")


@dataclass
class ScenarioRunStats:
    """Per-scenario statistics embedded in summary metadata."""

    scenario_id: str
    vehicle_id: str
    output_file: str
    record_count: int
    duration_s: float
    sample_rate_hz: float
    primary_fault: str
    tier_distribution: Dict[str, int]
    peak_camera_drift_deg: float
    peak_radar_drift_mm: float
    peak_lidar_drift_mm: float
    peak_timestamp_offset_ms: float
    first_timestamp: str
    last_timestamp: str


@dataclass
class GenerationSummary:
    """Top-level metadata written beside JSONL outputs."""

    generator_version: str
    generated_at: str
    run_id: str
    seed: int
    frames_per_scenario: int
    sample_rate_hz: float
    output_dir: str
    scenarios: List[ScenarioRunStats]
    schema_path: str = "NADIR_SDK/schemas/v1/telemetry-payload.schema.json"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "generator_version": self.generator_version,
            "generated_at": self.generated_at,
            "run_id": self.run_id,
            "seed": self.seed,
            "frames_per_scenario": self.frames_per_scenario,
            "sample_rate_hz": self.sample_rate_hz,
            "output_dir": self.output_dir,
            "schema_path": self.schema_path,
            "scenarios": [
                {
                    "scenario_id": s.scenario_id,
                    "vehicle_id": s.vehicle_id,
                    "output_file": s.output_file,
                    "record_count": s.record_count,
                    "duration_s": s.duration_s,
                    "sample_rate_hz": s.sample_rate_hz,
                    "primary_fault": s.primary_fault,
                    "tier_distribution": s.tier_distribution,
                    "peak_camera_drift_deg": s.peak_camera_drift_deg,
                    "peak_radar_drift_mm": s.peak_radar_drift_mm,
                    "peak_lidar_drift_mm": s.peak_lidar_drift_mm,
                    "peak_timestamp_offset_ms": s.peak_timestamp_offset_ms,
                    "first_timestamp": s.first_timestamp,
                    "last_timestamp": s.last_timestamp,
                }
                for s in self.scenarios
            ],
        }


@dataclass
class GenerationResult:
    """Paths and summary from a full generation run."""

    output_dir: Path
    summary_path: Path
    summary: GenerationSummary
    jsonl_paths: Dict[str, Path]
