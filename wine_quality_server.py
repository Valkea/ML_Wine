#! /usr/bin/env python3
# coding: utf-8

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)


# --- Load Model ---

print("Load Classification Model")
with open("model_classification.bin", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return f"Hello world !<br>The Wine server is up."


@app.route("/predict", methods=["POST"])
def predict():
    wine_infos = request.get_json()

    print(wine_infos)

    pred = model.predict(wine_infos)
    pred_proba = model.predict_proba(wine_infos)

    return jsonify(
        f"The predicted quality is: {pred[0]}\n<br>(with the following probabilities: {pred_proba[0]})\n"
    )


@app.route("/input")
def inputpage():
    html = """
    <html>
        <head>
            <title>Wine pyshicochemical information input</title>
            <script>

                function submitFunction() {
                    let A = document.getElementById('alcohol').value;
                    let B = document.getElementById('volatile_acidity').value;
                    let C = document.getElementById('sulphates').value;
                    let D = document.getElementById('citric_acid').value;
                    let E = document.getElementById('total_sulfur_dioxide').value;
                    let F = document.getElementById('density').value;
                    getPredict([A,B,C,D,E,F]);
                }

                function getPredict(ar){

                    fetch("/predict", {
                        method: "POST",
                        body: JSON.stringify([ar]),
                        headers: {
                            "Content-type": "application/json; charset=UTF-8"
                        }
                    })

                    .then(response => response.json())
                    .then(json => displayResult(json))
                    .catch( error => console.error('error:', error) );
                }

                function displayResult(r)
                {
                    document.getElementById('result').innerHTML = r
                }

            </script>
        </head>
        <body>

            <form>
            <p>
                <input type="range" value=0.4 min=0.0 max=15.0 step=0.1 id='alcohol'
                    oninput="this.nextElementSibling.value = this.value">
                <output>0.4</output>
                alcohol
            </p>

            <p>
                <input type="range" value=0.4 min=0.0 max=2.0 step=0.01 id='volatile_acidity'
                    oninput="this.nextElementSibling.value = this.value">
                <output>0.4</output>
                volatile_acidity
            </p>

            <p>
                <input type="range" value=0.4 min=0.0 max=2.0 step=0.01 id='sulphates'
                    oninput="this.nextElementSibling.value = this.value">
                <output>0.4</output>
                sulphates
            </p>

            <p>
                <input type="range" value=0.4 min=0.0 max=1.0 step=0.01 id='citric_acid'
                    oninput="this.nextElementSibling.value = this.value">
                <output>0.4</output>
                citric_acid
            </p>

            <p>
                <input type="range" value=4 min=0.0 max=300.0 step=1 id='total_sulfur_dioxide'
                    oninput="this.nextElementSibling.value = this.value">
                <output>4</output>
                total_sulfur_dioxide
            </p>

            <p>
                <input type="range" value=0.995 min=0.99 max=1.1 step=0.001 id='density'
                    oninput="this.nextElementSibling.value = this.value">
                <output>0.995</output>
                density
            </p>
            <p></p>
            <p><input type='button' value='Predict' onclick='submitFunction()'></p>
            </form>
            <p id='result'></p>
        </body>
    </html>
    """
    return html


print("Server ready")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
