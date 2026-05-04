import streamlit as st
import requests

st.title("💡 Customer Churn Prediction System")

st.header("Enter Customer Details")

# ---------------- BASIC ----------------
tenure = st.slider("Tenure (months)", 1, 72, 12)
monthly = st.slider("Monthly Charges", 10, 150, 50)

# ---------------- CATEGORICAL ----------------
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["NO", "YES"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

payment = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

# ---------------- BUTTON ----------------
if st.button("Predict"):

    url = "http://127.0.0.1:5000/predict"

    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_sec,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": tenure * monthly
    }

    try:
        res = requests.post(url, json=data)
        result = res.json()

        if "churn" in result:
            st.subheader("Prediction Result")

            if result["churn"] == 1:
                st.error("⚠️ Customer likely to churn")
            else:
                st.success("✅ Customer likely to stay")
        else:
            st.error(f"API Error: {result}")

    except Exception as e:
        st.error(f"Connection Error: {e}")
