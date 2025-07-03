from pydantic import BaseModel
from typing import List

class Point(BaseModel):
    price: float
    index: int

class PatternPoints(BaseModel):
    X: Point
    A: Point
    B: Point
    C: Point
    D: Point

class FibonacciRatios(BaseModel):
    AB: float
    BC: float
    CD: float

class HarmonicPattern(BaseModel):
    pattern: str
    points: PatternPoints
    fibonacci_ratios: FibonacciRatios
    prz: List[float]
