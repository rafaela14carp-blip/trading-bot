from binance.client import Client
import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


def get_client():
    if os.getenv("USE_TESTNET", "true").lower() == "true":
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        client.API_URL = 'https://testnet.binance.vision/api'
    else:
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
    return client


def fetch_klines(symbol="BTCUSDT", interval="1h", limit=100):
    client = get_client()
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    return klines


