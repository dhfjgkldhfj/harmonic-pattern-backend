from pydantic import BaseModel
from typing import Dict, List, Optional

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
    prz: List[float]  # Potential Reversal Zone range as list (start, end)
