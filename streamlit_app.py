import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/pred"

st.set_page_config(page_title="Insurance Prediction", page_icon="💡", layout="centered")
st.title("Insurance Charges Prediction")
st.write("Use this form to send input data to your prediction API and display a formatted result.")

with st.form("prediction_form"):
    age = st.number_input("Age", min_value=0, max_value=120, value=40)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI", min_value=0.0, value=28.5, step=0.1, format="%.2f")
    children = st.number_input("Children", min_value=0, value=0)
    smoker = st.selectbox("Smoker", ["no", "yes"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
    submit_button = st.form_submit_button("Predict")

if submit_button:
    payload = {
        "age": int(age),
        "sex": sex,
        "bmi": float(bmi),
        "children": int(children),
        "smoker": smoker,
        "region": region,
    }

    st.info(f"Sending request to: {API_URL}")

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        prediction_data = response.json()

        if "prediction" not in prediction_data:
            st.error("API response did not include a prediction.")
        else:
            prediction_value = prediction_data["prediction"]
            formatted = f"{prediction_value:,.2f}"
            st.success("Prediction received")
            st.metric(label="Estimated Insurance Charge", value=f"${formatted}")
            with st.expander("Raw API response"):
                st.json(prediction_data)
    except requests.exceptions.RequestException as exc:
        st.error(f"Request failed: {exc}")
    except ValueError:
        st.error("Unable to parse API response as JSON.")
