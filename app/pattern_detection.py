import asyncio
from typing import List
from app.models import HarmonicPattern, PatternPoints, FibonacciRatios, Point

async def fetch_candles(symbol: str, interval: str):
    # هنا جلب بيانات الشموع الحقيقية من API أو من بيانات وهمية
    # حاليا سنستخدم بيانات وهمية ثابتة (mock)
    # كل شمعة لها 'close' وسطر 'index' (رقم الشمعة)
    import pandas as pd
    data = {
        "close": [1.0, 1.2, 1.15, 1.18, 1.22, 1.25, 1.28, 1.30],
        "index": list(range(8)),
    }
    df = pd.DataFrame(data)
    await asyncio.sleep(0.1)
    return df

async def detect_patterns(symbol: str, interval: str) -> List[HarmonicPattern]:
    df = await fetch_candles(symbol, interval)

    # نقاط وهمية حقيقية (مبنية على إندكسات من df)
    example_points = PatternPoints(
        X=Point(price=df["close"][0], index=df["index"][0]),
        A=Point(price=df["close"][1], index=df["index"][1]),
        B=Point(price=df["close"][2], index=df["index"][2]),
        C=Point(price=df["close"][3], index=df["index"][3]),
        D=Point(price=df["close"][4], index=df["index"][4]),
    )
    example_ratios = FibonacciRatios(
        AB=0.618,
        BC=0.382,
        CD=1.272
    )
    example_prz = [df["close"][4], df["close"][4]*1.02]

    pattern = HarmonicPattern(
        pattern="Gartley",
        points=example_points,
        fibonacci_ratios=example_ratios,
        prz=example_prz
    )

    return [pattern]
