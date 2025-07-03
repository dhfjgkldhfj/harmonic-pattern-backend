from typing import List
import numpy as np
from app.models import HarmonicPattern, PatternPoints, FibonacciRatios, Point
from app.data_fetcher import fetch_candles

def find_pivots(df, window=3):
    highs = df['high'].values
    lows = df['low'].values
    pivot_highs = []
    pivot_lows = []

    for i in range(window, len(df) - window):
        window_high = highs[i - window:i + window + 1]
        window_low = lows[i - window:i + window + 1]

        if highs[i] == max(window_high):
            pivot_highs.append(i)
        if lows[i] == min(window_low):
            pivot_lows.append(i)

    return pivot_highs, pivot_lows

def approx_equal(value, target, tolerance=0.05):
    return abs(value - target) <= tolerance

async def detect_patterns(symbol: str, interval: str) -> List[HarmonicPattern]:
    df = await fetch_candles(symbol, interval)

    # إيجاد pivots
    pivot_highs, pivot_lows = find_pivots(df, window=3)

    # إذا لم نجد نقاط كافية نرجع قائمة فارغة
    if len(pivot_highs) < 2 or len(pivot_lows) < 2:
        return []

    # ببساطة نجرب آخر 5 نقاط (X,A,B,C,D) من pivot highs و lows بالتناوب (كمثال عملي)
    # هذا مجرد مثال للكشف عن نموذج Gartley بسيط جداً
    # يمكن تطوير منطق أذكى لاحقاً

    # بناء النقاط
    # هنا مثال: X (pivot low قديم) -> A (pivot high قديم) -> B (pivot low متوسط) -> C (pivot high متوسط) -> D (pivot low قريب)
    try:
        X_idx = pivot_lows[-5]
        A_idx = pivot_highs[-4]
        B_idx = pivot_lows[-3]
        C_idx = pivot_highs[-2]
        D_idx = pivot_lows[-1]

        X_price = df['low'][X_idx]
        A_price = df['high'][A_idx]
        B_price = df['low'][B_idx]
        C_price = df['high'][C_idx]
        D_price = df['low'][D_idx]

        # حساب نسب فيبوناتشي
        AB_ratio = (A_price - B_price) / (A_price - X_price)  # نسبة تصحيح AB
        BC_ratio = (C_price - B_price) / (A_price - B_price)  # نسبة تصحيح BC
        CD_ratio = (D_price - C_price) / (C_price - B_price)  # نسبة تمديد CD (غير دقيقة حسابياً لكنها توضيحية)

        # تحقق إذا النسب قريبة من نسب Gartley المعروفة
        if (
            approx_equal(AB_ratio, 0.618, 0.1) and
            approx_equal(BC_ratio, 0.382, 0.1) and
            approx_equal(CD_ratio, 1.272, 0.2)
        ):
            points = PatternPoints(
                X=Point(price=X_price, index=int(X_idx)),
                A=Point(price=A_price, index=int(A_idx)),
                B=Point(price=B_price, index=int(B_idx)),
                C=Point(price=C_price, index=int(C_idx)),
                D=Point(price=D_price, index=int(D_idx)),
            )
            ratios = FibonacciRatios(AB=AB_ratio, BC=BC_ratio, CD=CD_ratio)
            prz = [D_price * 0.99, D_price * 1.01]

            pattern = HarmonicPattern(
                pattern="Gartley",
                points=points,
                fibonacci_ratios=ratios,
                prz=prz
            )
            return [pattern]
    except Exception:
        return []

    return []
