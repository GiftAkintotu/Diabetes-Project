import streamlit as st
import joblib
import numpy as np

new_diabetes_model = joblib.load('new_diabetes_model.pkl')
new_scaler = joblib.load('new_scaler.pkl')

st.title('Diabetes Prediction')

glucose = st.number_input('Glucose',0)
bmi = st.number_input('BMI', min_value= 0.0,step=0.1, format="%.1f")
age = st.number_input('Age',0)
pregnancies = st.number_input('Pregnancies',0)


input_data = [glucose,bmi,age,pregnancies]

if st.button('Prediction'):
    scaled = new_scaler.transform([input_data])
    prediction = new_diabetes_model.predict(scaled)[0]
    prob = new_diabetes_model.predict_proba(scaled)[0][1]
    st.success(f"Prediction:{'Diabetic' if prediction else 'Not Diabetic'} (Confidence: {prob: 2f})")
