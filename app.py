import sys
import os

# Agregar la carpeta bot_trading al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'bot_trading'))

from main import main

if __name__ == "__main__":
    print("Ejecutando bot desde app.py...")
    main()
