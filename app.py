import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("Streamlit App Example with Map")

# Example dataset for the map
st.header("Map Visualization Example")
st.write("This example shows a map with random latitude and longitude points.")

# Create random latitude and longitude points
data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.77, -122.42],  # Centered around San Francisco
    columns=["lat", "lon"]
)

# Display the map
st.map(data)

# Other Streamlit functionalities
st.header("Simple Streamlit Components")

# Text input
name = st.text_input("Enter your name", "")
if name:
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df)

# Conclusion
st.write("This app demonstrates a simple map visualization and interactive components using Streamlit.")
