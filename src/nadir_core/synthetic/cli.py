"""CLI for synthetic telemetry generation."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from .generator import SyntheticTelemetryGenerator
from .types import GenerationConfig, ScenarioId


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate synthetic NADIR telemetry JSONL datasets.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_repo_root() / "NADIR_SDK" / "data" / "telemetry" / "generated",
        help="Base output directory (default: NADIR_SDK/data/telemetry/generated)",
    )
    parser.add_argument(
        "--scenarios",
        nargs="+",
        default=["all"],
        help=f"Scenario ids or 'all'. Choices: {', '.join(s.value for s in ScenarioId)}",
    )
    parser.add_argument("--frames", type=int, default=120, help="Frames per scenario")
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="Combined fleet mode: write run_id/frames.jsonl with this many total frames",
    )
    parser.add_argument(
        "--combined-only",
        action="store_true",
        help="With --count, skip per-scenario JSONL files (faster for large runs)",
    )
    parser.add_argument("--hz", type=float, default=10.0, help="Sample rate in Hz")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--run-id", default=None, help="Output subdirectory name")
    parser.add_argument("--vehicle-prefix", default="SYN-GEN", help="Vehicle id prefix")
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip JSON Schema validation (faster; not recommended)",
    )
    parser.add_argument(
        "--no-score",
        action="store_true",
        help="Skip per-frame drift scoring in summary metadata",
    )
    return parser


def resolve_scenarios(raw: list[str]) -> tuple[ScenarioId, ...]:
    if len(raw) == 1 and raw[0].lower() == "all":
        return ScenarioId.all()
    return tuple(ScenarioId.from_string(item) for item in raw)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    scenarios = resolve_scenarios(args.scenarios)
    start = datetime.now(timezone.utc)

    config = GenerationConfig(
        output_dir=args.output_dir,
        scenarios=scenarios,
        frames_per_scenario=args.frames,
        sample_rate_hz=args.hz,
        seed=args.seed,
        vehicle_prefix=args.vehicle_prefix,
        start_time=start,
        run_id=args.run_id or start.strftime("%Y%m%dT%H%M%SZ"),
        validate_schema=not args.no_validate,
        score_frames=not args.no_score,
        combined_frame_count=args.count,
        write_per_scenario_jsonl=not args.combined_only,
    )

    generator = SyntheticTelemetryGenerator(config)
    if args.count is not None:
        result = generator.generate_combined_fleet()
    else:
        result = generator.generate_all()

    print(f"Generated {len(result.jsonl_paths)} outputs -> {result.output_dir}")
    if args.count is not None:
        combined = result.output_dir / "frames.jsonl"
        lines = combined.read_text(encoding="utf-8").strip().splitlines()
        print(f"  frames.jsonl: {len(lines)} schema-valid frames")
    for stats in result.summary.scenarios:
        tiers = ", ".join(f"{k}={v}" for k, v in stats.tier_distribution.items()) or "n/a"
        print(
            f"  {stats.scenario_id}: {stats.record_count} frames, "
            f"peak_cam={stats.peak_camera_drift_deg}°, tiers {{{tiers}}}"
        )
    print(f"Summary: {result.summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
