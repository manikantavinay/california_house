from flask import Flask, request, render_template
import numpy as np
import joblib

load = joblib.load("califianio.joblib")

model = load["model"]
columns = load["columns"]

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", columns=columns)


@app.route("/predict", methods=["POST"])
def predict():

    input_data = []

    for column in columns:
        value = float(request.form[column])
        input_data.append(value)

    input_data = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        columns=columns,
        prediction=round(float(prediction), 2)
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )