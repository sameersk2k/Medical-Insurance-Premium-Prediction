import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIP.pkl', 'rb'))

# Function to map user inputs to model features
def map_user_inputs(gender, smoker, region, age, bmi, children):
    # Encode gender
    gender_encoded = 1 if gender == 'Male' else 0
    
    # Encode smoker
    smoker_encoded = 1 if smoker == 'Yes' else 0
    
    # Map region
    region_mapping = { 'NorthEast': [1, 0, 0, 0], 'NorthWest': [0, 1, 0, 0],'SouthEast': [0, 0, 1, 0], 'SouthWest': [0, 0, 0, 1]}
    region_encoded = region_mapping[region]
    
    return [age, bmi, children, gender_encoded, smoker_encoded] + region_encoded

# Function to make prediction
def predict_premium(features):
    return model.predict([features])[0]

st.header('Medical Insurance Premium Predictor')


gender = st.selectbox('Choose Gender',['Male','Female'])
smoker = st.selectbox('Are you a smoker ?',['Yes','No'])
region = st.selectbox('Choose Region',['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider('Enter Age:',5,80)
bmi = st.slider('Enter BMI',10,70)
children = st.slider('Choose No of Children',0,5)

if st.button('Predict Premium'):
    # Map user inputs to model features
    features = map_user_inputs(gender, smoker, region, age, bmi, children)
    
    # Make prediction
    predicted_premium = predict_premium(features)
    
    # Display prediction
    st.markdown(f'### Estimated Medical Insurance Premium: '+
                f'<span style="color:green;font-weight:bold;font-size:30px;">${round(predicted_premium, 2)}</span>', unsafe_allow_html=True)
