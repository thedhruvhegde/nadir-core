# Dashcam setup guide

## Goal

Get from zero → first Pulse tier from your car’s dashcam without touching the ECU.

## Pick a connection mode

### 1. Folder / SD (works for every brand)

1. Park, remove microSD (or use a reader / wireless sync tool).
2. Copy `DCIM/Movie` (VIOFO) or `Record` (BlackVue) to a folder.
3. `nadir-dashcam analyze --source folder --path /path/to/clips`

Pros: reliable, privacy-simple. Cons: not live.

### 2. VIOFO Wi‑Fi hotspot

1. Long-press Wi‑Fi on the camera until SSID appears.
2. Join that SSID from the machine running NADIR (your phone’s internet will drop — expected).
3. Find IP (often shown in app; try router-less link-local scanning or VIOFO docs for your firmware).
4. Open `http://IP/DCIM/Movie` in a browser.
5. `nadir-dashcam analyze --source viofo --host IP`

### 3. VIOFO station mode (home / shop LAN)

1. Enable station mode per VIOFO guide.
2. Reserve a DHCP lease for the camera.
3. When the car is in range and powered (hardwire kit recommended), run the same `viofo` source against the reserved IP.
4. Or run viofosync → folder mode overnight.

### 4. BlackVue

1. Join camera Wi‑Fi.
2. Confirm `http://10.99.77.1/blackvue_live.cgi` returns a stream.
3. `nadir-dashcam analyze --source blackvue --host 10.99.77.1`

## Interpreting output

- `NOMINAL` — geometry near local baseline.
- `CAUTION` — mounting yaw/pitch/roll proxies drifting; schedule a physical check.
- `CRITICAL` — large inconsistency; do not treat as OEM calibration proof — treat as “look at the mount / windshield work.”

Baselines form after the first several frames/clips on a vehicle_id. Delete the JSONL store to reset.

## Privacy

- Default store: local JSONL only.
- `--upload` sends anonymized scores, not video.
- Strip cabin-facing audio/video before sharing fixtures in PRs.
