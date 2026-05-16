from fastapi import FastAPI
from src.recommender import hybrid_recommend

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hybrid Recommendation API is working "}

@app.get("/recommend/{user_id}")
def recommend(user_id: str):

    try:
        results = hybrid_recommend(user_id)

        return {
            "user_id": user_id,
            "recommendations": results.to_dict(orient="records")
        }

    except Exception as e:

        return {
            "user_id": user_id,
            "error": str(e),
            "recommendations": []
        }