from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model
model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))

# Load columns
with open(os.path.join(BASE_DIR, 'columns.json'), 'r') as f:
    model_columns = json.load(f)


@app.route('/')
def home():
    return "Churn Prediction API Running"


# 🔥 REPLACE THIS FUNCTION
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Minimal inputs
    tenure = data.get('tenure', 1)
    monthly = data.get('MonthlyCharges', 50)
    contract = data.get('Contract', 'Month-to-month')

    # Default values
    default_data = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "TotalCharges": tenure * monthly
    }

    # Override with user input
    default_data.update({
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "Contract": contract
    })

    df = pd.DataFrame([default_data])

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0)

    df = pd.get_dummies(df)
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return jsonify({
        "churn": int(prediction),
        "probability": float(probability)
    })


if __name__ == '__main__':
    app.run(debug=True)