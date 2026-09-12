# Project status (nadir-core 0.2.0)

Last updated: 2026-09-11

## Version

| Field | Value |
|-------|-------|
| Package | `nadir-core` |
| Version | **0.2.0** (`nadir_core.__about__.__version__`) |
| Stage | public beta Open Core |
| License | Apache-2.0 |

## Progress

| Area | State | Notes |
|------|-------|-------|
| Pulse / Echo scoring | usable | numpy-only; CI green path |
| Dashcam ingest (folder / synthetic) | usable | needs `[dashcam]` extra for video decode |
| VIOFO HTTP client | beta | listing tested with fixtures; live cam TBD per firmware |
| BlackVue MJPEG | beta | unofficial local API |
| Vision mount tracker | beta | horizon + VP + flow + EKF + RANSAC |
| Novel residuals (IGMR, LI-CUSUM, SCE) | beta | proofs under `docs/proofs/` |
| Optional score upload | stub-ready | env-configured; video never default |
| Consumer mobile app | not started | out of scope for this repo |
| ASIL / OEM calib certificate | will not claim | see claim boundary |

## What works in CI today

- `pip install -e ".[dashcam,dev]"`
- full `pytest`
- `nadir-dashcam analyze --source synthetic`

## Known gaps

Tracked as GitHub issues on this repo (VIOFO firmware variance, cold-start baseline, live soak corpus, upload endpoint contract).
