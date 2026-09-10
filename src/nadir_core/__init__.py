"""NADIR Core — open-source ADAS sensor drift scoring."""

from nadir_core.__about__ import __version__
from nadir_core.scoring import DriftTier, PulseScoringOptions, SensorReadings, score_pulse, score_residual

__all__ = [
    "__version__",
    "DriftTier",
    "PulseScoringOptions",
    "SensorReadings",
    "score_pulse",
    "score_residual",
]
