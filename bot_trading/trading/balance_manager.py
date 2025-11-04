import json
from pathlib import Path
from bot_trading.utils.config import INITIAL_CAPITAL
from bot_trading.utils.logger import log_info

STATE_FILE = Path("state.json")

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    # estado inicial
    state = {"capital": INITIAL_CAPITAL, "positions": []}
    save_state(state)
    return state

def save_state(state):
    STATE_FILE.write_text(json.dumps(state))

def update_after_trade(profit_loss):
    state = load_state()
    state["capital"] = state.get("capital", INITIAL_CAPITAL) + profit_loss
    save_state(state)
    return state["capital"]


