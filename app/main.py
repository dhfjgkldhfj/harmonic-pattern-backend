from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.pattern_detection import detect_patterns

app = FastAPI()

origins = [
    "https://harmonic-pattern-frontend.vercel.app",
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

@app.get("/")
async def root():
    return {"message": "API up and running. استخدم /patterns مع symbol و interval."}

@app.get("/patterns")
async def get_patterns(symbol: str = Query(...), interval: str = Query("1h")):
    patterns = await detect_patterns(symbol, interval)
    return {"symbol": symbol, "interval": interval, "patterns": patterns}
