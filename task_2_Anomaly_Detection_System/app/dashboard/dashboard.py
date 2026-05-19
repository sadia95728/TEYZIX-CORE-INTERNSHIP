import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title="Anomaly Dashboard", layout="wide")

st.title("🚨 Real-Time Anomaly Detection Dashboard")

API_URL = "http://127.0.0.1:8000/stream"

if "data" not in st.session_state:
    st.session_state.data = []

if st.button("Start Streaming"):

    try:
        response = requests.get(API_URL, stream=True)

        for line in response.iter_lines():

            if line:
                record = json.loads(line.decode("utf-8"))

                st.session_state.data.append(record)

                df = pd.DataFrame(st.session_state.data)

                st.subheader("Live Data")

                st.dataframe(df, use_container_width=True)

                st.subheader("Latest Point")

                st.write(record)

    except Exception as e:
        st.error(f"Connection failed: {e}")