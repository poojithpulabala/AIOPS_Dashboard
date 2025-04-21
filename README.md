# AIOps Dashboard

AIOps Dashboard is a real-time monitoring and anomaly detection tool designed to provide insights into system metrics (CPU, memory, disk usage) and perform predictive analytics. 
The application uses machine learning models for anomaly detection and generates predictive alerts. 
Additionally, it can send email alerts in case of critical system performance issues and can analyze security logs for anomalies.

## Features

- **Real-time System Metrics**: Displays real-time CPU, memory, and disk usage.
- **Anomaly Detection**: Identifies anomalies in system metrics and security logs using the Isolation Forest algorithm.
- **Predictive Alerts**: Stub implementation for generating predictive alerts.
- **Email Alerts**: Sends email alerts when system metrics cross predefined thresholds.
- **Historical Data Trends**: Displays trends of system metrics over time using Plotly for visualization.
- **Security Log Analysis**: Analyzes security logs and identifies anomalies in login attempts.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- Psutil
- Python-dotenv
