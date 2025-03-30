import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# title 
st.title("🏡 House Price Prediction")

# Input Filed 
lot_area = st.number_input("Lot Area (sq.ft)",min_value=500,max_value=100000,step=100)

year_built = st.number_input("Year Built(yy)", min_value=1800, max_value=2024, step=1)

full_bath = st.number_input("Full Bathroom",min_value=0,max_value=5,step=1)

bedrooms = st.number_input("Bedrooms",min_value=1 , max_value=10,step=1)

garage = st.number_input("Garage ", min_value=0, max_value=5, step=1)



# Predict button
if st.button("Predict Price"):
    features = np.array([[lot_area, year_built, full_bath, bedrooms, garage]])
    prediction = model.predict(features)
    st.success(f"🏠 Estimated House Price: ${prediction[0]:,.2f}")