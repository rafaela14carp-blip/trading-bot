import os

USE_TESTNET = os.getenv("USE_BINANCE_TESTNET", "true").lower() == "true"

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

# Parámetros de riesgo / interés compuesto
INITIAL_CAPITAL = 20.0        # USDT de ejemplo
RISK_PER_TRADE = 0.01         # 1% del capital por operación
MAX_POSITIONS = 3
STOP_LOSS_PCT = 0.01          # 1%
TAKE_PROFIT_PCT = 0.015       # 1.5%

# Datos / frecuencia
SYMBOL = "BTCUSDT"
INTERVAL = "1m"               # timeframe para pruebas: 1m
FETCH_WINDOW = 200            # barras históricas a usar
SLEEP_SECONDS = 30            # ciclo principal
