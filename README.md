🎯 Problem Statement: Fake News Detection Tool

📰 With the rapid growth of social media and digital platforms, fake news spreads faster than ever, impacting public opinion, creating confusion, and sometimes causing serious harm.

⚠️ Users often struggle to verify whether information is authentic or misleading.

💡 Objective:
To develop a web-based Fake News Detection Tool (VerifyAI) that:

🧠 Uses Machine Learning algorithms to analyze news content
🔍 Classifies news as Fake or Real
📊 Provides a confidence score and explanation
⚡ Delivers quick and user-friendly results
👥 Team Members & Roles

👨‍💻 Yogesh Sawant – Frontend Developer
🎨 Designed user interface using HTML, CSS, JavaScript
🧩 Built interactive UI components
📱 Ensured responsive and clean design


👨‍💻 Prathmesh Karemore – Frontend Developer
🖌️ Assisted in UI/UX design and styling
🔄 Integrated frontend features with backend APIs
⚙️ Improved usability and performance


🖥️ Vedant Toke – Backend Developer
🔗 Developed server-side logic (Flask/Node.js)
📡 Managed API communication
🔐 Handled data processing and integration


🤖 Karan Bhilare – ML Model & Training
📊 Collected and cleaned datasets
🧠 Trained machine learning models
📈 Optimized accuracy and prediction performance


📄 Abhishek Vannal – Documentation & Presentation
📝 Prepared project documentation and report
🎤 Created presentation slides
🧪 Assisted in testing and final demonstration
 
  

A full-stack Machine Learning web application that detects whether a given news article or headline is **REAL or FAKE** using Natural Language Processing (NLP) and supervised learning techniques.

---

## 🚀 Project Overview

With the rapid spread of misinformation on digital platforms, it has become increasingly difficult to distinguish between real and fake news. This project provides an intelligent system that analyzes news content and predicts its authenticity in real-time.

The system combines:

* **Machine Learning (Naive Bayes)**
* **Natural Language Processing (TF-IDF)**
* **Flask Backend API**
* **Interactive User Input System**

to deliver accurate and explainable predictions.

---

## 🎯 Objectives

* Detect fake news using machine learning
* Provide real-time predictions via API
* Improve interpretability using keyword explanations
* Build a scalable full-stack ML system
* Deploy a production-ready solution

---

## 🏗️ System Architecture

```
User Input (Frontend / Terminal)
        ↓
Flask Backend API
        ↓
Preprocessing (Cleaning Text)
        ↓
TF-IDF Vectorization
        ↓
Naive Bayes Model
        ↓
Prediction + Confidence + Keywords
```

---

## 🧠 Machine Learning Pipeline

### 1. Data Collection

* Dataset: Fake & Real News Dataset (Kaggle)
* Combined two datasets:

  * Fake news → Label 0
  * Real news → Label 1

👉 Similar projects also rely on labeled datasets for supervised classification ([GitHub][1])

---

### 2. Data Preprocessing

* Lowercasing text
* Removing punctuation and special characters
* Stopword removal using NLTK
* Handling missing and empty values

---

### 3. Feature Engineering

**TF-IDF (Term Frequency – Inverse Document Frequency)**

* Converts text into numerical features
* Assigns importance to meaningful words
* Uses **n-grams (1,2)** for better context

Example:

* “economic policy” treated as one feature

---

### 4. Model Selection

**Algorithm Used:** Multinomial Naive Bayes

#### Why Naive Bayes?

* Efficient for high-dimensional text data
* Works well with TF-IDF features
* Fast training and prediction
* Strong baseline for NLP tasks

---

### 5. Model Evaluation

* Train/Test Split: 80/20
* Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1 Score

👉 Achieved:

* **Accuracy: ~90–95%**

---

## 🔍 Explainability Feature

The system provides **top keywords influencing prediction**

Example:

```
Input: "Breaking shocking news revealed"
Output: ['breaking', 'shocking', 'revealed']
```

👉 Helps users understand **why the model predicted FAKE or REAL**

---

## 🔮 Prediction System

### Input:

* News headline or article

### Output:

* Prediction: REAL / FAKE
* Confidence score (%)
* Important keywords

---

## 🌐 Backend (Flask API)

### API Endpoint:

```
POST /predict
```

### Request:

```json
{
  "text": "Government announces new economic policy"
}
```

### Response:

```json
{
  "prediction": "REAL",
  "confidence": 82.3,
  "keywords": ["economic", "policy"]
}
```

---

## ⚙️ Backend Features

* REST API using Flask
* Model loading using pickle
* Real-time inference
* JSON-based communication
* Error handling for invalid input

---

## 🎨 Frontend / User Interaction

Current system supports:

* Terminal-based interaction (`predict.py`)
* API testing via Postman / Thunder Client



* HTML + CSS UI
* React frontend
* Input box for news text
* Result display card

👉 Similar projects integrate HTML templates and UI pages for predictions ([GitHub][2])

---

## 📂 Project Structure

```
Fake-News-Detection-System/
│
├── index.html
├── script.js
├── style.css
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── __pycache__/
│   │   ├── __init__.cpython-314.pyc
│   │   └── predict.cpython-314.pyc
│   │
│   ├── __init__.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── train.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
├── application.py
├── config.py
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/sidekick20/Acesports_ML_Fake-news-detection-tool.git
cd Acesports_ML_Fake-news-detection-tool
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Preprocessing

```bash
python src/preprocess.py
```

---

### 4. Train Model

```bash
python src/train.py
```

---

### 5. Run Prediction (Terminal)

```bash
python src/predict.py
```

---

### 6. Start Flask Server

```bash
python app.py
```



## 🚀 Future Improvements

* Integrate transformer models like BERT
* Add real-time fact-check APIs
* Multi-language support
* Improve contextual understanding
* Deploy on cloud (Render / AWS)


## 📌 Conclusion

This project demonstrates how machine learning and NLP can be effectively used to detect fake news. It combines accuracy, speed, and explainability into a deployable system, making it a practical real-world solution to combat misinformation.

---

