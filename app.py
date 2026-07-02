from pathlib import Path
from typing import Annotated, Literal,Optional
import json
import pickle

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field,field_validator

with open('random_forest_model_pipeline.pkl', 'rb') as f:
            modal = pickle.load(f)
       

app = FastAPI()

class InputData(BaseModel):
    
    age: Annotated[int, Field(ge=0, le=120, description="Age of the individual in years")]
    sex:Annotated[Literal["male", "female"], Field(description="Sex of the individual")]
    bmi: Annotated[float, Field(ge=0, description="Body mass index")]
    children: Annotated[int, Field(ge=0, description="Number of children")]
    smoker: Annotated[Literal["yes", "no"], Field(description="Whether the individual is a smoker")]
    region: Annotated[Literal["northeast", "northwest", "southeast", "southwest"], Field(description="Region of the individual")]
    charges: Annotated[float, Field(ge=0, description="Medical insurance charges")]

    @computed_field
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    @computed_field
    @property
    def smoker_status(self) -> str:
        return "Smoker" if self.smoker == "yes" else "Non-smoker"
    @field_validator("data",mode="before")
    @classmethod
    def validate_data(cls, value):
        if not isinstance(value, dict):
            raise ValueError("Input data must be a dictionary.")
        return value
    
@app.post("/predict")
def predict(input_data: InputData):
    data=DataFrame([input_data.dict()])
    try:
        prediction = modal.predict(data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
