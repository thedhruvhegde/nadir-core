# NADIR Core

**Open-source ADAS drift scoring + free dashcam mount-health agent.**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

> Shadow mode. No ECU writes. Score first. Video stays local by default.

NADIR Core is the public Open Core of [NADIR](https://nadirai.net). It has two layers that share one scoring brain (`score_pulse`):

1. **Pulse / Echo** — residual scoring when you already have camera / radar / lidar / IMU-style telemetry.
2. **Dashcam agent** — if you only have a consumer dashcam (especially **VIOFO A229** in the US), we estimate **mount / horizon / ego-motion geometry health** from video and bridge those estimates into Pulse tiers.

Commercial Console, digests, signed evidence, and fleet pilots stay private. This repo is for developers, researchers, and builders.

---

## Does this actually work?

**Yes, as a local shadow-mode prototype:**

| Path | Status |
|------|--------|
| Synthetic road frames → mount estimate → Pulse tier | Working (`nadir-dashcam analyze --source synthetic`) |
| Folder of MP4/JPG clips | Working with `opencv-python-headless` |
| VIOFO HTTP listing (station / hotspot) | Client + fixtures tested; needs your camera on LAN |
| BlackVue MJPEG live | Client implemented against public unofficial endpoints |
| RTSP | OpenCV capture wrapper |

It will **not** magically diagnose your OEM radar from dashcam pixels. That claim would be false. What it *does* is detect **camera mounting / scene-geometry inconsistency** (yaw/pitch/roll proxies, vibration bands, gradual drift) and score them with the same Pulse tiering used for multi-sensor residuals.

Run the smoke path:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dashcam,dev]"
nadir-dashcam analyze --source synthetic --yaw-drift 1.2
pytest -q
```

You should see a JSON summary (`n`, `last_tier`, health score) and a one-line explanation that includes the claim boundary.

---

## What math is in here? (honest)

This is **not** a single new PhD theorem. It is a **composed classical stack** wired for a product problem:

**Dashcam vision / geometry**

- Horizon band energy + roll from gradient orientation
- Vanishing-structure yaw proxy + **RANSAC vanishing point** over edge line hypotheses
- Coarse / **pyramidal Lucas–Kanade** flow → yaw-rate proxy
- **SO(3) / SE(3) Lie helpers** (exp/log, left Jacobians)
- **DLT + RANSAC homography**, Brown–Conrady intrinsics
- **6-state mount EKF** (+ multi-hypothesis bank) over roll/pitch/yaw and rates
- Robust M-estimators (Huber/Tukey/… IRLS), Welch PSD vibration bands
- Page–Hinkley / MEWMA change detectors, split conformal interval helpers
- Trip segmentation from speed + yaw/roll series

**Pulse scoring (existing Open Core brain)**

- Mahalanobis residual fusion, adaptive σ, robust covariance hooks
- Cross-modal gates, CUSUM / gradual-slope style alerts
- Tiering: `NOMINAL` → `CAUTION` → `CRITICAL`

The novelty for NADIR as a company is the **product composition + claim boundary**: consumer dashcam soak → Pulse-compatible scores → optional anonymized upload → commercial pilots elsewhere — not “we invented geometry.”

---

## Install

```bash
git clone https://github.com/thedhruvhegde/nadir-core.git
cd nadir-core
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"           # scoring only (numpy)
pip install -e ".[dashcam,dev]"   # + opencv-headless, requests
```

Python **3.9+**. macOS / Linux primary; Windows should work for folder + synthetic.

---

## Quick start — scoring only

```bash
nadir-core-score --yaw-deg 0.35
```

```python
from nadir_core import SensorReadings, score_pulse
import math

def rot(yaw):
    r = math.radians(yaw); c,s = math.cos(r), math.sin(r)
    return [c,-s,0, s,c,0, 0,0,1]

