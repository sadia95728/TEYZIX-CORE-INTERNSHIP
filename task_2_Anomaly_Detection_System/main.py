from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="TEYZIX Core Anomaly Detection System",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Anomaly Detection API is running"}