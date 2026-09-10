"""Tier classification, fault attribution, and confidence estimation."""

from __future__ import annotations

import math
from typing import Mapping, Optional, Sequence, Tuple

from .types import (
    DriftTier,
    FaultSource,
    ScoringThresholds,
    SensorReadings,
)


def classify_tier(
    camera_deg: float,
    radar_mm: float,
    lidar_mm: float,
    mahal: float,
    thresholds: ScoringThresholds,
) -> DriftTier:
    """Classify drift severity (matches ``api.main._classify_tier``)."""
    if (
        camera_deg >= thresholds.camera_critical_deg
        or radar_mm >= thresholds.radar_critical_mm
        or lidar_mm >= thresholds.lidar_critical_mm
        or mahal >= thresholds.mahal_critical
    ):
        return DriftTier.CRITICAL
    if (
        camera_deg >= thresholds.camera_caution_deg
        or radar_mm >= thresholds.radar_caution_mm
        or lidar_mm >= thresholds.lidar_caution_mm
        or mahal >= thresholds.mahal_caution
    ):
        return DriftTier.CAUTION
    return DriftTier.NOMINAL


def infer_fault_source(
    fault_vector: Mapping[str, float],
    *,
    sensors: SensorReadings,
    timestamp_quality: Optional[Mapping[str, object]] = None,
    camera_deg: float = 0.0,
    radar_mm: float = 0.0,
    lidar_mm: float = 0.0,
) -> FaultSource:
    """
    Determine the dominant fault modality from normalised contributions.

    Time-sync and IMU paths activate when quality metadata indicates stress
    but geometric residuals are not yet dominant.
    """
    if timestamp_quality:
        quality = str(timestamp_quality.get("quality", "")).lower()
        offset_ms = float(timestamp_quality.get("offset_ms", 0.0) or 0.0)
        if quality in {"unsynced", "holdover"} or abs(offset_ms) > 25.0:
            if max(camera_deg, radar_mm, lidar_mm) < 0.5:
                return FaultSource.TIME_SYNC

    cam = float(fault_vector.get("camera", 0.0))
    rad = float(fault_vector.get("radar", 0.0))
    lid = float(fault_vector.get("lidar", 0.0))
    peak = max(cam, rad, lid)

    if peak < 0.34:
        if sensors.imu_accel_mps2 or sensors.imu_gyro_radps:
            return FaultSource.IMU_BIAS
        return FaultSource.UNKNOWN

    leaders = [k for k, v in (("camera", cam), ("radar", rad), ("lidar", lid)) if v >= peak * 0.85]
    if len(leaders) > 1:
        return FaultSource.MULTI_MODAL

    mapping = {
        "camera": FaultSource.CAMERA_EXTRINSICS,
        "radar": FaultSource.RADAR_ALIGNMENT,
        "lidar": FaultSource.LIDAR_REGISTRATION,
    }
    return mapping[leaders[0]]


def vote_entropy_confidence(weights: Mapping[str, float]) -> float:
    """Normalised entropy confidence: peaked votes → 1.0, uniform → 0.0."""
    total = sum(float(v) for v in weights.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for weight in weights.values():
        p = float(weight) / total
        if p > 0:
            entropy -= p * math.log(p)
    max_entropy = math.log(max(len(weights), 1))
    if max_entropy <= 0:
        return 1.0
    return float(max(0.0, min(1.0, 1.0 - entropy / max_entropy)))


def fuse_fault_source_votes(
    votes: Sequence[Tuple[FaultSource, float]],
) -> Tuple[FaultSource, float]:
    """Weighted plurality over detector fault-source votes."""
    if not votes:
        return FaultSource.UNKNOWN, 0.0
    tally: dict[FaultSource, float] = {}
    for source, weight in votes:
        tally[source] = tally.get(source, 0.0) + max(float(weight), 0.0)
    winner = max(tally, key=tally.get)
    total = sum(tally.values()) or 1.0
    return winner, tally[winner] / total


def estimate_confidence(
    tier: DriftTier,
    mahal: float,
    sensors: SensorReadings,
    *,
    camera_deg: float,
    radar_mm: float,
    lidar_mm: float,
    thresholds: ScoringThresholds,
) -> float:
    """
    Deterministic confidence in tier assignment (0–1).

    Starts from LiDAR modality confidence when provided, then adjusts by how
    deep the reading sits inside the assigned tier band.
    """
    base = float(sensors.lidar_confidence if sensors.lidar_confidence is not None else 0.95)

    margin = _tier_margin(
        tier,
        camera_deg=camera_deg,
        radar_mm=radar_mm,
        lidar_mm=lidar_mm,
        mahal=mahal,
        thresholds=thresholds,
    )
    # Larger margin inside a band → higher confidence (capped).
    margin_boost = min(0.12, margin * 0.04)
    mahal_penalty = min(0.15, max(0.0, mahal - thresholds.mahal_caution) * 0.02)

    if tier is DriftTier.CRITICAL:
        score = base + 0.05 + margin_boost - mahal_penalty * 0.5
    elif tier is DriftTier.CAUTION:
        score = base - 0.03 + margin_boost - mahal_penalty
    else:
        score = base + 0.02 + margin_boost * 0.5

    return round(max(0.5, min(0.99, score)), 4)


def _tier_margin(
    tier: DriftTier,
    *,
    camera_deg: float,
    radar_mm: float,
    lidar_mm: float,
    mahal: float,
    thresholds: ScoringThresholds,
) -> float:
    """Minimum distance above the tier's effective lower bound (normalised)."""
    signals = [
        camera_deg - (thresholds.camera_caution_deg if tier is DriftTier.CAUTION else 0.0),
        radar_mm - (thresholds.radar_caution_mm if tier is DriftTier.CAUTION else 0.0),
        lidar_mm - (thresholds.lidar_caution_mm if tier is DriftTier.CAUTION else 0.0),
        mahal - (thresholds.mahal_caution if tier is DriftTier.CAUTION else 0.0),
    ]
    if tier is DriftTier.CRITICAL:
        signals = [
            camera_deg - thresholds.camera_critical_deg,
            radar_mm - thresholds.radar_critical_mm,
            lidar_mm - thresholds.lidar_critical_mm,
            mahal - thresholds.mahal_critical,
        ]
    elif tier is DriftTier.NOMINAL:
        signals = [
            thresholds.camera_caution_deg - camera_deg,
            thresholds.radar_caution_mm - radar_mm,
            thresholds.lidar_caution_mm - lidar_mm,
            thresholds.mahal_caution - mahal,
        ]
    return max(0.0, max(signals))
