# import numpy as np
# import pickle


# #  Loading the Saved Model.
# loaded_model = pickle.load(open("diabetes_model.sav", "rb"))

# # input_data = (4,110,92,0,0,37.6,0.191,30)
# input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)

# #  changing the input_data into the numpy array.
# input_data_as_np = np.array(input_data)

# #  now change the dimensions of the numpy array
# reshaped_array = input_data_as_np.reshape(1, -1)

# # # Standardized the input data.
# # std_data = scalar.transform(reshaped_array)

# prediction = loaded_model.predict(reshaped_array)

# if prediction[0] == 1:
#     print("The Person Suffered by Diabetes")
# else:
#     print("The Person dont have the Diabetes")


import numpy as np
import streamlit as st
import pandas as pd
import sys

print("Numpy version:", np.__version__)
print("Streamlit version:", st.__version__)
print("Pandas version:", pd.__version__)
print("Python version:", sys.version)
