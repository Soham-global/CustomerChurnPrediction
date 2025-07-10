# 📊 Customer Churn Prediction (Telecom Industry)

A machine learning–powered web application that predicts whether a telecom customer will churn, with real-time dashboard integration using Power BI and Flask.

---

## 🌟 Features

- 🔍 Data cleaning performed using **SQL** on raw Excel data
- 🌲 Machine Learning model built using **Random Forest Classifier**
- 🌐 Web interface built with **Flask**
- 🔁 Real-time predictions via **REST API**
- 📈 Live **Power BI dashboard** embedded directly in the web app using `iframe`
- ⏱️ Dashboard updates in **real time** using **timestamp** and **Top N filter**

---

## 🗂️ Project Structure

CustomerChurnPrediction/
│
├── Dataset.xlsx # Raw telecom dataset
├── Cleaned_Data.xlsx # Cleaned data (via SQL)
├── model.pkl # Trained ML model
├── app.py # Main Flask application
├── requirements.txt # List of Python dependencies
├── static/
│ └── style.css # CSS styling
├── templates/
│ ├── index.html # Main page with Power BI dashboard
│ └── result.html # Output page showing predictions
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧰 Tech Stack

- **Python** (ML model, Flask API)
- **SQL** (data cleaning)
- **Scikit-learn** (Random Forest)
- **Flask** (web framework)
- **Power BI Online** (dashboard + REST API)
- **HTML / CSS** (frontend)
- **GitHub + Render** (deployment)

---

## 🔄 Real-Time Flow Overview

1. User fills form with customer data.
2. Flask app predicts churn using the trained ML model.
3. Prediction result is shown on the site instantly.
4. The result is also pushed via **REST API** to Power BI’s **streaming dataset**.
5. Dashboard gets updated in real time using **timestamp** and **Top N filter**.
6. Live Power BI dashboard is embedded inside `index.html` via `iframe`.

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CustomerChurnPrediction.git
cd CustomerChurnPrediction
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
3. Activate Environment
On Windows:

bash
Copy
Edit
venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Run the Flask App
bash
Copy
Edit
python app.py
Then go to http://127.0.0.1:5000/ in your browser.
```

📊 Power BI Setup
Report is created using Power BI Online Service
Streaming dataset configured to accept live data via REST API
Timestamp and Top N filter ensure only the latest records are displayed
Embedded in the site using an iframe in index.html
Make sure your Power BI report is shared publicly or with required access for iframe to work.

🚀 Deployment Notes
Project can be hosted using Render, Heroku, or any Flask-compatible host.
If using Render, connect the repo and enable auto-deploy from main branch.

💡 Future Enhancements
Add user login system
Logging & monitoring with logs dashboard
Option to export prediction history to Excel or CSV










Ask ChatGPT
