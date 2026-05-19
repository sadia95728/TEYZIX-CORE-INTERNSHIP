# 🚨 Real-Time Anomaly Detection System

A full-stack anomaly detection pipeline that processes time-series CPU utilization data in real-time using statistical methods and machine learning models. The system includes FastAPI backend, Streamlit dashboard, and database storage for historical anomaly tracking.

## 📌 Features

- Real-time / near real-time data streaming
- Multiple anomaly detection methods:
  - Statistical Method (Z-Score)
  - Machine Learning (Isolation Forest - Scikit-learn)
  - PyOD-based anomaly detection
- Alerting system for detected anomalies
- Streamlit dashboard for visualization
- Database storage for historical anomaly records
- Modular and scalable architecture


## 📊 Dataset

- CPU utilization time-series dataset provided for evaluation
- Columns:
  - timestamp
  - value (CPU usage metric)

The dataset is processed in real-time to simulate metric ingestion.


## 🏗️ System Architecture

1. Data Ingestion Layer (CSV-based streaming simulation)
2. Processing Layer (Preprocessing + ML models)
3. Detection Layer (Statistical + ML + PyOD)
4. Alerting Layer (Console/log-based alerts)
5. Storage Layer (SQLite/PostgreSQL for anomaly records)
6. Visualization Layer (Streamlit dashboard)


## ⚙️ Tech Stack

- Python 3.10+
- FastAPI
- Pandas, NumPy
- Scikit-learn
- PyOD
- Streamlit
- SQLAlchemy
- SQLite / PostgreSQL



## 🚀 API Endpoints

### Data Loading
GET /load-data

### Anomaly Detection
GET /zscore
GET /isolation
GET /pyod

### Real-Time Streaming

GET /stream

Returns live processed data with anomaly flags.

## 📡 Real-Time Streaming Output Example


app/
│── api/
│   └── routes.py
│
│── ml/
│   ├── preprocessing.py
│   ├── statistical.py
│   ├── isolation_forest.py
│   └── pyod_model.py
│
│── database/
│   ├── db.py
│   └── models.py
│
│── alerts/
│   └── notifiers.py
│
│── dashboard/
│   └── dashboard.py

dataset/
└── raw/
    └── cpu_utilization_asg_misconfiguration.csv

main.py




