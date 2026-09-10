# NADIR Core

**Open-source ADAS sensor drift scoring** — shadow-mode residuals, Pulse tiers, synthetic telemetry.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

> **Shadow mode. No ECU writes. Score first.**

NADIR Core is the open foundation of [NADIR](https://nadirai.net): a library that turns camera / radar / lidar disagreement into an actionable tier (`NOMINAL` → `CAUTION` → `CRITICAL`).

The commercial platform (Console, fleet digests, signed evidence workflows, OEM pilots) lives separately. This repo is for **developers, researchers, and builders** who want to run the math, generate synthetic fleets, and contribute.

## Why this exists

ADAS sensors drift after glass work, vibration, and thermal cycling — often with no dash warning. NADIR Core scores that drift from telemetry you already have (or synthetic data you generate here).

## Quick start

```bash
pip install -e ".[dev]"

# Score a simple yaw residual
nadir-core-score --yaw-deg 0.35

# Or from Python
python - <<'PY'
from nadir_core import SensorReadings, score_pulse
import math

def rot(yaw):
    r = math.radians(yaw); c,s = math.cos(r), math.sin(r)
    return [c,-s,0, s,c,0, 0,0,1]

result = score_pulse(
    vehicle_id="demo-1",
    sensors=SensorReadings(camera_rotation_matrix=rot(0.4)),
)
print(result.tier)
PY
```

## What’s included (Open Core)

| Module | What you get |
|--------|----------------|
| `nadir_core.scoring` | Echo residual engine + Pulse lane (Mahalanobis, adaptive σ, conformal-lite hooks) |
| `nadir_core.synthetic` | Scenario generators for yaw/pitch/radar-camera mismatch |
| `data/synthetic/` | Small fixture payloads |
| Schemas | Telemetry + residual-score JSON Schema drafts |

## What’s *not* in this repo (commercial)

- Fleet Console / CRITICAL queue / weekly digests  
- Org tenancy, auth, SSO, Stripe  
- Signed evidence workflow productization  
- OEM / transit pilot kits and private validation corpora  

See the live scientific dossier: https://nadirai.net/technology/validation

## Contributing

Issues and PRs welcome. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

We especially want:

- New synthetic drift scenarios  
- Scoring tests on public datasets (KITTI pose → residual injection)  
- Docs / examples / notebook tutorials  
- Performance and numerical robustness fixes  

## Claim boundary

This library is a **research / developer prototype**. It is **not** ASIL / ISO 26262 certified and must not be used as an autonomous driving controller.

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).

## Links

- Product: https://nadirai.net  
- Validation: https://nadirai.net/technology/validation  
- Founders: founders@nadirai.net  
