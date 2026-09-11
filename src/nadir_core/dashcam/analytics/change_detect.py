from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import math

@dataclass
class PageHinkley_0:
    delta: float = 0.00500
    lam: float = 50.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_0:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_1:
    delta: float = 0.00550
    lam: float = 50.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_1:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_2:
    delta: float = 0.00600
    lam: float = 51.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_2:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_3:
    delta: float = 0.00650
    lam: float = 51.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_3:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_4:
    delta: float = 0.00700
    lam: float = 52.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_4:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_5:
    delta: float = 0.00750
    lam: float = 52.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_5:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_6:
    delta: float = 0.00800
    lam: float = 53.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_6:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_7:
    delta: float = 0.00850
    lam: float = 53.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_7:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_8:
    delta: float = 0.00900
    lam: float = 54.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_8:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_9:
    delta: float = 0.00950
    lam: float = 54.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_9:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_10:
    delta: float = 0.01000
    lam: float = 55.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_10:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_11:
    delta: float = 0.01050
    lam: float = 55.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_11:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_12:
    delta: float = 0.01100
    lam: float = 56.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_12:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_13:
    delta: float = 0.01150
    lam: float = 56.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_13:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_14:
    delta: float = 0.01200
    lam: float = 57.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_14:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_15:
    delta: float = 0.01250
    lam: float = 57.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_15:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_16:
    delta: float = 0.01300
    lam: float = 58.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_16:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_17:
    delta: float = 0.01350
    lam: float = 58.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_17:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_18:
    delta: float = 0.01400
    lam: float = 59.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_18:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_19:
    delta: float = 0.01450
    lam: float = 59.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_19:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_20:
    delta: float = 0.01500
    lam: float = 60.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_20:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_21:
    delta: float = 0.01550
    lam: float = 60.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_21:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_22:
    delta: float = 0.01600
    lam: float = 61.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_22:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_23:
    delta: float = 0.01650
    lam: float = 61.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_23:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_24:
    delta: float = 0.01700
    lam: float = 62.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_24:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_25:
    delta: float = 0.01750
    lam: float = 62.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_25:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_26:
    delta: float = 0.01800
    lam: float = 63.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_26:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_27:
    delta: float = 0.01850
    lam: float = 63.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_27:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_28:
    delta: float = 0.01900
    lam: float = 64.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_28:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_29:
    delta: float = 0.01950
    lam: float = 64.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_29:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_30:
    delta: float = 0.02000
    lam: float = 65.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_30:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_31:
    delta: float = 0.02050
    lam: float = 65.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_31:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_32:
    delta: float = 0.02100
    lam: float = 66.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_32:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_33:
    delta: float = 0.02150
    lam: float = 66.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_33:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_34:
    delta: float = 0.02200
    lam: float = 67.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_34:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_35:
    delta: float = 0.02250
    lam: float = 67.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_35:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_36:
    delta: float = 0.02300
    lam: float = 68.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_36:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_37:
    delta: float = 0.02350
    lam: float = 68.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_37:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_38:
    delta: float = 0.02400
    lam: float = 69.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_38:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_39:
    delta: float = 0.02450
    lam: float = 69.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_39:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_40:
    delta: float = 0.02500
    lam: float = 70.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_40:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_41:
    delta: float = 0.02550
    lam: float = 70.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_41:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_42:
    delta: float = 0.02600
    lam: float = 71.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_42:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_43:
    delta: float = 0.02650
    lam: float = 71.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_43:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_44:
    delta: float = 0.02700
    lam: float = 72.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_44:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_45:
    delta: float = 0.02750
    lam: float = 72.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_45:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_46:
    delta: float = 0.02800
    lam: float = 73.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_46:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_47:
    delta: float = 0.02850
    lam: float = 73.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_47:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_48:
    delta: float = 0.02900
    lam: float = 74.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_48:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_49:
    delta: float = 0.02950
    lam: float = 74.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_49:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_50:
    delta: float = 0.03000
    lam: float = 75.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_50:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_51:
    delta: float = 0.03050
    lam: float = 75.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_51:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_52:
    delta: float = 0.03100
    lam: float = 76.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_52:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_53:
    delta: float = 0.03150
    lam: float = 76.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_53:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_54:
    delta: float = 0.03200
    lam: float = 77.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_54:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_55:
    delta: float = 0.03250
    lam: float = 77.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_55:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_56:
    delta: float = 0.03300
    lam: float = 78.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_56:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_57:
    delta: float = 0.03350
    lam: float = 78.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_57:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_58:
    delta: float = 0.03400
    lam: float = 79.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_58:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_59:
    delta: float = 0.03450
    lam: float = 79.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_59:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_60:
    delta: float = 0.03500
    lam: float = 80.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_60:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_61:
    delta: float = 0.03550
    lam: float = 80.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_61:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_62:
    delta: float = 0.03600
    lam: float = 81.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_62:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_63:
    delta: float = 0.03650
    lam: float = 81.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_63:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_64:
    delta: float = 0.03700
    lam: float = 82.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_64:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_65:
    delta: float = 0.03750
    lam: float = 82.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_65:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_66:
    delta: float = 0.03800
    lam: float = 83.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_66:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_67:
    delta: float = 0.03850
    lam: float = 83.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_67:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_68:
    delta: float = 0.03900
    lam: float = 84.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_68:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_69:
    delta: float = 0.03950
    lam: float = 84.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_69:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_70:
    delta: float = 0.04000
    lam: float = 85.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_70:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_71:
    delta: float = 0.04050
    lam: float = 85.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_71:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_72:
    delta: float = 0.04100
    lam: float = 86.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_72:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_73:
    delta: float = 0.04150
    lam: float = 86.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_73:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_74:
    delta: float = 0.04200
    lam: float = 87.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_74:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_75:
    delta: float = 0.04250
    lam: float = 87.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_75:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_76:
    delta: float = 0.04300
    lam: float = 88.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_76:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_77:
    delta: float = 0.04350
    lam: float = 88.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_77:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_78:
    delta: float = 0.04400
    lam: float = 89.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_78:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_79:
    delta: float = 0.04450
    lam: float = 89.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_79:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_80:
    delta: float = 0.04500
    lam: float = 90.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_80:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_81:
    delta: float = 0.04550
    lam: float = 90.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_81:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_82:
    delta: float = 0.04600
    lam: float = 91.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_82:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_83:
    delta: float = 0.04650
    lam: float = 91.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_83:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_84:
    delta: float = 0.04700
    lam: float = 92.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_84:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_85:
    delta: float = 0.04750
    lam: float = 92.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_85:
    lam: float = 0.150
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_86:
    delta: float = 0.04800
    lam: float = 93.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_86:
    lam: float = 0.155
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_87:
    delta: float = 0.04850
    lam: float = 93.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_87:
    lam: float = 0.160
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_88:
    delta: float = 0.04900
    lam: float = 94.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_88:
    lam: float = 0.165
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_89:
    delta: float = 0.04950
    lam: float = 94.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_89:
    lam: float = 0.170
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_90:
    delta: float = 0.05000
    lam: float = 95.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_90:
    lam: float = 0.100
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_91:
    delta: float = 0.05050
    lam: float = 95.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_91:
    lam: float = 0.105
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_92:
    delta: float = 0.05100
    lam: float = 96.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_92:
    lam: float = 0.110
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_93:
    delta: float = 0.05150
    lam: float = 96.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_93:
    lam: float = 0.115
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_94:
    delta: float = 0.05200
    lam: float = 97.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_94:
    lam: float = 0.120
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_95:
    delta: float = 0.05250
    lam: float = 97.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_95:
    lam: float = 0.125
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_96:
    delta: float = 0.05300
    lam: float = 98.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_96:
    lam: float = 0.130
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_97:
    delta: float = 0.05350
    lam: float = 98.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_97:
    lam: float = 0.135
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_98:
    delta: float = 0.05400
    lam: float = 99.00
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_98:
    lam: float = 0.140
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

@dataclass
class PageHinkley_99:
    delta: float = 0.05450
    lam: float = 99.50
    mean: float = 0.0
    sum: float = 0.0
    min_sum: float = 0.0
    n: int = 0
    def update(self, x: float) -> bool:
        self.n += 1
        self.mean += (x - self.mean)/self.n
        self.sum += x - self.mean - self.delta
        self.min_sum = min(self.min_sum, self.sum)
        return (self.sum - self.min_sum) > self.lam

@dataclass
class MEWMA_99:
    lam: float = 0.145
    z: float = 0.0
    def update(self, x: float) -> float:
        self.z = self.lam*x + (1-self.lam)*self.z
        return self.z

