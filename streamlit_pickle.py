import streamlit as st
import pandas as pd
import numpy as np
import pickle

#Streamlit Page Creation
st.set_page_config(page_title='Diabetes Prediction',
                layout='wide',initial_sidebar_state='expanded')
st.title(':blue[&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;👨‍⚕️**Diabetes Prediction** 💉 💊]')
st.header('Enter the following details:')
Name=st.text_input('Enter your name')
gender=st.selectbox('Gender',['Female', 'Male', 'Other'])
if gender == 'Female':
    gender=0
elif gender == 'Male':
    gender=1
else:
    gender=2
age=st.number_input('Age',min_value=0,max_value=120)
hypertension=st.selectbox('Hyper tension',['Yes', 'No'])
if hypertension == 'Yes':
    hypertension=1
else:
    hypertension=0
heart_disease=st.selectbox('Heart disease',['Yes', 'No'])
if heart_disease == 'Yes':
    heart_disease=1
else:
    heart_disease=0
smoking_history=st.selectbox('Smoking history',['never', 'No Info', 'current', 'former', 'ever', 'not current'])
if smoking_history=='never':
    smoking_history=4
elif smoking_history=='No Info':
    smoking_history=0
elif smoking_history=='current':
    smoking_history=1
elif smoking_history=='former':
    smoking_history=3 
elif smoking_history=='ever':
    smoking_history=2
else:
    smoking_history=5

bmi=st.text_input('BMI')
HbA1c_level=st.text_input('Hemoglobin A1C level')
blood_glucose_level=st.number_input('Blood glucose level',min_value=0,max_value=500)

# Ensure inputs are in the correct format
try:
        bmi=float(bmi)
        HbA1c_level=float(HbA1c_level)
except ValueError:
        st.error("BMI and Hemoglobin A1C level must be numeric.")
        st.stop()

# Load the trained model (make sure to provide the correct path to your model file)
file_path="C:/Users/user/OneDrive/Desktop/Data Science Project/Diabetes/diabetes_result"
diabetes_model= pickle.load(open(file_path,'rb'))

# Button and session state logic
Get_data= st.button('Get your result')
if "Get_state" not in st.session_state:
    st.session_state.Get_state = False
if Get_data or st.session_state.Get_state:
    st.session_state.Get_state = True
# Ensure inputs are in the correct format and check for missing values
    missing_input = False
    if not Name:
        st.error("Name is required.")
        missing_input = True
    if not bmi:
        st.error("BMI is required.")
        missing_input = True
    if not HbA1c_level:
        st.error("Hemoglobin A1C level is required.")
        missing_input = True

    if missing_input:
        st.stop()

# Ensure inputs are in the correct format
    input=np.array([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
# Make prediction
    input_predict=diabetes_model.predict(input)
# Display result
    if input_predict==1:
        st.header(f'''Unfortunately, {Name}, you have tested positive for diabetes.''')
    else:
        st.header(f'''Good news, {Name}, you do not have diabetes.''')


