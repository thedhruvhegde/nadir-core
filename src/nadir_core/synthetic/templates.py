"""Assemble schema-shaped telemetry payloads from sensor state."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Mapping, Optional

import numpy as np

from .routes import DEFAULT_HIGHWAY_ROUTE, RouteTemplate, advance_route
from .scenarios import SensorState
from .types import ScenarioId, SCENARIO_SPECS


def _iso_timestamp(start: datetime, frame_index: int, dt_s: float) -> str:
    instant = start + timedelta(seconds=frame_index * dt_s)
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=timezone.utc)
    return instant.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def build_imu_samples(state: SensorState, rng: np.random.Generator) -> List[Dict[str, Any]]:
    """High-rate IMU batch (4 samples per telemetry frame)."""
    samples: List[Dict[str, Any]] = []
    for offset_ms in (0, 10, 20, 30):
        samples.append(
            {
                "timestamp_offset_ms": offset_ms,
                "accel_mps2": [
                    float(state.imu_accel_mps2[0] + rng.normal(0, 0.008)),
                    float(state.imu_accel_mps2[1] + rng.normal(0, 0.008)),
                    float(state.imu_accel_mps2[2] + rng.normal(0, 0.015)),
                ],
                "gyro_radps": [
                    float(state.imu_gyro_radps[0] + rng.normal(0, 0.0002)),
                    float(state.imu_gyro_radps[1] + rng.normal(0, 0.0002)),
                    float(state.imu_gyro_radps[2] + rng.normal(0, 0.0001)),
                ],
            }
        )
    return samples


def build_telemetry_frame(
    *,
    scenario: ScenarioId,
    vehicle_id: str,
    frame_index: int,
    total_frames: int,
    start_time: datetime,
    dt_s: float,
    state: SensorState,
    rng: np.random.Generator,
    fleet_id: str,
    organization_id: str,
    platform: str,
    route_template: RouteTemplate = DEFAULT_HIGHWAY_ROUTE,
    sequence_base: int = 100_000,
) -> Dict[str, Any]:
    """Build one ``TelemetryPayload``-shaped dict."""
    spec = SCENARIO_SPECS[scenario]
    timestamp = _iso_timestamp(start_time, frame_index, dt_s)
    route = advance_route(
        route_template,
        frame_index=frame_index,
        dt_s=dt_s,
        speed_mps=state.can_vehicle_speed_mps,
    )
    sequence = sequence_base + frame_index

    payload: Dict[str, Any] = {
        "vehicle_id": vehicle_id,
        "timestamp": timestamp,
        "vehicle_identity": {
            "vehicle_id": vehicle_id,
            "vin": f"1N4SYN{vehicle_id[-8:].replace('-', '0')[:11]}",
            "fleet_id": fleet_id,
            "organization_id": organization_id,
            "platform": platform,
            "model_year": 2025,
        },
        "timestamp_quality": {
            "source": state.timestamp_source,
            "offset_ms": round(state.timestamp_offset_ms, 3),
            "jitter_ms": round(state.timestamp_jitter_ms, 3),
            "sequence": sequence,
            "quality": state.timestamp_quality_label,
        },
        "sensor_profile_id": f"prof-adas-v3-gen-{scenario.value}",
        "sensors": state.as_sensors_dict(),
        "imu_samples": build_imu_samples(state, rng),
        "can_signals": {
            "vehicle_speed_mps": state.can_vehicle_speed_mps,
            "steering_angle_deg": round(float(rng.normal(0.5, 1.2)), 2),
            "yaw_rate_radps": round(float(rng.normal(0.008, 0.004)), 4),
            "gear": "drive",
            "brake_applied": False,
        },
        "camera_metadata": {
            "exposure_ms": round(float(rng.normal(11.0, 0.5)), 2),
            "gain_db": round(float(rng.normal(5.5, 0.3)), 2),
            "frame_id": 880_000 + frame_index,
            "temperature_c": round(float(rng.normal(38.0, 1.5)), 2),
            "lane_detection_confidence": round(
                max(0.5, min(0.99, 0.94 - (frame_index / total_frames) * 0.05)),
                3,
            ),
        },
        "radar_metadata": {
            "scan_id": 55_000 + frame_index,
            "target_count": int(rng.integers(3, 8)),
            "interference_level": round(float(rng.uniform(0.01, 0.08)), 3),
        },
        "gps": {
            "latitude_deg": route["latitude_deg"],
            "longitude_deg": route["longitude_deg"],
            "altitude_m": round(float(rng.normal(12.0, 2.0)), 1),
            "fix_quality": "rtk_fixed",
            "hdop": round(float(rng.uniform(0.4, 0.9)), 2),
        },
        "route_context": route,
        "weather": {
            "condition": "clear",
            "temperature_c": round(float(rng.normal(24.0, 1.5)), 1),
            "precipitation_mm_h": 0.0,
            "visibility_m": 16_000,
            "wind_speed_mps": round(float(rng.uniform(2.0, 5.0)), 1),
        },
        "operating_context": {
            "mode": "highway",
            "adas_features_active": ["acc", "lka"],
            "cabin_hvac_stress": False,
            "vibration_index": round(state.vibration_index, 3),
        },
        "metadata": {
            "synthetic_scenario": scenario.value,
            "synthetic_generator": "nadir_sdk.synthetic",
            "frame_index": frame_index,
            "frame_count": total_frames,
            "progress": round(frame_index / max(total_frames - 1, 1), 4),
            "primary_fault": spec.primary_fault,
            "ingest_source": "synthetic-generator-v1",
            "description": spec.description,
        },
    }
    return payload


def vehicle_id_for_scenario(prefix: str, scenario: ScenarioId) -> str:
    slug = scenario.value.upper().replace("_", "-")
    return f"{prefix}-{slug}"[:32]
