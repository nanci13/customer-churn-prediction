print ('running updated file')
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import json


# Load data safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, '..', 'data', 'churn.csv')

df = pd.read_csv(data_path)

# ✅ Clean column names
df.columns = df.columns.str.strip()

# ✅ Remove ID column (VERY IMPORTANT)
if 'customerID' in df.columns:
    df.drop('customerID', axis=1, inplace=True)

# ✅ Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing values
df.loc[:, 'TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())


# ✅ Convert target column
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})

# ✅ Identify categorical columns ONLY
cat_cols = df.select_dtypes(include=['object', 'string']).columns

# Encode only categorical columns ( getting warnings due to dumies because of internal pandas )
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# Define X and y
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open(os.path.join(BASE_DIR, 'model.pkl'), 'wb'))

with open(os.path.join(BASE_DIR, 'columns.json'), 'w') as f:
    json.dump(list(X.columns), f)
print("Total columns:", len(df.columns))

print("✅ Clean model created!")

print("Check line executed")
