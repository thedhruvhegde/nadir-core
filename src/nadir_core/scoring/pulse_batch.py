"""Batch vectorized Pulse scoring for fleet frames (P10)."""

from __future__ import annotations

import time
from typing import Any, List, Mapping, Optional, Sequence, Union

import numpy as np

from .pulse import score_pulse
from .pulse_options import PulseScoringOptions
from .types import ResidualScoreResult, ScoringThresholds, SensorReadings


def _frame_sensors(frame: Mapping[str, Any]) -> Union[SensorReadings, Mapping[str, Any]]:
    sensors = frame.get("sensors")
    if isinstance(sensors, Mapping):
        return sensors
    return frame


def score_pulse_batch(
    vehicle_id: str,
    frames: Sequence[Mapping[str, Any]],
    *,
    baseline_camera_rotation: Optional[Sequence[float]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    options: Optional[PulseScoringOptions] = None,
    shared_pulse_context: Optional[Mapping[str, object]] = None,
) -> List[ResidualScoreResult]:
    """Score a sequence of telemetry frames on the Pulse lane."""
    results: List[ResidualScoreResult] = []
    for frame in frames:
        ctx = frame if shared_pulse_context is None else {**shared_pulse_context, **frame}
        ts = frame.get("timestamp")
        timestamp = str(ts) if ts is not None else None
        tq = frame.get("timestamp_quality")
        timestamp_quality = tq if isinstance(tq, Mapping) else None
        results.append(
            score_pulse(
                vehicle_id,
                _frame_sensors(frame),
                baseline_camera_rotation=baseline_camera_rotation,
                timestamp=timestamp,
                timestamp_quality=timestamp_quality,
                thresholds=thresholds,
                options=options,
                pulse_context=ctx,
            )
        )
    return results


def score_pulse_batch_vectorized(
    vehicle_id: str,
    normalized_vectors: np.ndarray,
    *,
    thresholds: Optional[ScoringThresholds] = None,
) -> np.ndarray:
    """
    Vectorized Mahalanobis distance for pre-normalized (N, 3) drift vectors.

    Used by batch export paths; tier classification still runs per-frame in
    ``score_pulse_batch`` when full API results are required.
    """
    cfg = thresholds or ScoringThresholds()
    if normalized_vectors.ndim != 2 or normalized_vectors.shape[1] != 3:
        raise ValueError("normalized_vectors must have shape (N, 3)")
    return np.sqrt(np.sum(normalized_vectors.astype(float) ** 2, axis=1))


def benchmark_pulse_batch(
    vehicle_id: str,
    frames: Sequence[Mapping[str, Any]],
    *,
    options: Optional[PulseScoringOptions] = None,
) -> dict[str, float]:
    """Return elapsed seconds and frames/sec for batch scoring."""
    started = time.perf_counter()
    results = score_pulse_batch(vehicle_id, frames, options=options)
    elapsed = time.perf_counter() - started
    count = max(len(results), 1)
    return {
        "frame_count": float(len(results)),
        "elapsed_s": round(elapsed, 4),
        "frames_per_s": round(len(results) / elapsed, 2),
    }
