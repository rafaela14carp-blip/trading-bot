#!/usr/bin/env bash
set -e

echo "🚀 Iniciando bot de trading..."

# Asegurarse de estar en la carpeta raíz
cd "$(dirname "$0")"

# Ejecutar el módulo principal
python -m bot_trading.main
