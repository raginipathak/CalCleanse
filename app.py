import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("CalCleanse – Track the Burn🔥")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1)
height = st.number_input("Height (cm)", min_value=50)
weight = st.number_input("Weight (kg)", min_value=10)
duration = st.number_input("Exercise Duration (mins)", min_value=1)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200)
body_temp = st.number_input("Body Temp (°C)", min_value=35.0, max_value=42.0, step=0.1)

if st.button("Predict"):
    gender_val = 0 if gender == "Male" else 1
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    result = model.predict(input_data)
    st.success(f"✅ Estimated Calories Burnt: {result[0]:.2f} kcal")
