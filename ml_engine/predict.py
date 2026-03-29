import joblib
import os

MODEL_PATH = "ml_engine/spam_model.pkl"
VECTORIZER_PATH = "ml_engine/vectorizer.pkl"

def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    return None, None

model, vectorizer = load_model()

def predict_spam(text):
    if model and vectorizer:
        vec = vectorizer.transform([text])
        return float(model.predict(vec)[0])
    return 0.5  # fallback for CI