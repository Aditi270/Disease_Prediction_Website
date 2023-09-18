# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 03:02:31 2023

@author: hp
"""


import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/hp/Desktop/Python/diabetes_model.sav','rb'))

#Function for pred
def diabetes_pred(input_data):
    
#change input data to a numpy array
    num_arr = np.array(input_data)
#reshape the numpy array
    input_data_reshape = num_arr.reshape(1,-1)
#Standardise the data
    #std_data = scaler.transform(input_data_reshape)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if prediction[0]==0:
        
        return('DOES NOT HAVE DIABETES')
    else:
        return('HAVE DIABETES')
    
    
def main():
    
    #Giving a title
    st.title = ("Diabetes Prediction web app")
    
    #getting the input data from user
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("SkinThickness value")
    Insulin = st.text_input("Insulin Level value")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Func value")
    Age = st.text_input("Enter age of patient")
    
    #Code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __main__ == '__main__':
    main()
    
    
    
    