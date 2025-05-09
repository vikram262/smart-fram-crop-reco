import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the trained model
model = joblib.load('crop_recommendation_model.pkl')

# Load the district-wise rainfall data
district_rainfall_df = pd.read_parquet('district_wise_rainfall_normal.parquet')

# Load the label encoder
label_encoder = joblib.load('label_encoder.pkl')

# Function to display the homepage
def show_homepage():
    st.session_state.page = "Crop Recommendation"

# Function to display the crop recommendation page
def show_crop_recommendation():
    st.title("Crop Recommendation")

    # District selection
    district = st.selectbox("Select District", district_rainfall_df['DISTRICT'].unique())

    # Month selection
    month = st.selectbox("Select Month", ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])

    # Auto-fill rainfall based on selected district and month
    district_data = district_rainfall_df[district_rainfall_df['DISTRICT'] == district].iloc[0]
    rainfall = district_data[month]

    # Display auto-filled rainfall
    st.write(f"Rainfall (mm): {rainfall}")

    # Input fields for N, P, K, pH, temperature, and humidity
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=100, value=50)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=100, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=100, value=50)
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
    temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)

    # Predict button
    if st.button("Predict"):
        # Create a DataFrame for the input
        input_data = pd.DataFrame({
            'N': [N],
            'P': [P],
            'K': [K],
            'temperature': [temperature],
            'humidity': [humidity],
            'ph': [ph],
            'rainfall': [rainfall]
        })
        
        # Make prediction
        prediction_probs = model.predict_proba(input_data)
        prediction_classes = model.classes_
        
        # Create a DataFrame for the prediction probabilities
        prediction_df = pd.DataFrame(prediction_probs, columns=label_encoder.inverse_transform(prediction_classes))
        
        # Get the top N recommendations
        top_n = 5  # You can change this value to get more or fewer recommendations
        top_recommendations = prediction_df.T.sort_values(by=0, ascending=False).head(top_n)
        
        # Display the top N recommendations
        st.write("Top Crop Recommendations:")
        for i, (crop, score) in enumerate(top_recommendations.iterrows(), start=1):
            st.write(f"{i}. {crop} (Confidence: {score.values[0] * 100:.2f}%)")

    if st.button("Back to Home"):
        st.session_state.page = "Home"

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Crop Recommendation"  # Set default page to Crop Recommendation

# Display the appropriate page based on the session state
if st.session_state.page == "Home":
    show_homepage()
elif st.session_state.page == "Crop Recommendation":
    show_crop_recommendation()
    
