import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

data = {
    "text": [
        "Win money now",
        "Free lottery offer",
        "Call me later",
        "Meeting at 5pm",
        "You won prize",
        "Let's talk tomorrow"
    ],
    "label": [1, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)

joblib.dump(model, "ml_engine/spam_model.pkl")
joblib.dump(vectorizer, "ml_engine/vectorizer.pkl")

print("Model trained")