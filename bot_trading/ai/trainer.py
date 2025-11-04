import numpy as np
from bot_trading.data.fetch_data import get_client, fetch_klines
from bot_trading.data.indicators import add_indicators
from bot_trading.ai.predictor import SimplePredictor
from bot_trading.utils.logger import log_info

def prepare_features(df):
    # ejemplo simple: usar relacion EMA y rsi y mom
    X = df[["ema8","ema21","rsi","mom"]].values
    # target: si close sube en el siguiente paso
    y = (df["close"].shift(-1) > df["close"]).astype(int).values[:-1]
    X = X[:-1]
    return X, y

def run_initial_training():
    client = get_client()
    df = fetch_klines(client)
    df = add_indicators(df)
    X, y = prepare_features(df)
    if len(X) > 10:
        pred = SimplePredictor()
        log_info("Entrenando modelo inicial con datos históricos...")
        pred.partial_fit(X, y)
        log_info("Entrenamiento inicial completado.")
    else:
        log_info("Datos insuficientes para entrenamiento inicial.")




