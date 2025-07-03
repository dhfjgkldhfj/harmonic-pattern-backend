import yfinance as yf
import pandas as pd
import anyio

async def fetch_candles(symbol: str, interval: str) -> pd.DataFrame:
    yf_symbol = symbol.upper()
    if yf_symbol.endswith("USDT"):
        yf_symbol = yf_symbol[:-4] + "-USD"

    interval_map = {
        "1m": "1m",
        "5m": "5m",
        "15m": "15m",
        "1h": "60m",
        "4h": "60m",  # لا يدعم 4 ساعات بشكل مباشر في yfinance
        "1d": "1d",
        "1wk": "1wk",
        "1mo": "1mo",
    }
    yf_interval = interval_map.get(interval, "1d")

    data = await anyio.to_thread.run_sync(
        lambda: yf.download(tickers=yf_symbol, period="7d", interval=yf_interval, progress=False)
    )

    if data.empty:
        raise ValueError(f"No data found for {yf_symbol} with interval {yf_interval}")

    data.reset_index(inplace=True)
    data.rename(columns={
        "Date": "timestamp",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    }, inplace=True)

    return data
