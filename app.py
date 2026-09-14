import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

# Load model and scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load('models/fraud_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

model, scaler = load_artifacts()

# App Header
st.title("🛡️ FraudShield: Credit Card Fraud Detection")
st.markdown("An end-to-end machine learning application designed to detect fraudulent credit card transactions in real-time.")

st.sidebar.header("Transaction Parameters")

# Input fields for user (Time, Amount, and V1-V28 PCA features)
def user_input_features():
    time = st.sidebar.number_input("Transaction Time (Seconds elapsed)", value=0.0)
    amount = st.sidebar.number_input("Transaction Amount ($)", value=50.0)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Anonymized PCA Features (V1 - V28)")
    
    features = {'Time': time, 'Amount': amount}
    
    # Adding simplified inputs for V1-V28 (defaulting to 0.0 representing mean/median)
    for i in range(1, 29):
        features[f'V{i}'] = st.sidebar.slider(f'V{i}', float(-30.0), float(30.0), float(0.0))
        
    return pd.DataFrame(features, index=[0])

input_df = user_input_features()

# Main Panel Display
st.subheader("User Input Transaction Summary")
st.dataframe(input_df)

if st.button("Predict Fraud Status", type="primary"):
    # Scale Time and Amount using the saved scaler
    input_df[['Time', 'Amount']] = scaler.transform(input_df[['Time', 'Amount']])
    
    # Ensure columns match the exact order the model was trained on
    input_df = input_df[model.feature_names_in_]
    
    # Prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    st.markdown("---")
    st.subheader("Prediction Results")
    
    if prediction[0] == 1:
        st.error(f"⚠️ **Alert! High Fraud Probability Detected!** (Confidence: {prediction_proba[0][1]*100:.2f}%)")
    else:
        st.success(f"✅ **Transaction Appears Legitimate.** (Fraud Probability: {prediction_proba[0][1]*100:.2f}%)")