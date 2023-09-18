# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
loaded_model = pickle.load(open('C:/Users/hp/Desktop/Python/diabetes_model.sav','rb'))

input_data=(6,148,72,35,0,33.6,0.627,50)
#change input data to a numpy array
num_arr = np.asarray(input_data)
#reshape the numpy array
input_data_reshape = num_arr.reshape(1,-1)
#Standardise the data
#std_data = scaler.transform(input_data_reshape)

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if prediction[0]==0:
    print('DOES NOT HAVE DIABETES')
else:
    print('HAVE DIABETES')

