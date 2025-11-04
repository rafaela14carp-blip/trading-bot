from bot_trading.data.fetch_data import get_client
from bot_trading.utils.config import SYMBOL, RISK_PER_TRADE, INITIAL_CAPITAL, STOP_LOSS_PCT, TAKE_PROFIT_PCT
from bot_trading.utils.logger import log_info, log_trade
import math, time
from bot_trading.trading.balance_manager import update_after_trade
client = get_client()

def calc_order_amount(capital, price, risk_pct=RISK_PER_TRADE):
    usd_to_use = capital * risk_pct
    qty = usd_to_use / price
    # redondeo sencillo (Binance requiere precision)
    return float("{:.6f}".format(qty))

def place_test_order(side, qty):
    # En testnet: usar create_test_order o enviar order con modo test.
    try:
        res = client.create_test_order(symbol=SYMBOL, side=side, type='MARKET', quantity=qty)
        log_info(f"Test order simulated: {side} qty={qty}")
        return res
    except Exception as e:
        log_info(f"Error simulando orden: {e}")
        return None

def execute_trade(side, qty, price, reason="signal"):
    # Este es el punto donde en main se tomaría la decisión
    res = place_test_order(side, qty)
    entry = {
        "timestamp": int(time.time()),
        "symbol": SYMBOL,
        "side": side,
        "qty": qty,
        "price": price,
        "reason": reason
    }
    log_trade(entry)
    return res




