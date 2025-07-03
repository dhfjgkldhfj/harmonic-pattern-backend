import httpx
import pandas as pd
from datetime import datetime

# خريطة بسيطة لتحويل رموز Binance إلى معرفات CoinGecko
def symbol_to_coingecko_id(symbol: str) -> str:
    mapping = {
        "BTCUSDT": "bitcoin",
        "ETHUSDT": "ethereum",
        "BNBUSDT": "binancecoin",
        # أضف رموز أخرى حسب الحاجة
    }
    return mapping.get(symbol.upper())

# تحويل فترات Binance إلى فترات CoinGecko المناسبة
INTERVAL_MAP = {
    "1m": "minutely",
    "5m": "minutely",
    "15m": "minutely",
    "1h": "hourly",
    "4h": "hourly",
    "1d": "daily",
    "1w": "weekly",
}

async def fetch_candles(symbol: str, interval: str):
    """
    جلب بيانات أسعار من CoinGecko API.
    ملاحظة: CoinGecko لا يوفر بيانات شموع كاملة، لذا هذه بيانات سعر إغلاق تقريبي.
    """
    coin_id = symbol_to_coingecko_id(symbol)
    if not coin_id:
        raise ValueError(f"Unsupported symbol {symbol}")

    vs_currency = "usd"
    days = "30"  # آخر 30 يوم من البيانات

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": vs_currency,
        "days": days,
        "interval": INTERVAL_MAP.get(interval, "daily"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    prices = data.get("prices", [])

    # تحويل الأسعار إلى DataFrame
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    # إعداد أعمدة Open, High, Low, Close كلها مساوية للسعر (تقريب)
    df["open"] = df["price"]
    df["high"] = df["price"]
    df["low"] = df["price"]
    df["close"] = df["price"]

    return df
