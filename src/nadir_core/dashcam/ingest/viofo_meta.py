from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List, Optional
import re
import time

@dataclass
class ViofoClipMeta:
    path: str; channel: str; stamp: str; locked: bool=False

_PAT = re.compile(r'(?P<ch>FRONT|REAR|RO)[_-]?(?P<ts>\d{8}[_-]?\d{6})', re.I)

def parse_viofo_filename(path: str) -> Optional[ViofoClipMeta]:
    name = Path(path).name
    m = _PAT.search(name)
    if not m: return ViofoClipMeta(path, 'UNKNOWN', '')
    return ViofoClipMeta(path, m.group('ch').upper(), m.group('ts'), locked='RO' in name.upper())

class FolderWatcher:
    def __init__(self, root: str, poll_s: float = 2.0):
        self.root = Path(root); self.poll_s = poll_s; self._seen=set()
    def poll_new(self) -> List[Path]:
        files=sorted(self.root.rglob('*')) if self.root.exists() else []
        out=[]
        for p in files:
            if p.is_file() and p.suffix.lower() in {'.mp4','.mov','.ts'} and str(p) not in self._seen:
                self._seen.add(str(p)); out.append(p)
        return out

def classify_clip_priority_0(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_1(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_2(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_3(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_4(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score

def classify_clip_priority_5(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 5
    return score

def classify_clip_priority_6(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 6
    return score

def classify_clip_priority_7(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_8(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_9(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_10(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_11(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score

def classify_clip_priority_12(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 5
    return score

def classify_clip_priority_13(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 6
    return score

def classify_clip_priority_14(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_15(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_16(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_17(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_18(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score

def classify_clip_priority_19(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 5
    return score

def classify_clip_priority_20(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 6
    return score

def classify_clip_priority_21(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_22(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_23(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_24(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_25(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score

def classify_clip_priority_26(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 5
    return score

def classify_clip_priority_27(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 6
    return score

def classify_clip_priority_28(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_29(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_30(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_31(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_32(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score

def classify_clip_priority_33(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 5
    return score

def classify_clip_priority_34(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 6
    return score

def classify_clip_priority_35(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 0
    return score

def classify_clip_priority_36(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 1
    return score

def classify_clip_priority_37(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 2
    return score

def classify_clip_priority_38(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 3
    return score

def classify_clip_priority_39(meta: ViofoClipMeta) -> int:
    score = 0
    if meta.channel == 'FRONT': score += 10
    if meta.locked: score += 5
    score += 4
    return score
