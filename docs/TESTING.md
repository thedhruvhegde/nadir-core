# Testing

## How we run tests

```bash
pip install -e ".[dashcam,dev]"
pytest -q
nadir-dashcam analyze --source synthetic --yaw-drift 1.2 --store /tmp/t.jsonl
```

CI (`.github/workflows/ci.yml`) installs the same extras on Python 3.11 and 3.12, runs pytest, then a synthetic CLI smoke.

## What is covered today

| Suite | What it checks |
|-------|----------------|
| `tests/test_score_pulse.py` | Pulse scoring smoke |
| `tests/dashcam/test_vision.py` | horizon / vanishing / clamp |
| `tests/dashcam/test_viofo.py` | HTML + XML listing parsers (mocked session) |
| `tests/dashcam/test_agent.py` | end-to-end synthetic agent + bridge + upload payload shape |
| `tests/dashcam/test_pipeline_depth.py` | deeper pipeline + report text |
| `tests/dashcam/geometry/test_lie.py` | SO(3) exp/log, rpy, geodesic |
| `tests/dashcam/filters/test_ekf.py` | mount EKF update |
| `tests/dashcam/analytics/test_spectral_trips.py` | Welch PSD + trip segmentation |
| `tests/dashcam/math_novel/` | IGMR / LI-CUSUM / SCE unit checks |

## Testing we have done (lab notes)

1. **Synthetic soak** — `SyntheticSource` with yaw drift 0.8–2.0° over 12–36 frames; agent returns `n` matching frame count; explanations include claim boundary string.
2. **Fixture VIOFO listings** — checked HTML scrape and XML `cmd=3015` path without a physical camera.
3. **Lie round-trip** — random so3_exp/so3_log errors under 1e-8.
4. **EKF** — measurement pull moves state away from zero.
5. **CI regression** — previously failed when only `[dev]` was installed (missing `requests`) and when `robust_mahalanobis` imported private `nadir_sdk`; both fixed in 0.2.0.

## Not yet tested in CI (tracked as issues)

- Live A229 on station Wi‑Fi across firmware builds
- BlackVue on-car MJPEG longevity
- Large MP4 folder performance / memory
- Upload against a real `NADIR_API_URL`
