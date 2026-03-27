from flask import Blueprint, request, jsonify, render_template
from src.predict import predict_news, explain_prediction

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    prediction, confidence = predict_news(text)
    keywords = explain_prediction(text)
    label = "REAL" if prediction == 1 else "FAKE"

    return jsonify({
        'label': label,
        'confidence': round(float(confidence) * 100, 2),
        'keywords': keywords
    })