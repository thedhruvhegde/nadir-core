# Dashcam mount health (Open Core)

Free local agent: point at VIOFO / folder / BlackVue / RTSP, get shadow-mode
**vision mount / geometry health** bridged into Pulse tiers.

## Claim boundary

- This is **not** a multi-radar / lidar ADAS calibration certificate.
- Dashcam pixels cannot invent radar residuals. We estimate yaw/pitch/roll
  proxies from horizon, vanishing structure, and optical flow, then score
  them with the same Pulse lane used elsewhere in NADIR Core.
- Shadow mode only. No ECU writes. Not ASIL.
- Video stays on your machine by default. `--upload` sends anonymized JSON scores only.

## Quick start

```bash
pip install -e ".[dashcam,dev]"

# no camera required
nadir-dashcam analyze --source synthetic --yaw-drift 1.2

# VIOFO on LAN (station mode or hotspot)
nadir-dashcam connect --brand viofo
nadir-dashcam analyze --source viofo --host 192.168.1.50

# synced SD / viofosync folder
nadir-dashcam analyze --source folder --path ./recordings

# BlackVue live MJPEG
nadir-dashcam analyze --source blackvue --host 10.99.77.1
```

## Hybrid mode

When a live stream is reachable, analyze frames in near-real time. Otherwise
process clips as they land in a watch folder after parking. Same scoring path.

## Privacy

Local JSONL store defaults to `out/dashcam_health.jsonl`. Set `NADIR_API_URL`
and `NADIR_API_TOKEN` only if you want optional score upload.
