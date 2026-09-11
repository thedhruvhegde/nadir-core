from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, List, Optional
import math

@dataclass
class GpsFix:
    lat: float; lon: float; speed_knots: float=0.0; course_deg: float=0.0; t_s: float=0.0

    @property
    def speed_mps(self) -> float:
        return self.speed_knots * 0.514444

def _nmea_checksum_ok(sentence: str) -> bool:
    if '!' not in sentence and not sentence.startswith('$'): return False
    try:
        body, csum = sentence.strip()[1:].split('*')
        x = 0
        for ch in body:
            x ^= ord(ch)
        return f'{x:02X}' == csum.upper()
    except Exception:
        return False

def parse_rmc(sentence: str) -> Optional[GpsFix]:
    if not sentence.startswith('$') or 'RMC' not in sentence: return None
    parts = sentence.split(',')
    if len(parts) < 9 or parts[2] == 'V': return None
    def dm_to_deg(dm, hemi):
        if not dm: return 0.0
        dm = float(dm); d = int(dm//100); m = dm - d*100
        deg = d + m/60.0
        return -deg if hemi in ('S','W') else deg
    lat = dm_to_deg(parts[3], parts[4]); lon = dm_to_deg(parts[5], parts[6])
    spd = float(parts[7] or 0.0); course = float(parts[8] or 0.0)
    return GpsFix(lat, lon, spd, course)

def haversine_m(a: GpsFix, b: GpsFix) -> float:
    R=6371000.0
    p1,p2=math.radians(a.lat),math.radians(b.lat)
    dp=p2-p1; dl=math.radians(b.lon-a.lon)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(min(1.0, math.sqrt(h)))

def synthesize_nmea_track_0(n: int = 20, lat0: float = 40.00000, lon0: float = -74.00000, speed_kts: float = 10) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_1(n: int = 21, lat0: float = 40.01000, lon0: float = -74.01000, speed_kts: float = 11) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_2(n: int = 22, lat0: float = 40.02000, lon0: float = -74.02000, speed_kts: float = 12) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_3(n: int = 23, lat0: float = 40.03000, lon0: float = -74.03000, speed_kts: float = 13) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_4(n: int = 24, lat0: float = 40.04000, lon0: float = -74.04000, speed_kts: float = 14) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_5(n: int = 25, lat0: float = 40.05000, lon0: float = -74.05000, speed_kts: float = 15) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_6(n: int = 26, lat0: float = 40.06000, lon0: float = -74.06000, speed_kts: float = 16) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_7(n: int = 27, lat0: float = 40.07000, lon0: float = -74.07000, speed_kts: float = 17) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_8(n: int = 28, lat0: float = 40.08000, lon0: float = -74.08000, speed_kts: float = 18) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_9(n: int = 29, lat0: float = 40.09000, lon0: float = -74.09000, speed_kts: float = 19) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_10(n: int = 30, lat0: float = 40.10000, lon0: float = -74.10000, speed_kts: float = 20) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_11(n: int = 31, lat0: float = 40.11000, lon0: float = -74.11000, speed_kts: float = 21) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_12(n: int = 32, lat0: float = 40.12000, lon0: float = -74.12000, speed_kts: float = 22) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_13(n: int = 33, lat0: float = 40.13000, lon0: float = -74.13000, speed_kts: float = 23) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_14(n: int = 34, lat0: float = 40.14000, lon0: float = -74.14000, speed_kts: float = 24) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_15(n: int = 35, lat0: float = 40.15000, lon0: float = -74.15000, speed_kts: float = 10) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_16(n: int = 36, lat0: float = 40.16000, lon0: float = -74.16000, speed_kts: float = 11) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_17(n: int = 37, lat0: float = 40.17000, lon0: float = -74.17000, speed_kts: float = 12) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_18(n: int = 38, lat0: float = 40.18000, lon0: float = -74.18000, speed_kts: float = 13) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_19(n: int = 39, lat0: float = 40.19000, lon0: float = -74.19000, speed_kts: float = 14) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_20(n: int = 40, lat0: float = 40.20000, lon0: float = -74.20000, speed_kts: float = 15) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_21(n: int = 41, lat0: float = 40.21000, lon0: float = -74.21000, speed_kts: float = 16) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_22(n: int = 42, lat0: float = 40.22000, lon0: float = -74.22000, speed_kts: float = 17) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_23(n: int = 43, lat0: float = 40.23000, lon0: float = -74.23000, speed_kts: float = 18) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_24(n: int = 44, lat0: float = 40.24000, lon0: float = -74.24000, speed_kts: float = 19) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_25(n: int = 45, lat0: float = 40.25000, lon0: float = -74.25000, speed_kts: float = 20) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_26(n: int = 46, lat0: float = 40.26000, lon0: float = -74.26000, speed_kts: float = 21) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_27(n: int = 47, lat0: float = 40.27000, lon0: float = -74.27000, speed_kts: float = 22) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_28(n: int = 48, lat0: float = 40.28000, lon0: float = -74.28000, speed_kts: float = 23) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_29(n: int = 49, lat0: float = 40.29000, lon0: float = -74.29000, speed_kts: float = 24) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_30(n: int = 50, lat0: float = 40.30000, lon0: float = -74.30000, speed_kts: float = 10) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_31(n: int = 51, lat0: float = 40.31000, lon0: float = -74.31000, speed_kts: float = 11) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_32(n: int = 52, lat0: float = 40.32000, lon0: float = -74.32000, speed_kts: float = 12) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_33(n: int = 53, lat0: float = 40.33000, lon0: float = -74.33000, speed_kts: float = 13) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_34(n: int = 54, lat0: float = 40.34000, lon0: float = -74.34000, speed_kts: float = 14) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_35(n: int = 55, lat0: float = 40.35000, lon0: float = -74.35000, speed_kts: float = 15) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_36(n: int = 56, lat0: float = 40.36000, lon0: float = -74.36000, speed_kts: float = 16) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_37(n: int = 57, lat0: float = 40.37000, lon0: float = -74.37000, speed_kts: float = 17) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_38(n: int = 58, lat0: float = 40.38000, lon0: float = -74.38000, speed_kts: float = 18) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_39(n: int = 59, lat0: float = 40.39000, lon0: float = -74.39000, speed_kts: float = 19) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_40(n: int = 60, lat0: float = 40.40000, lon0: float = -74.40000, speed_kts: float = 20) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_41(n: int = 61, lat0: float = 40.41000, lon0: float = -74.41000, speed_kts: float = 21) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_42(n: int = 62, lat0: float = 40.42000, lon0: float = -74.42000, speed_kts: float = 22) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_43(n: int = 63, lat0: float = 40.43000, lon0: float = -74.43000, speed_kts: float = 23) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_44(n: int = 64, lat0: float = 40.44000, lon0: float = -74.44000, speed_kts: float = 24) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_45(n: int = 65, lat0: float = 40.45000, lon0: float = -74.45000, speed_kts: float = 10) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_46(n: int = 66, lat0: float = 40.46000, lon0: float = -74.46000, speed_kts: float = 11) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_47(n: int = 67, lat0: float = 40.47000, lon0: float = -74.47000, speed_kts: float = 12) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_48(n: int = 68, lat0: float = 40.48000, lon0: float = -74.48000, speed_kts: float = 13) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out

def synthesize_nmea_track_49(n: int = 69, lat0: float = 40.49000, lon0: float = -74.49000, speed_kts: float = 14) -> List[str]:
        out=[]
        for t in range(n):
            lat = lat0 + t * 0.0001
            lon = lon0 + t * 0.00012
            # simplified RMC without strict checksum for sim
            out.append(f'$GPRMC,0000{t:02d}.00,A,{int(lat)*100+(lat-int(lat))*60:.4f},N,{abs(int(lon))*100+(abs(lon)-abs(int(lon)))*60:.4f},W,{speed_kts:.1f},90.0,010125,,,A*00')
        return out
