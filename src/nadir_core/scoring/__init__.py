"""NADIR Open Core scoring — Echo residual engine + Pulse lane."""

from __future__ import annotations

from .engine import DriftScoringEngine, score_residual, score_telemetry_payload
from .pulse import score_pulse
from .pulse_options import PulseScoringOptions, default_pulse_options
from .types import (
    DriftTier,
    ResidualScoreResult,
    ScoringRequest,
    ScoringThresholds,
    SensorReadings,
)

try:
    from .pulse import PulseScoringLane
except ImportError:  # pragma: no cover
    PulseScoringLane = None  # type: ignore

__all__ = [
    "DriftScoringEngine",
    "score_residual",
    "score_telemetry_payload",
    "score_pulse",
    "PulseScoringLane",
    "PulseScoringOptions",
    "default_pulse_options",
    "DriftTier",
    "ResidualScoreResult",
    "ScoringRequest",
    "ScoringThresholds",
    "SensorReadings",
]
