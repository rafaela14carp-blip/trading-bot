import pandas as pd
import numpy as np

def add_indicators(df: pd.DataFrame):
    # EMA rápida y lenta
    df = df.copy()
    df["ema8"] = df["close"].ewm(span=8, adjust=False).mean()
    df["ema21"] = df["close"].ewm(span=21, adjust=False).mean()
    # RSI simple
    delta = df["close"].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.ewm(com=13, adjust=False).mean()
    ma_down = down.ewm(com=13, adjust=False).mean()
    rs = ma_up / (ma_down + 1e-9)
    df["rsi"] = 100 - (100 / (1 + rs))
    # Momentum simple
    df["mom"] = df["close"].pct_change(3)
    # Feature set (dropna at the end)
    df = df.dropna().reset_index(drop=True)
    return df
