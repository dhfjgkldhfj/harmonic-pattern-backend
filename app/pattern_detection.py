import numpy as np
import pandas as pd
from typing import List
from app.models import HarmonicPattern, PatternPoints, FibonacciRatios
from app.data_fetcher import fetch_candles

async def detect_patterns(symbol: str, interval: str) -> List[HarmonicPattern]:
    """
    كشف نماذج هارمونيك مبسطة باستخدام بيانات أسعار CoinGecko.
    """
    df = await fetch_candles(symbol, interval)

    # نستخدم سعر الإغلاق كالسعر الرئيسي
    prices = df["close"].values

    # مؤشر لكل نقطة (فقط أعداد صحيحة 0,1,2,...)
    indices = np.arange(len(prices))

    # للبساطة: اختر نقاط pivot يدوية (مثال)
    # في مشروع حقيقي يجب خوارزمية متقدمة للكشف عن نقاط X,A,B,C,D
    # هنا نختار أول 5 نقاط كمثال فقط:
    if len(prices) < 5:
        return []

    points = PatternPoints(
        X=prices[0],
        A=prices[1],
        B=prices[2],
        C=prices[3],
        D=prices[4]
    )

    fibonacci_ratios = FibonacciRatios(
        AB=0.618,
        BC=0.382,
        CD=1.272
    )

    prz = [prices[3], prices[4]]

    pattern = HarmonicPattern(
        pattern="SamplePattern",
        points=points,
        fibonacci_ratios=fibonacci_ratios,
        prz=prz
    )

    return [pattern]