print(score_pulse("demo", SensorReadings(camera_rotation_matrix=rot(0.4))).tier)
```

---

## Quick start — dashcam agent (the free public tool)

### A) No hardware (sanity)

```bash
nadir-dashcam connect --brand viofo
nadir-dashcam analyze --source synthetic --yaw-drift 1.5 --store out/demo.jsonl
nadir-dashcam report --store out/demo.jsonl
```

### B) VIOFO A229 / A229 Pro / Plus (recommended US volume path)

1. Update camera firmware from VIOFO’s site.
2. Either:
   - **Hotspot:** long-press Wi‑Fi, join `VIOFO-…` from the laptop/phone that will run the agent, or
   - **Station mode:** join the camera to your home/car Wi‑Fi (see VIOFO docs; some firmware needs support build to persist station mode).
3. Find the camera IP (router client list, or VIOFO app / screen).
4. Soft-check in a browser: `http://<cam-ip>/DCIM/Movie`
5. Run:

```bash
nadir-dashcam analyze --source viofo --host <cam-ip> --vehicle-id my-car --store out/my-car.jsonl
```

Hardwire kit (e.g. HK4) helps for parking / post-drive sync. For “after I park” workflows, also use [viofosync](https://github.com/jusii/viofosync)-style folder sync, then:

```bash
nadir-dashcam analyze --source folder --path ~/Dashcam/Movie
```

### C) Any brand via microSD / synced folder

```bash
# copy clips off the SD card, or sync with your favorite tool
nadir-dashcam analyze --source folder --path /Volumes/DASHCAM/DCIM/Movie
```

### D) BlackVue live (unofficial local Wi‑Fi API)

Join the camera AP (often `10.99.77.1`), then:

```bash
nadir-dashcam analyze --source blackvue --host 10.99.77.1
```

Live endpoint used: `/blackvue_live.cgi` (MJPEG). VOD list: `/blackvue_vod.cgi`.

### E) RTSP (firmware-dependent)

```bash
nadir-dashcam analyze --source rtsp --url rtsp://<cam-ip>/
```

### Optional anonymized score upload

Video is **not** uploaded by default. To POST score JSON only:

```bash
export NADIR_API_URL="https://your-endpoint.example/v1/dashcam-scores"
export NADIR_API_TOKEN="…"
nadir-dashcam analyze --source synthetic --upload --api-url "$NADIR_API_URL"
```

Payload includes `claim_boundary: vision_mount_health_only`.

---

## Hybrid realtime model

```
live stream reachable? ──yes──► frame loop → EKF mount → Pulse → JSONL
         │
         no
         ▼
   watch folder / SD sync → same pipeline on new clips
```

True on-drive realtime usually means the laptop/phone stays associated to the camera hotspot or a car Wi‑Fi. Home station sync analyzes after parking. Both are first-class.

---

## Project layout

```
src/nadir_core/
  scoring/          Pulse / Echo residual brain
  dashcam/
    sources/        folder, viofo, blackvue, rtsp, synthetic
    vision/         horizon, vanishing, flow, mount tracker
    geometry/       SO(3)/SE(3), homography, road plane
    filters/        mount EKF, robust stats, hypothesis bank
    features/       RANSAC VP, pyramid LK, illumination
    analytics/      spectral, trips, conformal helpers, reports
    ingest/         NMEA/GPS, VIOFO meta, BlackVue proto
    calib/          Brown–Conrady intrinsics
    sim/            scenario library
  synthetic/        telemetry generators for Pulse demos
docs/DASHCAM.md     short boundary + commands
docs/dashcam/       deeper guides
```

---

## Claim boundary (read this)

- Not ASIL / ISO 26262.
- Not an ECU writer / ADAS calibrator certificate.
- Dashcam path = **vision mount / geometry health** bridged into Pulse.
- Do not tell customers “we measured your radar bias from a VIOFO.”

Fuller notes: [`docs/DASHCAM.md`](docs/DASHCAM.md), [`docs/dashcam/SETUP.md`](docs/dashcam/SETUP.md), [`docs/dashcam/MATH.md`](docs/dashcam/MATH.md).

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Highest-value PRs: new brand adapters, on-road fixture clips (with privacy scrubbing), numerical tests, docs for specific VIOFO firmware quirks.

## License

Apache-2.0 — [`LICENSE`](LICENSE).

## Links

- Product: https://nadirai.net
- Validation dossier: https://nadirai.net/technology/validation
- Issues: https://github.com/thedhruvhegde/nadir-core/issues
- Founders: founders@nadirai.net
