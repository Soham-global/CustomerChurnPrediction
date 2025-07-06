from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = {}
    for feature in selected_features:
        input_data[feature] = request.form.get(feature)

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Convert numeric columns to float
    for column in numeric_columns:
        input_df[column] = input_df[column].astype(float)

    # Apply label encoding to categorical columns
    for column in categorical_columns:
        input_df[column] = label_encoders[column].transform(input_df[column])

    # Predict
    prediction = rf_model.predict(input_df)

    # Map prediction to label
    result = 'Churned' if prediction[0] == 1 else 'Stayed'

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
