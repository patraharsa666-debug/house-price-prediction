import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")

if st.button("Predict Price"):

    data = np.array([[area, bedrooms, bathrooms, stories,
                      1, 0, 0, 0, 1, 2, 1, 1, 0, 0]])

    prediction = model.predict(data)

    st.success(f"Predicted Price: ₹{prediction[0]:,.0f}")
