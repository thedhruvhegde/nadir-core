"""Configuration and enrichment types for NADIR Pulse v2 scoring lane."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional


@dataclass(frozen=True)
class PulseScoringOptions:
    """
    Feature flags for Pulse v2 math layers (P1–P10).

    Defaults enable P1–P5 + vibration notch; optional layers off by default.
    """

    enable_adaptive_sigma: bool = True
    enable_robust_mahalanobis: bool = True
    enable_cross_modal_gate: bool = True
    enable_block_covariance: bool = False
    enable_thermal_sigma: bool = True
    enable_vibration_notch: bool = True
    enable_edge_cusum_boost: bool = False
    enable_gradual_slope_boost: bool = False
    enable_fault_attribution_v2: bool = False
    enable_conformal_lite: bool = False
    enable_latency_profiler: bool = True
    adaptive_min_samples: int = 30
    cross_modal_confidence: float = 0.997
    robust_huber_delta: float = 2.5
    thermal_reference_c: float = 25.0
    thermal_alpha_per_c: float = 0.008


@dataclass(frozen=True)
class PulseEnrichment:
    """Optional Pulse-specific metadata attached to scoring results."""

    pipeline_version: str = "pulse"
    adaptive_sigma: Optional[Dict[str, Any]] = None
    robust_mahalanobis: Optional[Dict[str, Any]] = None
    cross_modal_gate: Optional[Dict[str, Any]] = None
    block_covariance: Optional[Dict[str, Any]] = None
    thermal_sigma: Optional[Dict[str, Any]] = None
    vibration_filter: Optional[Dict[str, Any]] = None
    edge_cusum: Optional[Dict[str, Any]] = None
    gradual_slope: Optional[Dict[str, Any]] = None
    fault_attribution_v2: Optional[Dict[str, Any]] = None
    conformal_lite: Optional[Dict[str, Any]] = None
    scoring_gated: bool = False
    gate_reason: Optional[str] = None

    def to_api_dict(self) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "pipeline_version": self.pipeline_version,
            "scoring_gated": self.scoring_gated,
        }
        if self.gate_reason is not None:
            body["gate_reason"] = self.gate_reason
        if self.adaptive_sigma is not None:
            body["adaptive_sigma"] = dict(self.adaptive_sigma)
        if self.robust_mahalanobis is not None:
            body["robust_mahalanobis"] = dict(self.robust_mahalanobis)
        if self.cross_modal_gate is not None:
            body["cross_modal_gate"] = dict(self.cross_modal_gate)
        if self.block_covariance is not None:
            body["block_covariance"] = dict(self.block_covariance)
        if self.thermal_sigma is not None:
            body["thermal_sigma"] = dict(self.thermal_sigma)
        if self.vibration_filter is not None:
            body["vibration_filter"] = dict(self.vibration_filter)
        if self.edge_cusum is not None:
            body["edge_cusum"] = dict(self.edge_cusum)
        if self.gradual_slope is not None:
            body["gradual_slope"] = dict(self.gradual_slope)
        if self.fault_attribution_v2 is not None:
            body["fault_attribution_v2"] = dict(self.fault_attribution_v2)
        if self.conformal_lite is not None:
            body["conformal_lite"] = dict(self.conformal_lite)
        return body


def default_pulse_options() -> PulseScoringOptions:
    """Open Core Pulse defaults."""
    return PulseScoringOptions(
        enable_adaptive_sigma=True,
        enable_robust_mahalanobis=True,
        enable_cross_modal_gate=True,
        enable_block_covariance=False,
        enable_thermal_sigma=True,
        enable_vibration_notch=True,
        enable_edge_cusum_boost=False,
        enable_gradual_slope_boost=False,
        enable_fault_attribution_v2=False,
        enable_conformal_lite=False,
        enable_latency_profiler=False,
    )



def pulse_options_from_mapping(payload: Optional[Mapping[str, object]]) -> PulseScoringOptions:
    """Build ``PulseScoringOptions`` from an API ``pulse_options`` object."""
    from dataclasses import fields, replace

    base = default_pulse_options()
    if not payload:
        return base
    allowed = {f.name for f in fields(PulseScoringOptions)}
    updates = {
        key: payload[key]
        for key in allowed
        if key in payload and payload[key] is not None
    }
    return replace(base, **updates) if updates else base
