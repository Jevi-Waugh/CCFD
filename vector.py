from __future__ import annotations
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector{self.x, self.y}"
    
    # def __eq__(self, other: Vector) -> bool:
    #     return self.x == other.x and self.y == other.y
    
    def __add__(self, other : Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other : Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)
    
    def manhatten_distance(self: Vector, other: Vector) -> int:
        # Heuristic
        # for all E |xi - yi|
        # a vector instance needs to be calling this
        return abs(self.x - other.x) + abs(self.y - other.y)