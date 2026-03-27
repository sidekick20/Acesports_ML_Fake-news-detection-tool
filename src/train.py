import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


def train_model():
    print("🚀 Starting training...")

    # 🔹 Path
    data_path = 'data/processed/cleaned.csv'

    # 🔹 Check file exists
    if not os.path.exists(data_path):
        print("❌ Cleaned data not found! Run preprocess.py first.")
        return

    # 🔹 Load data (ONLY ONCE)
    print("📂 Loading cleaned data...")
    data = pd.read_csv(data_path)

    print(f"📊 Total samples: {len(data)}")

    # 🔹 Clean NaN and empty values
    print("🧹 Cleaning NaN values...")
    data = data.dropna(subset=['text'])
    data['text'] = data['text'].astype(str)
    data = data[data['text'].str.strip() != ""]

    print(f"✅ Remaining samples after cleaning: {len(data)}")

    # 🔹 Check label balance (important insight)
    print("\n📊 Label Distribution:")
    print(data['label'].value_counts())

    # 🔹 Split data
    X = data['text']
    y = data['label']

    print("\n✂️ Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🔹 TF-IDF with BIGRAMS (IMPORTANT IMPROVEMENT)
    print("🔢 Converting text to features (TF-IDF with bigrams)...")
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2)   # 🔥 key improvement
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 🔹 Model (better for text)
    print("🤖 Training model (SGDClassifier)...")
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # 🔹 Evaluation
    print("🔮 Evaluating model...")
    y_pred = model.predict(X_test_vec)

    accuracy = accuracy_score(y_test, y_pred)

    print("\n📈 RESULTS")
    print("Accuracy:", accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # 🔹 Save model
    print("💾 Saving model...")
    os.makedirs('models', exist_ok=True)

    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('models/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    print("🎉 Model saved in models/ folder")


if __name__ == "__main__":
    train_model()