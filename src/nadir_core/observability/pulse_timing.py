"""Pulse latency profiler — per-stage ms breakdown + 200 ms budget (P11)."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional


DEFAULT_PULSE_LATENCY_BUDGET_MS = 200.0


class PulseLatencyExceededError(RuntimeError):
    """Raised when Pulse scoring exceeds the configured latency budget."""

    def __init__(
        self,
        elapsed_ms: float,
        budget_ms: float,
        *,
        stages: Optional[List[Dict[str, float]]] = None,
    ) -> None:
        stage_hint = ""
        if stages:
            breakdown = ", ".join(f"{s['stage']}={s['ms']}ms" for s in stages[:6])
            stage_hint = f" stages=[{breakdown}]"
        super().__init__(
            f"Pulse scoring exceeded latency budget: {elapsed_ms:.3f}ms > {budget_ms:.3f}ms"
            f"{stage_hint}"
        )
        self.elapsed_ms = elapsed_ms
        self.budget_ms = budget_ms
        self.stages = list(stages or [])


@dataclass
class PulseLatencyProfiler:
    """Accumulates stage timings for Pulse v2 engine."""

    budget_ms: float = DEFAULT_PULSE_LATENCY_BUDGET_MS
    _started: float = field(default_factory=time.perf_counter)
    _last: float = field(default_factory=time.perf_counter)
    stages: List[Dict[str, float]] = field(default_factory=list)

    def mark(self, name: str) -> None:
        now = time.perf_counter()
        elapsed_ms = (now - self._last) * 1000.0
        self.stages.append({"stage": name, "ms": round(elapsed_ms, 3)})
        self._last = now

    def total_ms(self) -> float:
        return round((time.perf_counter() - self._started) * 1000.0, 3)

    def exceeds_budget(self) -> bool:
        return self.total_ms() > self.budget_ms

    def to_dict(self) -> Dict[str, object]:
        total = self.total_ms()
        return {
            "budget_ms": self.budget_ms,
            "total_ms": total,
            "within_budget": total <= self.budget_ms,
            "stages": list(self.stages),
        }


def check_pulse_latency_budget(
    profiler: Optional[PulseLatencyProfiler],
    *,
    raise_on_exceed: bool = True,
) -> Optional[Dict[str, object]]:
    """Return timing dict; optionally raise when budget exceeded."""
    if profiler is None:
        return None
    body = profiler.to_dict()
    if raise_on_exceed and profiler.exceeds_budget():
        raise PulseLatencyExceededError(
            profiler.total_ms(),
            profiler.budget_ms,
            stages=list(profiler.stages),
        )
    return body
