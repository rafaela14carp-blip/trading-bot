import numpy as np
from sklearn.linear_model import SGDClassifier
import joblib
from pathlib import Path

MODEL_PATH = Path("ai_model.pkl")

class SimplePredictor:
    def __init__(self):
        self.model = None
        if MODEL_PATH.exists():
            self.model = joblib.load(MODEL_PATH)
        else:
            # classifier binario: subir (1) / bajar (0)
            self.model = SGDClassifier(max_iter=1000, tol=1e-3)
            # necesita un partial_fit inicial: lo haremos en trainer con clases [0,1]

    def predict(self, X):
        # X: numpy array (n_samples, n_features)
        if X.shape[0] == 0:
            return np.array([])
        try:
            preds = self.model.predict(X)
            return preds
        except Exception:
            # en caso de que no esté entrenado
            return np.zeros(X.shape[0], dtype=int)

    def partial_fit(self, X, y):
        # X,y numpy arrays
        if hasattr(self.model, "partial_fit"):
            self.model.partial_fit(X, y, classes=np.array([0,1]))
            # guardar modelo
            import joblib
            joblib.dump(self.model, MODEL_PATH)
