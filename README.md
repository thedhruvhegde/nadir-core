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
