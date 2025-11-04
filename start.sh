#!/bin/bash
echo "Starting bot..."

# Usar ruta absoluta y llamar al archivo como script (no como paquete)
python3 -u bot_trading/main.py
python app.py
