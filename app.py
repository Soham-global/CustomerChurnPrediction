from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

#changed
import os
from datetime import datetime#for showing datetime

import requests
import json      # For formatting JSON


# WSGI
app = Flask(__name__)

# Load the trained model and encoders
rf_model = joblib.load('model/rf_model_tuned.pkl')
label_encoders = joblib.load('model/label_encoders.pkl')

# Selected features (same as you used in your tuned model)
selected_features = ['Age', 'State', 'Number_of_Referrals', 'Tenure_in_Months', 'Value_Deal',
                     'Internet_Service', 'Internet_Type', 'Online_Security',
                     'Premium_Support', 'Contract', 'Paperless_Billing', 'Payment_Method',
                     'Monthly_Charge', 'Total_Charges', 'Total_Extra_Data_Charges',
                     'Total_Long_Distance_Charges', 'Total_Revenue']

# Define categorical columns based on your dataset
categorical_columns = ['State', 'Value_Deal', 'Internet_Service', 'Internet_Type',
                       'Online_Security', 'Premium_Support', 'Contract',
                       'Paperless_Billing', 'Payment_Method']

# Numeric columns
numeric_columns = ['Age', 'Number_of_Referrals', 'Tenure_in_Months',
                   'Monthly_Charge', 'Total_Charges', 'Total_Extra_Data_Charges',
                   'Total_Long_Distance_Charges', 'Total_Revenue']


#changed 

POWERBI_PUSH_URL = "https://api.powerbi.com/beta/ca43080f-e4c8-47a5-90bc-bcac0d1979ff/datasets/cf5ed4bf-9a9b-4397-b2eb-4b6401db892a/rows?experience=power-bi&key=ZK6e5uND9G8pkoVzuZh34QOwuYZSkHKmC6so%2FKQ20%2BOtq%2BkqQuUIxhovu45cCTqK%2FT0lPguLAWhdxK91u3vmTw%3D%3D"



def push_to_powerbi(input_dict, prediction_result):
    input_dict['Prediction'] = prediction_result
    input_dict['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = [input_dict]

    try:
        # Just push the new row (no delete)
        print("=== Payload being sent to Power BI ===")
        print(json.dumps(payload[0], indent=4))

        response = requests.post(POWERBI_PUSH_URL, json=payload)
        response.raise_for_status()
        print("✅ Data pushed to Power BI successfully.")
    except requests.exceptions.RequestException as e:
        print("❌ Power BI update failed:", e)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {feature: request.form.get(feature) for feature in selected_features}
    input_df = pd.DataFrame([input_data])

    for col in numeric_columns:
        input_df[col] = input_df[col].astype(float)

    for col in categorical_columns:
        input_df[col] = label_encoders[col].transform(input_df[col])

    prediction = rf_model.predict(input_df)
    result = 'Churned' if prediction[0] == 1 else 'Stayed'

    input_original = input_data.copy()
    for col in categorical_columns:
        input_original[col] = label_encoders[col].inverse_transform([input_df[col][0]])[0]

    # Push to Power BI
    push_to_powerbi(input_original, result)

    return render_template(
        'result.html',
        prediction=result,
    )


if __name__ == '__main__':
    app.run(debug=True)