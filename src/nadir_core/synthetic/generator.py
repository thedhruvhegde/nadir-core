"""Synthetic telemetry stream generator."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Mapping, Optional

import numpy as np

from nadir_core.scoring import score_telemetry_payload
from nadir_core.scoring.math import extract_drift_measurements, lidar_drift_mm, radar_drift_mm
from nadir_core.scoring.types import ScoringThresholds, SensorReadings

from .io import write_jsonl, write_summary
from .scenarios import SensorState, apply_scenario_drift, nominal_sensor_state
from .templates import build_telemetry_frame, vehicle_id_for_scenario
from .types import (
    GENERATOR_VERSION,
    GenerationConfig,
    GenerationResult,
    GenerationSummary,
    ScenarioId,
    ScenarioRunStats,
    SCENARIO_SPECS,
)
from .validation import schema_path_relative, validate_telemetry_payload


class SyntheticTelemetryGenerator:
    """
    Generate schema-valid synthetic telemetry timelines for NADIR demos.

    Produces one JSONL file per scenario plus a ``summary.json`` metadata file.
    """

    def __init__(self, config: Optional[GenerationConfig] = None) -> None:
        self.config = config or GenerationConfig()

    def _build_frame(
        self,
        scenario: ScenarioId,
        frame_index: int,
        *,
        total_frames: int,
        rng: np.random.Generator,
        state: SensorState,
    ) -> Dict[str, Any]:
        cfg = self.config
        apply_scenario_drift(
            scenario,
            state,
            frame_index=frame_index,
            total_frames=total_frames,
            rng=rng,
        )
        return build_telemetry_frame(
            scenario=scenario,
            vehicle_id=vehicle_id_for_scenario(cfg.vehicle_prefix, scenario),
            frame_index=frame_index,
            total_frames=total_frames,
            start_time=cfg.start_time or datetime.now(timezone.utc),
            dt_s=1.0 / cfg.sample_rate_hz,
            state=state,
            rng=rng,
            fleet_id=cfg.fleet_id,
            organization_id=cfg.organization_id,
            platform=cfg.platform,
            sequence_base=100_000 + hash(scenario.value) % 1000,
        )

    def iter_frames(self, scenario: ScenarioId) -> Iterator[Dict[str, Any]]:
        """Yield telemetry payloads for a single scenario."""
        cfg = self.config
        rng = np.random.default_rng(cfg.seed + hash(scenario.value) % 10_000)
        state = nominal_sensor_state(rng)

        for frame_index in range(cfg.frames_per_scenario):
            frame = self._build_frame(
                scenario,
                frame_index,
                total_frames=cfg.frames_per_scenario,
                rng=rng,
                state=state,
            )
            if cfg.validate_schema:
                validate_telemetry_payload(frame)
            yield frame

    def generate_scenario(
        self,
        scenario: ScenarioId,
        *,
        output_dir: Optional[Path] = None,
    ) -> ScenarioRunStats:
        """Generate one scenario JSONL and return per-scenario statistics."""
        cfg = self.config
        out = output_dir or (cfg.output_dir / cfg.run_id)
        out.mkdir(parents=True, exist_ok=True)

        filename = f"{scenario.value}.jsonl"
        path = out / filename
        records = list(self.iter_frames(scenario))
        write_jsonl(path, records)

        return _stats_for_scenario(scenario, records, path, cfg)

    def generate_all(self, *, output_dir: Optional[Path] = None) -> GenerationResult:
        """Generate all configured scenarios and write summary metadata."""
        cfg = self.config
        out = output_dir or (cfg.output_dir / cfg.run_id)
        out.mkdir(parents=True, exist_ok=True)

        scenario_stats: List[ScenarioRunStats] = []
        jsonl_paths: Dict[str, Path] = {}

        for scenario in cfg.scenarios:
            stats = self.generate_scenario(scenario, output_dir=out)
            scenario_stats.append(stats)
            jsonl_paths[scenario.value] = out / stats.output_file

        summary = GenerationSummary(
            generator_version=GENERATOR_VERSION,
            generated_at=datetime.now(timezone.utc).isoformat(),
            run_id=cfg.run_id or "run",
            seed=cfg.seed,
            frames_per_scenario=cfg.frames_per_scenario,
            sample_rate_hz=cfg.sample_rate_hz,
            output_dir=str(out),
            scenarios=scenario_stats,
            schema_path=schema_path_relative(),
        )
        summary_path = out / "summary.json"
        write_summary(summary_path, summary)

        return GenerationResult(
            output_dir=out,
            summary_path=summary_path,
            summary=summary,
            jsonl_paths=jsonl_paths,
        )

    def generate_combined_fleet(self, *, output_dir: Optional[Path] = None) -> GenerationResult:
        """
        Write a single ``frames.jsonl`` with ``combined_frame_count`` schema-valid rows.

        Scenarios are round-robin interleaved so drift profiles stay represented at scale.
        """
        cfg = self.config
        count = cfg.combined_frame_count
        if count is None:
            raise ValueError("combined_frame_count must be set for combined fleet generation")

        out = output_dir or (cfg.output_dir / cfg.run_id)
        out.mkdir(parents=True, exist_ok=True)
        scenarios = list(cfg.scenarios)
        if not scenarios:
            raise ValueError("At least one scenario is required")

        max_per_scenario = (count + len(scenarios) - 1) // len(scenarios)
        rng_by_scenario = {
            s: np.random.default_rng(cfg.seed + hash(s.value) % 10_000) for s in scenarios
        }
        state_by_scenario = {s: nominal_sensor_state(rng_by_scenario[s]) for s in scenarios}
        frame_counters: Dict[ScenarioId, int] = {s: 0 for s in scenarios}

        records: List[Dict[str, Any]] = []
        for global_index in range(count):
            scenario = scenarios[global_index % len(scenarios)]
            frame_index = frame_counters[scenario]
            frame_counters[scenario] += 1
            frame = self._build_frame(
                scenario,
                frame_index,
                total_frames=max_per_scenario,
                rng=rng_by_scenario[scenario],
                state=state_by_scenario[scenario],
            )
            frame["metadata"]["combined_fleet_index"] = global_index
            frame["metadata"]["combined_fleet_count"] = count
            if cfg.validate_schema:
                validate_telemetry_payload(frame)
            records.append(frame)

        combined_path = out / "frames.jsonl"
        write_jsonl(combined_path, records)

        scenario_stats: List[ScenarioRunStats] = []
        jsonl_paths: Dict[str, Path] = {"frames": combined_path}

        if cfg.write_per_scenario_jsonl:
            for scenario in scenarios:
                stats = self.generate_scenario(scenario, output_dir=out)
                scenario_stats.append(stats)
                jsonl_paths[scenario.value] = out / stats.output_file
        else:
            by_scenario: Dict[str, List[Mapping[str, Any]]] = {}
            for record in records:
                scenario_id = str(record.get("metadata", {}).get("synthetic_scenario", "unknown"))
                by_scenario.setdefault(scenario_id, []).append(record)
            for scenario in scenarios:
                subset = by_scenario.get(scenario.value, [])
                if not subset:
                    continue
                scenario_stats.append(
                    _stats_for_scenario(scenario, subset, combined_path, cfg)
                )

        summary = GenerationSummary(
            generator_version=GENERATOR_VERSION,
            generated_at=datetime.now(timezone.utc).isoformat(),
            run_id=cfg.run_id or "run",
            seed=cfg.seed,
            frames_per_scenario=max_per_scenario,
            sample_rate_hz=cfg.sample_rate_hz,
            output_dir=str(out),
            scenarios=scenario_stats,
            schema_path=schema_path_relative(),
        )
        summary_path = out / "summary.json"
        write_summary(summary_path, summary)

        return GenerationResult(
            output_dir=out,
            summary_path=summary_path,
            summary=summary,
            jsonl_paths=jsonl_paths,
        )


def generate_scenario_dataset(
    config: Optional[GenerationConfig] = None,
) -> GenerationResult:
    """Functional entry point — generate all scenarios with optional config."""
    return SyntheticTelemetryGenerator(config).generate_all()


def _stats_for_scenario(
    scenario: ScenarioId,
    records: List[Mapping[str, Any]],
    path: Path,
    cfg: GenerationConfig,
) -> ScenarioRunStats:
    spec = SCENARIO_SPECS[scenario]
    thresholds = ScoringThresholds()
    tier_counts: Counter[str] = Counter()
    peak_cam = 0.0
    peak_rad = 0.0
    peak_lid = 0.0
    peak_offset = 0.0

    for record in records:
        tq = record.get("timestamp_quality") or {}
        peak_offset = max(peak_offset, float(tq.get("offset_ms", 0.0)))

        sensors_raw = record.get("sensors") or {}
        sensors = SensorReadings.from_mapping(sensors_raw)
        cam_deg, rad_mm, lid_mm = extract_drift_measurements(sensors, None, thresholds)
        peak_cam = max(peak_cam, cam_deg)
        peak_rad = max(peak_rad, radar_drift_mm(sensors.radar_range_bias_m, sensors.radar_azimuth_bias_deg))
        peak_lid = max(peak_lid, lidar_drift_mm(sensors.lidar_registration_error_m))

        if cfg.score_frames:
            result = score_telemetry_payload(record)
            tier_counts[result.tier.value] += 1

    vehicle_id = str(records[0].get("vehicle_id", "")) if records else ""
    duration_s = cfg.frames_per_scenario / cfg.sample_rate_hz

    return ScenarioRunStats(
        scenario_id=scenario.value,
        vehicle_id=vehicle_id,
        output_file=path.name,
        record_count=len(records),
        duration_s=round(duration_s, 3),
        sample_rate_hz=cfg.sample_rate_hz,
        primary_fault=spec.primary_fault,
        tier_distribution=dict(sorted(tier_counts.items())),
        peak_camera_drift_deg=round(peak_cam, 4),
        peak_radar_drift_mm=round(peak_rad, 4),
        peak_lidar_drift_mm=round(peak_lid, 4),
        peak_timestamp_offset_ms=round(peak_offset, 3),
        first_timestamp=str(records[0].get("timestamp", "")) if records else "",
        last_timestamp=str(records[-1].get("timestamp", "")) if records else "",
    )
