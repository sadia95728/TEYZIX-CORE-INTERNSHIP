from app.alerts.notifiers import send_alert
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.database.db import SessionLocal
from app.database.models import Anomaly

import pandas as pd
import json
import time

from app.ml.preprocessing import preprocess
from app.ml.statistical import detect_anomalies_zscore
from app.ml.isolation_forest import detect_anomalies_isolation_forest
from app.ml.pyod_model import detect_anomalies_pyod


router = APIRouter()

DATA_PATH = "dataset/raw/cpu_utilization_asg_misconfiguration.csv"

BASE_DF = pd.read_csv(DATA_PATH)

MEAN = float(BASE_DF["value"].mean())
STD = float(BASE_DF["value"].std())


@router.get("/load-data")
def load_data():
    return {
        "rows": len(BASE_DF),
        "columns": list(BASE_DF.columns)
    }


@router.get("/zscore")
def zscore_detection():

    df = preprocess(BASE_DF.copy())
    result = detect_anomalies_zscore(df)

    return {
        "total_anomalies": int(len(result[result["anomaly"] == True]))
    }

@router.get("/isolation")
def isolation_detection():

    df = preprocess(BASE_DF.copy(), scale=True)
    result = detect_anomalies_isolation_forest(df)

    return {
        "total_anomalies": int(len(result[result["anomaly"] == True]))
    }


@router.get("/pyod")
def pyod_detection():

    df = preprocess(BASE_DF.copy(), scale=True)
    result = detect_anomalies_pyod(df)

    return {
        "total_anomalies": int(len(result[result["anomaly"] == True]))
    }

@router.get("/stream")
def stream_data():

    db = SessionLocal()   

    def is_zscore_anomaly(value: float) -> bool:
        if STD == 0:
            return False
        return abs((value - MEAN) / STD) > 3


    def generate():

        for _, row in BASE_DF.head(20).iterrows():

            value = float(row["value"])

            z_flag = bool(is_zscore_anomaly(value))

            iso_flag = bool(
                value > MEAN + 2 * STD
                or value < MEAN - 2 * STD
            )

            anomaly = bool(z_flag or iso_flag)


            record = Anomaly(
                timestamp=str(row["timestamp"]),
                value=value,
                anomaly=int(anomaly),
                zscore_flag=int(z_flag),
                isolation_flag=int(iso_flag)
            )

            db.add(record)
            db.commit()

            if anomaly:
                try:
                    send_alert({
                        "timestamp": str(row["timestamp"]),
                        "value": value,
                        "anomaly": anomaly,
                        "zscore_flag": z_flag,
                        "isolation_flag": iso_flag
                    })
                except Exception as e:
                    print("Alert error:", e)

        
            yield json.dumps({
                "timestamp": str(row["timestamp"]),
                "value": value,
                "anomaly": anomaly,
                "zscore_flag": z_flag,
                "isolation_flag": iso_flag
            }) + "\n"

            time.sleep(0.05)


    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson"
    )