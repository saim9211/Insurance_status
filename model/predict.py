from pickle import load
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model = load(f)

def predict_output(user_data:dict):
    data=pd.DataFrame([user_data])
    prediction = model.predict(data)
    return prediction[0]
        
