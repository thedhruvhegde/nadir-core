from __future__ import annotations

from typing import Iterator, Optional

from nadir_core.dashcam.bridge import score_mount_estimate
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.health import HealthSample, HealthSeries
from nadir_core.dashcam.store import JsonlStore
from nadir_core.dashcam.types import FramePacket
from nadir_core.dashcam.upload import upload_sample
from nadir_core.dashcam.vision.explain import explain_mount
from nadir_core.dashcam.vision.mount import MountTracker


class DashcamAgent:
    def __init__(self, config: Optional[DashcamConfig] = None) -> None:
        self.config = config or DashcamConfig.from_env()
        self.tracker = MountTracker(max_width=self.config.max_width)
        self.series = HealthSeries()
        self.store = JsonlStore(self.config.store_path)

    def process_frame(self, packet: FramePacket) -> HealthSample:
        est = self.tracker.update(packet)
        result = score_mount_estimate(self.config.vehicle_id, est)
        explanation = explain_mount(est, result.tier)
        sample = HealthSample(
            timestamp_s=packet.timestamp_s,
            estimate=est,
            tier=result.tier,
            mahal=float(result.mahal_distance),
            health_score=float(result.health_score),
            explanation=explanation,
        )
        self.series.add(sample)
        self.store.append(sample)
        return sample

    def run(self, frames: Iterator[FramePacket], *, upload: bool = False) -> HealthSeries:
        for packet in frames:
            sample = self.process_frame(packet)
            if upload and self.config.api_url:
                upload_sample(
                    self.config.api_url,
                    self.config.vehicle_id,
                    sample,
                    token=self.config.api_token(),
                )
        return self.series
