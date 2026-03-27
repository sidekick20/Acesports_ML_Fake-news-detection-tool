import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import os

# Download stopwords (only first time)
nltk.download('stopwords')

# Load stopwords ONCE (important for performance)
stop_words = set(stopwords.words('english'))


# 🔹 Text Cleaning Function
def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    words = text.split()
    words = [w for w in words if w not in stop_words]  # remove stopwords
    return " ".join(words)


# 🔹 Main Function
def load_and_process():
    print("🚀 Starting preprocessing...")

    # Paths
    fake_path = 'data/raw/Fake.csv'
    true_path = 'data/raw/True.csv'
    output_path = 'data/processed/cleaned.csv'

    # Check if files exist
    if not os.path.exists(fake_path) or not os.path.exists(true_path):
        print("❌ Dataset files not found! Check data/raw/ folder.")
        return

    # Load datasets
    print("📂 Loading datasets...")
    fake = pd.read_csv(fake_path)
    true = pd.read_csv(true_path)

    print("✅ Data loaded successfully")

    # Add labels
    fake['label'] = 0
    true['label'] = 1

    # Combine datasets
    data = pd.concat([fake, true], ignore_index=True)

    # Keep only required columns
    data = data[['text', 'label']]

    print(f"📊 Total samples: {len(data)}")

    # Ensure text is string
    data['text'] = data['text'].astype(str)

    # Clean text
    print("🧹 Cleaning text... (takes 1–2 minutes)")
    data['text'] = data['text'].apply(clean_text)
    print("✅ Cleaning completed")

    # Create processed folder if not exists
    os.makedirs('data/processed', exist_ok=True)

    # Save cleaned data
    print("💾 Saving cleaned dataset...")
    data.to_csv(output_path, index=False)

    print(f"🎉 Done! File saved at: {output_path}")


# 🔹 Entry Point
if __name__ == "__main__":
    load_and_process()