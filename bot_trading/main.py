import time
import numpy as np
from data.fetch_data import get_client, fetch_klines
from data.indicators import add_indicators
from ai.predictor import SimplePredictor
from ai.trainer import run_initial_training, prepare_features
from trading.execute_order import calc_order_amount, execute_trade
from trading.balance_manager import load_state, update_after_trade
from utils.logger import log_info

def main_loop():
    # entrenamiento inicial
    run_initial_training()
    pred = SimplePredictor()
    state = load_state()
    client = get_client()

    while True:
        try:
            df = fetch_klines(client)
            df = add_indicators(df)
            X, y = prepare_features(df)
            if len(X) == 0:
                log_info("Sin suficientes datos para predecir.")
                time.sleep(10)
                continue

            # Predecir el último registro (más reciente)
            latest_X = X[-1].reshape(1, -1)
            pred_label = pred.predict(latest_X)[0]  # 1=sube, 0=baja
            price = df["close"].iloc[-1]
            capital = state.get("capital", 0.0)
            qty = calc_order_amount(capital, price)

            log_info(f"Predicción: {pred_label} | Precio: {price} | Capital: {capital:.2f}")

            if pred_label == 1:
                # Simulamos compra de mercado (test)
                execute_trade("BUY", qty, price, reason="predicted_up")
                # Aquí deberíamos monitorizar y calcular P/L luego de cierre; por ahora simulamos ganancia ficticia
                simulated_profit = price * qty * 0.001  # ejemplo minigana 0.1%
                new_cap = update_after_trade(simulated_profit)
                state["capital"] = new_cap
                log_info(f"Operación simulada ganancia: {simulated_profit:.6f} new capital: {new_cap:.6f}")
            else:
                log_info("No se ejecuta operación (predice caída).")

            # Aprendizaje incremental: usar la etiqueta real del pasado reciente
            # (en entorno real hay que construir y pasar y_true)
            # Aquí no implementamos re-etiquetado automático por simplicidad.

            time.sleep(30)  # ciclo principal; ajustar a SLEEP_SECONDS de config

        except Exception as e:
            log_info(f"Error en loop principal: {e}")
            time.sleep(10)

if __name__ == "__main__":
print("Bot iniciado correctamente en Render")
