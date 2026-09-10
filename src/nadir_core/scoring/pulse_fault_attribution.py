"""Bayesian fault-source attribution v2 for Pulse (P8).

Produces a calibrated posterior over {camera, radar, lidar, fusion} that sums
to 1.0 and complements the discrete ``probable_fault_source`` label.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Optional

from .types import FaultSource, SensorReadings


@dataclass(frozen=True)
class FaultAttributionV2Config:
    temperature: float = 1.4
    fusion_prior: float = 0.08
    imu_prior: float = 0.05
    min_posterior: float = 1e-6


def _softmax(logits: Mapping[str, float]) -> dict[str, float]:
    max_logit = max(logits.values())
    exp_vals = {k: math.exp(v - max_logit) for k, v in logits.items()}
    total = sum(exp_vals.values()) or 1.0
    return {k: float(v / total) for k, v in exp_vals.items()}


def bayesian_fault_posterior(
    fault_vector: Mapping[str, float],
    *,
    sensors: SensorReadings,
    probable_fault_source: FaultSource,
    config: Optional[FaultAttributionV2Config] = None,
) -> dict[str, float]:
    """
    Softmax posterior over camera / radar / lidar / fusion modalities.

    Uses normalized fault-vector magnitudes as likelihood terms with small
    priors for fusion (multi-modal) and IMU coupling when gyro/accel present.
    """
    cfg = config or FaultAttributionV2Config()
    cam = max(float(fault_vector.get("camera", 0.0)), cfg.min_posterior)
    rad = max(float(fault_vector.get("radar", 0.0)), cfg.min_posterior)
    lid = max(float(fault_vector.get("lidar", 0.0)), cfg.min_posterior)

    logits = {
        "camera": math.log(cam) / cfg.temperature,
        "radar": math.log(rad) / cfg.temperature,
        "lidar": math.log(lid) / cfg.temperature,
        "fusion": math.log(cfg.fusion_prior),
    }

    if probable_fault_source is FaultSource.MULTI_MODAL:
        logits["fusion"] += 1.35
    elif probable_fault_source is FaultSource.IMU_BIAS and (
        sensors.imu_accel_mps2 or sensors.imu_gyro_radps
    ):
        logits["fusion"] += math.log(cfg.imu_prior + 0.5)

    peak = max(cam, rad, lid)
    if peak > 0 and len([v for v in (cam, rad, lid) if v >= peak * 0.85]) > 1:
        logits["fusion"] += 0.65

    posterior = _softmax(logits)
    total = sum(posterior.values())
    if abs(total - 1.0) > 1e-6:
        posterior = {k: v / total for k, v in posterior.items()}
    return {k: round(v, 6) for k, v in posterior.items()}


def posterior_entropy(posterior: Mapping[str, float]) -> float:
    entropy = 0.0
    for weight in posterior.values():
        p = float(weight)
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)


def attribution_confidence_from_posterior(posterior: Mapping[str, float]) -> float:
    """Peaked posterior → high confidence (0–1)."""
    entropy = posterior_entropy(posterior)
    max_entropy = math.log(max(len(posterior), 1))
    if max_entropy <= 0:
        return 1.0
    return round(max(0.0, min(1.0, 1.0 - entropy / max_entropy)), 4)
