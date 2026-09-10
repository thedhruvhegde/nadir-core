# Contributing to NADIR Core

Thanks for helping build open ADAS drift tooling.

## Dev setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## Guidelines

1. **Keep Open Core open** — no secrets, no private fleet data, no customer PII.
2. **Small PRs** — one idea per pull request.
3. **Tests** — add or update `tests/` for scoring or synthetic changes.
4. **Claim boundary** — do not imply ASIL certification or ECU actuation.

## Project layout

```
src/nadir_core/scoring/     # residual + Pulse scoring
src/nadir_core/synthetic/   # telemetry generators
examples/                   # runnable demos
tests/                      # pytest
```

## Commercial contributions

If you need fleet Console, evidence workflows, or OEM pilots, email founders@nadirai.net — that product is separate from this Apache-2.0 core.
