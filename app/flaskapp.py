import os
import joblib
import pandas as pd

from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = "models/sales_model.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

model = joblib.load(model_path)

@app.route("/")
def home():
    return "Advertising Sales Prediction API is running"

@app.route("/predict")
def predict():
    try:
        tv = float(request.args.get("tv"))
        radio = float(request.args.get("radio"))
        newspaper = float(request.args.get("newspaper"))

        input_data = pd.DataFrame(
            [[tv, radio, newspaper]],
            columns=["TV", "Radio", "Newspaper"]
        )

        prediction = model.predict(input_data)[0]

        return jsonify({
            "tv": tv,
            "radio": radio,
            "newspaper": newspaper,
            "predicted_sales": round(prediction, 2)
        })

    except Exception as error:
        return jsonify({
            "error": str(error),
            "example": "/predict?tv=100&radio=20&newspaper=10"
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
