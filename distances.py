import numpy as np
# from __future__ import annotations
from vector import Vector

def euclidean_distance(x, y) -> float:
    return np.sqrt(np.sum(x-y)**2)

def manhatten_distance(self: Vector, other: Vector) -> int:
    return abs(self.x - other.x) + abs(self.y - other.y)

def minkowski_distance(self):
    pass