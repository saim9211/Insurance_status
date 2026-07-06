from pathlib import Path
from pickle import load

from fastapi import FastAPI, HTTPException

from model.predict import predict_output
from schema.user_data import InputData

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

with MODEL_PATH.open("rb") as f:
    model = load(f)

app = FastAPI(title="Insurance Prediction API", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Prediction API. Use the /pred endpoint to make predictions."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/pred")
def predict(input_data: InputData):
    user_input = {
        "age_group": input_data.age_category,
        "sex": input_data.sex,
        "bmi": input_data.bmi,
        "children": input_data.children,
        "smoker": input_data.smoker,
        "region_group": input_data.region_category,
    }

    try:
        prediction = predict_output(user_input)
        return {"prediction": prediction}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc