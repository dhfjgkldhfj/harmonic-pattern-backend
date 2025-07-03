from typing import List
from fastapi import FastAPI, Query
from app.pattern_detection import detect_patterns
from app.models import HarmonicPattern

app = FastAPI()

@app.get("/patterns", response_model=List[HarmonicPattern])
async def get_patterns(symbol: str = Query(...), interval: str = Query("1h")):
    patterns = await detect_patterns(symbol, interval)
    return patterns

@app.get("/")
async def root():
    return {"message": "API up and running. استخدم /patterns مع symbol و interval."}
