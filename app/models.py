from pydantic import BaseModel
from typing import List

class PatternPoints(BaseModel):
    X: float
    A: float
    B: float
    C: float
    D: float

class FibonacciRatios(BaseModel):
    AB: float
    BC: float
    CD: float

class HarmonicPattern(BaseModel):
    pattern: str
    points: PatternPoints
    fibonacci_ratios: FibonacciRatios
    prz: List[float]
