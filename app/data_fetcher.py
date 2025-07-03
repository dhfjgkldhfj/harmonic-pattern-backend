import yfinance as yf
import pandas as pd

async def fetch_candles(symbol: str, interval: str) -> pd.DataFrame:
    """
    جلب بيانات الشموع من Yahoo Finance.
    symbol مثال: "BTCUSDT", "ETHUSDT", "AAPL"
    interval: '1m', '5m', '15m', '1h', '4h', '1d', '1wk', '1mo'
    """

    # تحويل رمز التداول ليناسب Yahoo Finance
    yf_symbol = symbol.upper()
    if yf_symbol.endswith("USDT"):
        yf_symbol = yf_symbol[:-4] + "-USD"  # BTCUSDT -> BTC-USD
    # يمكن إضافة تحويلات أخرى حسب الحاجة

    interval_map = {
        "1m": "1m",
        "5m": "5m",
        "15m": "15m",
        "1h": "60m",
        "4h": "60m",  # لا يوجد دعم رسمي لـ 4 ساعات في yfinance - يمكن استخدام 60m
        "1d": "1d",
        "1wk": "1wk",
        "1mo": "1mo",
    }

    yf_interval = interval_map.get(interval, "1d")

    # تنزيل البيانات لآخر 7 أيام كافتراض، يمكن تعديل الفترة حسب الحاجة
    data = yf.download(tickers=yf_symbol, period="7d", interval=yf_interval, progress=False)

    if data.empty:
        raise ValueError(f"No data found for symbol {yf_symbol} with interval {yf_interval}")

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
