from fastapi import FastAPI,HTTPException
from model.predict import predict_output
from schema.user_data import InputData
from pickle import load
import pandas as pd


with open("model/model.pkl", "rb") as f:
    model = load(f)


app = FastAPI()


@app.get("/")                 
def home():
    return {"message": "Welcome to the Insurance Prediction API. Use the /pred endpoint to make predictions."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/pred")
def predict(input_data: InputData):
    user_input={
        'age_group': input_data.age_category,
        'sex': input_data.sex,
        'bmi': input_data.bmi,
        'children': input_data.children,
        'smoker': input_data.smoker,
        'region_group': input_data.region_category
    }

    try:
        prediction = predict_output(user_input)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))