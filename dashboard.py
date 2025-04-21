import os
import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function: System Metrics
def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk


# Function: Anomaly Detection
def detect_anomalies(data):
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    anomalies = model.predict(data)
    return anomalies

# Function: Predictive Alerts (Stub)
def generate_predictive_alerts(data):
    alerts = ["No alerts"] * len(data)
    return alerts


# Function: Email Alerts
def send_email_alert(subject, body, to_email):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, [to_email], msg.as_string())
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error: unable to send email - {e}")

# -------------------------
# Function: Log Analysis
# -------------------------
def analyze_logs(logs):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(logs)
    model = IsolationForest(contamination=0.1)
    model.fit(X)
    anomalies = model.predict(X)
    return anomalies

# -------------------------
st.set_page_config(layout="wide")
st.title("🧠 AIOps Dashboard")

# Background Image
st.markdown("""
    <style>
        body {
            background-image: url('https://www.alcortech.com/wp-content/uploads/2023/05/Generative-AIOps_LinkedIn-1.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(0, 0, 0, 0.6); /* Slight transparent overlay */
            padding: 20px;
            border-radius: 12px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout Selection
layout = st.selectbox("Select Layout", ["Default", "Compact", "Expanded"])
st.write(f"{layout} layout selected")

# Get real-time metrics
cpu, memory, disk = get_system_metrics()

# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("CPU Usage", f"{cpu}%")
    st.metric("Memory Usage", f"{memory}%")
    st.metric("Disk Usage", f"{disk}%")

# Anomaly Detection
data = pd.DataFrame({'metric': [cpu, memory, disk]})
anomalies = detect_anomalies(data)
with col2:
    st.write("Detected Anomalies:")
    st.write(anomalies)

# Predictive Alerts
alerts = generate_predictive_alerts(data)
with col3:
    st.write("Predictive Alerts:")
    st.write(alerts)

# Email Alert Example (optional)
if st.button("Send Test Email Alert"):
    send_email_alert("AIOps Alert", "CPU usage is high", "your-receiver-email@gmail.com")

# Historical Data Trends
st.subheader("📈 Historical Data Trends")
historical_data = pd.DataFrame({
    'Time': pd.date_range(start='2025-04-20', periods=10, freq='h'),
    'CPU': [cpu + i for i in range(10)],
    'Memory': [memory + i for i in range(10)],
    'Disk': [disk + i for i in range(10)]
})
fig = px.line(historical_data, x='Time', y=['CPU', 'Memory', 'Disk'], labels={'value': 'Usage (%)'})
st.plotly_chart(fig)

# Security Log Analysis
st.subheader("🛡️ Security Log Anomaly Detection")
logs = [
    "User login from IP 192.168.1.1",
    "Failed login attempt from IP 192.168.1.2"
]
log_anomalies = analyze_logs(logs)
st.write("Security Anomalies:", log_anomalies)
