"""Scenario-specific sensor drift profiles over a telemetry timeline."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, List

import numpy as np

from .geometry import add_noise, euler_to_rotation_matrix, identity_rotation, smoothstep
from .types import ScenarioId


@dataclass
class SensorState:
    """Mutable sensor fields applied when building each telemetry frame."""

    camera_rotation: List[float]
    camera_translation_m: List[float]
    radar_range_bias_m: float
    radar_azimuth_bias_deg: float
    lidar_registration_error_m: float
    lidar_confidence: float
    imu_accel_mps2: List[float]
    imu_gyro_radps: List[float]
    can_vehicle_speed_mps: float
    timestamp_offset_ms: float
    timestamp_jitter_ms: float
    timestamp_quality_label: str
    timestamp_source: str
    vibration_index: float

    def as_sensors_dict(self) -> Dict[str, Any]:
        return {
            "camera_rotation_matrix": self.camera_rotation,
            "camera_translation_m": self.camera_translation_m,
            "radar_range_bias_m": round(self.radar_range_bias_m, 6),
            "radar_azimuth_bias_deg": round(self.radar_azimuth_bias_deg, 5),
            "lidar_registration_error_m": round(self.lidar_registration_error_m, 6),
            "lidar_confidence": round(self.lidar_confidence, 4),
            "imu_accel_mps2": [round(v, 4) for v in self.imu_accel_mps2],
            "imu_gyro_radps": [round(v, 5) for v in self.imu_gyro_radps],
            "can_vehicle_speed_mps": round(self.can_vehicle_speed_mps, 2),
        }


def nominal_sensor_state(rng: np.random.Generator) -> SensorState:
    """Factory-nominal calibration baseline."""
    return SensorState(
        camera_rotation=identity_rotation(),
        camera_translation_m=[1.42, 0.0, 1.18],
        radar_range_bias_m=add_noise(0.00012, rng, 1e-5),
        radar_azimuth_bias_deg=add_noise(0.004, rng, 0.001),
        lidar_registration_error_m=add_noise(0.00008, rng, 1e-5),
        lidar_confidence=add_noise(0.96, rng, 0.01),
        imu_accel_mps2=[0.05, -0.02, 9.79],
        imu_gyro_radps=[0.0008, -0.0012, 0.0003],
        can_vehicle_speed_mps=27.8,
        timestamp_offset_ms=0.2,
        timestamp_jitter_ms=0.8,
        timestamp_quality_label="good",
        timestamp_source="ptp",
        vibration_index=0.12,
    )


def apply_scenario_drift(
    scenario: ScenarioId,
    state: SensorState,
    *,
    frame_index: int,
    total_frames: int,
    rng: np.random.Generator,
) -> SensorState:
    """
    Update ``state`` in-place for the given scenario and timeline position.

    ``progress`` runs 0→1 across frames; early frames stay near nominal where noted.
    """
    progress = frame_index / max(total_frames - 1, 1)
    eased = smoothstep(progress)

    if scenario == ScenarioId.NORMAL_ROUTE:
        state.can_vehicle_speed_mps = add_noise(27.5 + 0.5 * math.sin(progress * 6.28), rng, 0.3)
        state.radar_range_bias_m = add_noise(0.00012, rng, 2e-5)
        state.lidar_confidence = add_noise(0.96, rng, 0.008)
        return state

    if scenario == ScenarioId.YAW_DRIFT:
        yaw_deg = eased * 1.15
        state.camera_rotation = euler_to_rotation_matrix(yaw_deg=yaw_deg)
        state.camera_translation_m = [
            add_noise(1.42, rng, 0.002),
            add_noise(0.01 + eased * 0.04, rng, 0.002),
            add_noise(1.18, rng, 0.002),
        ]
        state.radar_range_bias_m = add_noise(0.00015, rng, 2e-5)
        state.lidar_confidence = max(0.75, add_noise(0.94 - eased * 0.08, rng, 0.01))
        return state

    if scenario == ScenarioId.PITCH_DRIFT:
        pitch_deg = eased * 0.85
        state.camera_rotation = euler_to_rotation_matrix(pitch_deg=pitch_deg)
        state.camera_translation_m = [
            add_noise(1.42, rng, 0.002),
            add_noise(0.0, rng, 0.001),
            add_noise(1.18 + eased * 0.05, rng, 0.003),
        ]
        state.lidar_registration_error_m = add_noise(0.0001 + eased * 0.0008, rng, 1e-5)
        return state

    if scenario == ScenarioId.RADAR_CAMERA_MISMATCH:
        state.camera_rotation = identity_rotation()
        state.radar_range_bias_m = add_noise(0.0002 + eased * 0.0038, rng, 5e-5)
        state.radar_azimuth_bias_deg = add_noise(0.01 + eased * 0.22, rng, 0.005)
        state.lidar_registration_error_m = add_noise(0.00012 + eased * 0.0005, rng, 1e-5)
        state.lidar_confidence = max(0.7, add_noise(0.93 - eased * 0.12, rng, 0.01))
        return state

    if scenario == ScenarioId.IMU_BIAS:
        bias_scale = eased
        state.imu_accel_mps2 = [
            add_noise(0.05 + bias_scale * 0.18, rng, 0.01),
            add_noise(-0.02 + bias_scale * 0.12, rng, 0.01),
            add_noise(9.79 - bias_scale * 0.08, rng, 0.02),
        ]
        state.imu_gyro_radps = [
            add_noise(0.0008 + bias_scale * 0.006, rng, 0.0003),
            add_noise(-0.0012 + bias_scale * 0.004, rng, 0.0003),
            add_noise(0.0003 + bias_scale * 0.002, rng, 0.0002),
        ]
        state.vibration_index = min(0.95, 0.12 + eased * 0.45)
        state.lidar_confidence = max(0.78, add_noise(0.94 - eased * 0.06, rng, 0.01))
        return state

    if scenario == ScenarioId.TIME_SYNC_OFFSET:
        state.timestamp_offset_ms = add_noise(0.3 + eased * 28.0, rng, 0.5)
        state.timestamp_jitter_ms = add_noise(0.9 + eased * 14.0, rng, 0.4)
        if eased < 0.35:
            state.timestamp_quality_label = "good"
            state.timestamp_source = "ptp"
        elif eased < 0.7:
            state.timestamp_quality_label = "degraded"
            state.timestamp_source = "gnss"
        else:
            state.timestamp_quality_label = "unsynced"
            state.timestamp_source = "gnss"
        state.radar_range_bias_m = add_noise(0.00018 + eased * 0.0004, rng, 2e-5)
        return state

    if scenario == ScenarioId.POST_CALIBRATION_RECOVERY:
        calibration_frame = int(total_frames * 0.4)
        if frame_index < calibration_frame:
            pre_progress = frame_index / max(calibration_frame, 1)
            pre_eased = smoothstep(pre_progress)
            state.camera_rotation = euler_to_rotation_matrix(yaw_deg=pre_eased * 1.05)
            state.radar_range_bias_m = add_noise(0.0002 + pre_eased * 0.0035, rng, 4e-5)
            state.radar_azimuth_bias_deg = add_noise(0.02 + pre_eased * 0.18, rng, 0.004)
            state.imu_accel_mps2 = [
                add_noise(0.06 + pre_eased * 0.14, rng, 0.01),
                add_noise(-0.02 + pre_eased * 0.1, rng, 0.01),
                add_noise(9.78 - pre_eased * 0.06, rng, 0.015),
            ]
            state.vibration_index = min(0.9, 0.15 + pre_eased * 0.35)
        else:
            post_frames = max(total_frames - calibration_frame, 1)
            post_progress = (frame_index - calibration_frame) / post_frames
            recovery = 1.0 - smoothstep(post_progress)
            state.camera_rotation = euler_to_rotation_matrix(yaw_deg=recovery * 0.08)
            state.radar_range_bias_m = add_noise(0.00012 + recovery * 0.00025, rng, 2e-5)
            state.radar_azimuth_bias_deg = add_noise(0.005 + recovery * 0.04, rng, 0.002)
            state.imu_accel_mps2 = [
                add_noise(0.05 + recovery * 0.02, rng, 0.005),
                add_noise(-0.02 + recovery * 0.01, rng, 0.005),
                add_noise(9.79 - recovery * 0.01, rng, 0.01),
            ]
            state.vibration_index = max(0.12, 0.2 + recovery * 0.15)
            state.timestamp_quality_label = "good" if post_progress > 0.5 else "degraded"
            state.timestamp_source = "ptp" if post_progress > 0.5 else "gnss"
        return state

    raise ValueError(f"Unhandled scenario: {scenario}")
