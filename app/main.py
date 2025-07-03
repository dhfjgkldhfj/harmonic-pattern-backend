from fastapi import FastAPI, Query
from app.pattern_detection import detect_patterns

app = FastAPI()

@app.get("/patterns")
async def get_patterns(symbol: str = Query(...), interval: str = Query("1h")):
    """
    API endpoint to get detected harmonic patterns for given symbol and timeframe.
    """
    patterns = await detect_patterns(symbol, interval)
    return {"symbol": symbol, "interval": interval, "patterns": patterns}
