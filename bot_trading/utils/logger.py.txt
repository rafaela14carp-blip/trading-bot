import csv
from pathlib import Path
from datetime import datetime

LOGFILE = Path("trades_log.csv")

def log_trade(entry: dict):
    write_header = not LOGFILE.exists()
    with LOGFILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(entry.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(entry)

def log_info(msg: str):
    print(f"[{datetime.utcnow().isoformat()}] {msg}")
