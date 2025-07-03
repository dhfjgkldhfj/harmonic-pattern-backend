from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.pattern_detection import detect_patterns

app = FastAPI()

# السماح للفرونت اند بالتواصل مع الباك اند (غير آمن للإنتاج لكن مناسب للتجربة)
origins = [
    "https://harmonic-pattern-frontend.vercel.app",  # رابط الفرونت اند الفعلي على Vercel
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/patterns")
async def get_patterns(symbol: str = Query(...), interval: str = Query("1h")):
    """
    API endpoint to get detected harmonic patterns for given symbol and timeframe.
    """
    patterns = await detect_patterns(symbol, interval)
    return {"symbol": symbol, "interval": interval, "patterns": patterns}
