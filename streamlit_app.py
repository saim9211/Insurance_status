import streamlit as st
from model.predict import predict_output

st.set_page_config(page_title="Insurance Prediction", page_icon="💡", layout="centered")
st.title("Insurance Charges Prediction")
st.write("Use this form to generate a prediction directly with the trained model.")

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

    try:
        prediction_value = predict_output(payload)
        formatted = f"{float(prediction_value):,.2f}"
        st.success("Prediction received")
        st.metric(label="Estimated Insurance Charge", value=f"${formatted}")
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")


