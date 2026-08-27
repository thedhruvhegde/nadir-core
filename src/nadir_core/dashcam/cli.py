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
    return open_source("synthetic", n_frames=36, yaw_drift_deg=yaw, roll_drift_deg=0.4)


def _run_analyze(args) -> int:
    cfg = DashcamConfig.from_env(
        vehicle_id=args.vehicle_id,
        store_path=args.store,
        api_url=args.api_url,
    )
    agent = DashcamAgent(cfg)
    src = _source_from_args(args)
    series = agent.run(src.frames(), upload=bool(args.upload))
    summary = series.summary()
    last = series.latest()
    if args.json:
        print(json.dumps({"summary": summary, "last": last.as_dict() if last else None}, indent=2))
    else:
        print(json.dumps(summary, indent=2))
        if last:
            print(last.explanation)
    return 0


def _run_report(args) -> int:
    cfg = DashcamConfig.from_env(store_path=args.store)
    from nadir_core.dashcam.store import JsonlStore

    rows = JsonlStore(cfg.store_path).read_all()
    if args.json:
        print(json.dumps({"n": len(rows), "rows": rows[-20:]}, indent=2))
    else:
        print(f"samples={len(rows)} store={cfg.store_path}")
        if rows:
            print(json.dumps(rows[-1], indent=2))
    return 0


def _run_connect(args) -> int:
    if args.brand == "viofo":
        print("VIOFO A229: enable Wi-Fi station or join camera hotspot")
        print("browse http://<cam-ip>/DCIM/Movie or use nadir-dashcam analyze --source viofo --host <ip>")
        print("SD card / viofosync folder also works: --source folder --path ./recordings")
    else:
        print("BlackVue: join camera Wi-Fi (often 10.99.77.1)")
        print("live: http://10.99.77.1/blackvue_live.cgi")
        print("nadir-dashcam analyze --source blackvue --host 10.99.77.1")
    print("video stays local by default; --upload only sends anonymized score JSON")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.cmd in ("analyze", "watch"):
        return _run_analyze(args)
    if args.cmd == "report":
        return _run_report(args)
    if args.cmd == "connect":
        return _run_connect(args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
