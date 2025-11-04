from binance.client import Client
import pandas as pd
from bot_trading.utils.config import BINANCE_API_KEY, BINANCE_API_SECRET, USE_TESTNET, SYMBOL, INTERVAL, FETCH_WINDOW
from bot_trading.utils.logger import log_info

def get_client():
    if USE_TESTNET:
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)
    else:
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
    return client

def fetch_klines(client: Client, symbol=SYMBOL, interval=INTERVAL, limit=FETCH_WINDOW):
    # devuelve DataFrame con columnas: open, high, low, close, volume, open_time
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "open_time","open","high","low","close","volume","close_time","qav",
        "num_trades","taker_base_vol","taker_quote_vol","ignore"
    ])
    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    return df


