from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from nadir_core.dashcam.agent import DashcamAgent
from nadir_core.dashcam.config import DashcamConfig
from nadir_core.dashcam.sources import open_source


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nadir-dashcam",
        description="Vision mount health from dashcam footage (shadow mode, local-first)",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_common(sp):
        sp.add_argument("--vehicle-id", default=None)
        sp.add_argument("--store", default=None)
        sp.add_argument("--upload", action="store_true")
        sp.add_argument("--api-url", default=None)
        sp.add_argument("--json", action="store_true")

    a = sub.add_parser("analyze", help="Analyze a source once")
    a.add_argument("--source", required=True, choices=["folder", "viofo", "blackvue", "rtsp", "synthetic"])
    a.add_argument("--path", default=None, help="folder path")
    a.add_argument("--host", default=None, help="viofo/blackvue host")
    a.add_argument("--url", default=None, help="rtsp url")
    a.add_argument("--yaw-drift", type=float, default=0.8, help="synthetic yaw drift deg")
    add_common(a)

    w = sub.add_parser("watch", help="Same as analyze (hybrid loop entrypoint)")
    w.add_argument("--source", required=True, choices=["folder", "viofo", "blackvue", "rtsp", "synthetic"])
    w.add_argument("--path", default=None)
    w.add_argument("--host", default=None)
    w.add_argument("--url", default=None)
    add_common(w)

    r = sub.add_parser("report", help="Summarize local jsonl store")
    r.add_argument("--store", default=None)
    r.add_argument("--json", action="store_true")

    c = sub.add_parser("connect", help="Print connection hints for VIOFO / BlackVue")
    c.add_argument("--brand", default="viofo", choices=["viofo", "blackvue"])

    return p


def _source_from_args(args):
    kind = args.source
    if kind == "folder":
        if not args.path:
            raise SystemExit("--path required for folder source")
        return open_source("folder", root=args.path)
    if kind == "viofo":
        host = args.host or "192.168.1.1"
        return open_source("viofo", host=host)
    if kind == "blackvue":
        host = args.host or "10.99.77.1"
        return open_source("blackvue", host=host)
    if kind == "rtsp":
        if not args.url:
            raise SystemExit("--url required for rtsp")
        return open_source("rtsp", url=args.url)
    yaw = getattr(args, "yaw_drift", 0.8)
