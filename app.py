import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import sys
import os

# Asegura que Python pueda encontrar el módulo dentro de bot_trading
sys.path.append(os.path.join(os.path.dirname(__file__), 'bot_trading'))

from bot_trading.main import main  # 👈 Import correcto

if __name__ == "__main__":
    print("🚀 Iniciando el bot desde app.py...")
    main()
