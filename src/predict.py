import pickle
import re
import nltk


from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download('stopwords')

# Load stopwords once
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = pickle.load(open('models/model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))


# 🔹 Preprocessing (SAME as training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)  

def predict_news(text):
    # Clean and preprocess text
    cleaned = clean_text(text)

    # Transform text to features
    features = vectorizer.transform([cleaned])

    # Make prediction
    prediction = model.predict(features)[0]

    # Get confidence (probability)
    probabilities = model.predict_proba(features)[0]
    confidence = max(probabilities)

    return prediction, confidence


# 🔹 Explainability (Top keywords)
def explain_prediction(text):
    cleaned = clean_text(text)
    transformed = vectorizer.transform([cleaned])

    feature_names = vectorizer.get_feature_names_out()
    scores = transformed.toarray()[0]

    important_words = sorted(
        zip(feature_names, scores),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    return [word for word, score in important_words if score > 0]


# 🔹 Main (Terminal testing)
if __name__ == "__main__":
    while True:
        text = input("\n📰 Enter news text (or type 'exit'): ")

        if text.lower() == 'exit':
            break

        pred, conf = predict_news(text)

        label = "REAL ✅" if pred == 1 else "FAKE ❌"

        print("\n🔍 Result:")
        print("Prediction:", label)
        print("Confidence:", round(conf * 100, 2), "%")

        print("Key words:", explain_prediction(text))