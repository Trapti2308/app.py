
import streamlit as st

st.title("House Price Prediction App 🏠")
st.write("Enter the details below to predict the price of a house.")

# User Inputs
location = st.selectbox("Select Location", ['Location1', 'Location2', 'Location3'])
square_footage = st.number_input("Enter Square Footage", min_value=100, max_value=10000, step=50)
num_bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=10, step=1)
num_bathrooms = st.slider("Number of Bathrooms", min_value=1, max_value=10, step=1)

# Prediction (Placeholder Logic)
if st.button("Predict Price"):
    price = square_footage * 100  # Example: Replace with model prediction
    st.success(f"The predicted price of the house is: ${price:,.2f}")
