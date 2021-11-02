#! /usr/bin/env python3
# coding: utf-8

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)


# --- Load Model ---

print("Load Classification Model")
with open('model_classification.bin', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return f"Hello world !<br>The Wine server is up."


@app.route('/predict', methods=['POST'])
def predict():
    wine_infos = request.get_json()

    pred = model.predict(wine_infos)
    pred_proba = model.predict_proba(wine_infos)

    return jsonify(f"The predicted quality for the physicochemical information ({wine_infos}) is: {pred[0]}\n(with the following probabilities: {pred_proba[0]})\n")


print("Server ready")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
