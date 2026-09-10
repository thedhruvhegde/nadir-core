"""Synthetic ADAS telemetry generators for demos and tests."""

from __future__ import annotations

from .generator import SyntheticTelemetryGenerator, generate_scenario_dataset
from .io import write_jsonl, write_summary
from .types import GenerationConfig, GenerationSummary, ScenarioId

__all__ = [
    "SyntheticTelemetryGenerator",
    "generate_scenario_dataset",
    "write_jsonl",
    "write_summary",
    "GenerationConfig",
    "GenerationSummary",
    "ScenarioId",
]
