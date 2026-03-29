import joblib

model = joblib.load("ml_engine/spam_model.pkl")
vectorizer = joblib.load("ml_engine/vectorizer.pkl")

def predict_spam(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return float(prediction)