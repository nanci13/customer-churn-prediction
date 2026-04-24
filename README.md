# customer-churn-prediction
Built an end-to-end Customer Churn Prediction system using machine learning. Performed data preprocessing, feature engineering, and trained a Random Forest model. Developed a Streamlit-based web app to predict churn in real-time with probability scores, improving usability through simplified user inputs.


# Customer Churn Prediction 📊

## 📌 Overview

This project is a "Machine Learning model" that predicts whether a customer is likely to churn (leave a service) based on their usage
behavior and demographic data.
It helps businesses identify at-risk customers and take proactiveretention actions.



## 🚀 Project Features

### 📌 Input Features Used
The model is trained on customer behavior attributes such as:
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Internet Service Type
- Online Security / Tech Support usage


---

### 🤖 ML Pipeline
- Data Cleaning & Missing Value Handling
- Exploratory Data Analysis (EDA)
- Feature Encoding (Categorical → Numerical)
- Model Training (Classification)
- Prediction of Customer Churn

---

### 📊 Output
- Predicts whether a customer will **Churn or Not Churn**
- Provides probability score (if enabled)


## 🧠 Technologies Used

-   Python 🐍
-   Pandas, NumPy
-   Scikit-learn
-   os , pickle,json
-   Streamlit 
-   python (frontend UI)


## 📂 Project Structure

   customer project/
│
├── backend/
│   ├── app.py
│   ├── columns.json
│   ├── model.pkl
│   ├── preprocess.py
│   ├── test_api.py
│   └── train.py
│
├── data/
│   └── churn.csv
│
├── frontend/
│   └── app_ui.py
│
├── notebooks/
│   └── model_training.ipynb
│
└── README.md

## ⚙️ Installation
git clone https://github.com/nanci13/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt



## ▶️ How to Run
python frontend/app_ui.py

## 📊 Model Performance

-   Accuracy: \~85-95% (depending on model used)
-   Evaluated using confusion matrix, precision, recall


## 🔮 Future Improvements

-   Deploy using Streamlit or Flask
-   Add real-time prediction API
-   Improve model with hyperparameter tuning
-   Add dashboard for analytics


## 👩‍💻 Author

Developed by "Nanci Rawat"


## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
