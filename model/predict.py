from pickle import load
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model = load(f)


def _normalize_user_data(user_data: dict) -> dict:
    normalized = dict(user_data)

    if "age_group" not in normalized and "age" in normalized:
        age = normalized["age"]
        if age < 18:
            normalized["age_group"] = "under age"
        elif age < 35:
            normalized["age_group"] = "best age"
        else:
            normalized["age_group"] = "over_age"

    if "region_group" not in normalized and "region" in normalized:
        region = normalized["region"]
        normalized["region_group"] = "south" if region in {"southeast", "southwest"} else "north"

    if "bmi_category" not in normalized and "bmi" in normalized:
        bmi = normalized["bmi"]
        if bmi < 18.5:
            normalized["bmi_category"] = "Underweight"
        elif bmi < 25:
            normalized["bmi_category"] = "Normal weight"
        elif bmi < 30:
            normalized["bmi_category"] = "Overweight"
        else:
            normalized["bmi_category"] = "Obese"

    return normalized


def predict_output(user_data: dict):
    prepared_data = _normalize_user_data(user_data)
    data = pd.DataFrame([prepared_data])

    expected_columns = list(getattr(model, "feature_names_in_", []))
    if expected_columns:
        data = data.reindex(columns=expected_columns)

    prediction = model.predict(data)
    return prediction[0]

