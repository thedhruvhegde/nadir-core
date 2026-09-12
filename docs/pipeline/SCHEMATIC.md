# Pipeline schematic

Generated technical view of the **nadir-core 0.2** dashcam → Pulse path.

## End-to-end

```mermaid
flowchart TB
  subgraph sources [Sources]
    SYN[SyntheticSource]
    FLD[FolderSource_SD]
    VIO[ViofoHTTP]
    BV[BlackVueMJPEG]
    RT[RTSP]
  end

  subgraph frames [Frame path]
    FP[FramePacket]
    RSZ[resize_max]
    GRAY[to_gray]
  end

  subgraph vision [Vision measurements]
    HZ[horizon_roll_pitch]
    VP[vanishing_yaw]
    RANSAC[ransac_vanishing_point]
    FLOW[flow_yaw_rate]
  end

  subgraph filter [Temporal filter]
    HUB[Huber_window]
    EKF[MountEKF_6state]
    HMM[MountHMM_optional]
  end

  subgraph novel [Novel residuals]
    IGMR[IGMR_FisherRao]
    LIC[LI_CUSUM_SO3]
    SCE[SoftCouplingEnergy]
  end

  subgraph pulse [Pulse brain]
    BR[vision_to_readings]
    SP[score_pulse]
    TIER[NOMINAL_CAUTION_CRITICAL]
  end

  subgraph out [Outputs]
    HS[HealthSeries]
    JSONL[JsonlStore]
    REP[text_report]
    UP[optional_score_upload]
  end

  SYN --> FP
  FLD --> FP
  VIO --> FP
  BV --> FP
  RT --> FP
  FP --> RSZ --> GRAY
  GRAY --> HZ
  GRAY --> VP
  GRAY --> RANSAC
  GRAY --> FLOW
  HZ --> HUB
  VP --> HUB
  RANSAC --> HUB
  FLOW --> HUB
  HUB --> EKF
  EKF --> HMM
  EKF --> IGMR
  EKF --> LIC
  EKF --> SCE
  SCE --> BR
  IGMR --> HS
  LIC --> HS
  BR --> SP --> TIER --> HS
  HS --> JSONL
  HS --> REP
  HS --> UP
```

## Module map

| Stage | Primary modules |
|-------|-----------------|
| Ingest | `dashcam/sources/*`, `dashcam/ingest/*` |
| Vision | `dashcam/vision/*`, `dashcam/features/*` |
| Geometry | `dashcam/geometry/lie_so3.py`, `homography.py` |
| Filters | `dashcam/filters/ekf_mount.py`, `robust_stats.py` |
| Novel math | `dashcam/math_novel/*` + `docs/proofs/*` |
| Score | `dashcam/bridge.py` → `scoring/pulse.py` |
| Agent CLI | `dashcam/agent.py`, `dashcam/cli.py` |

## Data contracts

- **In:** BGR/`uint8` frames or synthetic arrays; optional NMEA speed.
- **Mid:** `MountEstimate` (yaw/pitch/roll deg, confidence, notes).
- **Out:** `HealthSample` JSONL; Pulse `DriftTier`; optional upload JSON with `claim_boundary=vision_mount_health_only`.

## Failure modes (by design)

```mermaid
flowchart LR
  noCam[no_camera] --> synth[use_synthetic]
  noReq[missing_requests] --> folder[folder_or_fixture_tests]
  chartSing[chart_singularity] --> lieGuard[LI_term_in_IGMR]
  cold[cold_baseline] --> wait[first_N_frames_learn]
```
