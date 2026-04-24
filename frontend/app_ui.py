import streamlit as st
import requests

st.title("💡 Customer Churn Prediction")

st.write("Enter customer details:")

# Inputs
tenure = st.slider("Tenure (months)", 1, 72, 12)
monthly = st.slider("Monthly Charges", 10, 150, 50)
contract = st.selectbox("Contract Type", [
    "Month-to-month", "One year", "Two year"
])

# Button
if st.button("Predict"):

    url = "http://127.0.0.1:5000/predict"

    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "Contract": contract
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()

        churn = result["churn"]
        prob = result["probability"]

        if churn == 1:
            st.error(f"⚠️ Customer likely to churn ({prob*100:.2f}%)")
        else:
            st.success(f"✅ Customer likely to stay ({prob*100:.2f}%)")
    else:
        st.error("Error connecting to API")