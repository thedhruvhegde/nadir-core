# Math notes (dashcam lane)

## State we estimate

Mount state `x = [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate]` in a local camera frame relative to a learned baseline.

## Measurements

1. Horizon detector — pitch/roll proxies from row-energy and gradient orientation.
2. Vanishing / lane structure — yaw proxy; RANSAC over line hypotheses rejects outliers.
3. Optical flow (pyramidal LK / coarse block match) — yaw-rate proxy.
4. Optional GPS speed (NMEA RMC) — trip segmentation and process-noise scheduling.

## Filter

Linear-Gaussian EKF prediction with a constant-velocity angle model; measurement update on roll/pitch/yaw. A multi-hypothesis bank reweights by innovation Mahalanobis likelihood.

## Scoring bridge

Estimated yaw/pitch (deg) map to `camera_rotation_matrix` via yaw then pitch rotations; roll leaks lightly into a radar-azimuth proxy so Pulse sees cross-signal tension. Then `score_pulse` applies Mahalanobis tiering.

## What is not claimed

We do not recover OEM extrinsics or radar boresight from monocular dashcam video alone. Uncertainty helpers (conformal / jackknife+) bound vision residuals, not ISO 26262 compliance.
