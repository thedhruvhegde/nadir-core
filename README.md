# NADIR Core

Open-source ADAS drift scoring, plus a free local dashcam agent that estimates
camera mount / geometry health and scores it with the same Pulse engine.

Version **0.2.0** (beta). Apache-2.0. Shadow mode only — no ECU writes.

Repo: https://github.com/thedhruvhegde/nadir-core · Product: https://nadirai.net

## Status in one paragraph

Pulse scoring works today on numpy telemetry. The dashcam lane works end-to-end on
synthetic frames and on folder / VIOFO / BlackVue adapters (live hardware depends
on your firmware and Wi‑Fi). Novel residuals (IGMR, LI-CUSUM, soft coupling) are
implemented with writeups under `docs/proofs/`. See [`docs/STATUS.md`](docs/STATUS.md)
and [`docs/TESTING.md`](docs/TESTING.md).

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dashcam,dev]"
pytest -q
nadir-dashcam analyze --source synthetic --yaw-drift 1.2
```

## Docs map

| Doc | Contents |
|-----|----------|
| [`docs/STATUS.md`](docs/STATUS.md) | version, progress table |
| [`docs/TESTING.md`](docs/TESTING.md) | suites + lab notes |
| [`docs/pipeline/SCHEMATIC.md`](docs/pipeline/SCHEMATIC.md) | pipeline schematic |
| [`docs/DASHCAM.md`](docs/DASHCAM.md) | dashcam quick use |
| [`docs/dashcam/SETUP.md`](docs/dashcam/SETUP.md) | VIOFO / BlackVue / folder setup |
| [`docs/dashcam/MATH.md`](docs/dashcam/MATH.md) | engineering math overview |
| [`docs/proofs/`](docs/proofs/) | IGMR / LI-CUSUM / SCE propositions |

## Install

```bash
git clone https://github.com/thedhruvhegde/nadir-core.git
cd nadir-core
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dashcam,dev]"   # scoring + dashcam
# or: pip install -e ".[dev]"     # scoring only
```

Needs Python 3.9+.

## Pulse scoring (telemetry you already have)

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

## Dashcam agent (free / local-first)

If you have a **VIOFO A229**-class camera (common on Amazon US), a synced SD folder,
BlackVue local Wi‑Fi, or RTSP:

```bash
nadir-dashcam connect --brand viofo
nadir-dashcam analyze --source synthetic --yaw-drift 1.5 --store out/demo.jsonl
nadir-dashcam analyze --source folder --path ./recordings
nadir-dashcam analyze --source viofo --host 192.168.1.50
nadir-dashcam analyze --source blackvue --host 10.99.77.1
nadir-dashcam report --store out/demo.jsonl
```

Hybrid behavior: analyze live when a stream is up; otherwise score clips as they
land after parking. Video stays on disk unless you pass `--upload` (score JSON only).

## Pipeline

Full schematic: [`docs/pipeline/SCHEMATIC.md`](docs/pipeline/SCHEMATIC.md).

Short version: frames → horizon / vanishing / flow → EKF → IGMR + LI-CUSUM + soft
coupling → `score_pulse` → JSONL / CLI.

## Math (including proofs)

We ship three NADIR-named formulations for the dashcam lane:

1. **IGMR** — information-geometric mount residual (Fisher–Rao + SO(3) guard)
2. **LI-CUSUM** — left-invariant CUSUM on SO(3) innovations
3. **SCE** — SPD soft-coupling energy into a Pulse-like scalar

Propositions and proofs: [`docs/proofs/`](docs/proofs/). Implementation:
`nadir_core.dashcam.math_novel`.

Classical pieces (RANSAC VP, pyramidal LK, Huber IRLS, Welch PSD) sit underneath.
None of this is an ASIL proof.

## Claim boundary

Dashcam pixels do not invent radar/lidar OEM residuals. This lane is **vision mount /
geometry health** bridged into Pulse. Not a calibration certificate. Not ASIL.

## What’s in / out of the public repo

**In:** Pulse/Echo scoring, dashcam agent, synthetic generators, schemas, proofs, CI.  
**Out:** Console, auth, digests, signed evidence product, customer data, transit/OEM packs.

## Contributing

[`CONTRIBUTING.md`](CONTRIBUTING.md). Useful PRs: brand adapters, scrubbed fixtures,
numerical tests, firmware-specific VIOFO notes.

## License

Apache-2.0 — [`LICENSE`](LICENSE).

## Contact

founders@nadirai.net · https://nadirai.net/technology/validation
