import httpx
import pandas as pd

async def fetch_candles(symbol: str, interval: str):
    """
    Fetch OHLCV candle data from Binance public API asynchronously.
    """
    base_url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": 500
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit='ms')

    return df[["open_time", "open", "high", "low", "close", "volume"]]
