import numpy as np
import pandas as pd
import streamlit as st
import pickle

# loaded_model = pickle.load(
#     open(
#         r"C:\\Users\\USER\\OneDrive\\Desktop\\Github\\Deployed_Project\\Deployed_Machine_Learning_Models\\001_Diabetes_Model_Prediction\\diabetes_model.pkl",
#         "rb",
#     )
# )
# model_path = r"C:\\Users\\USER\\OneDrive\\Desktop\\Github\\Deployed_Project\\Deployed_Machine_Learning_Models\\001_Diabetes_Model_Prediction\\diabetes_model.pkl"
model_path = "diabetes_model.pkl"
loaded_model = pickle.load(open(model_path, "rb"))

# print(loaded_model)


#  Creating the function for prediction.
def diabetes_prediction(new_data):
    #  changing the input_data into the numpy array.
    input_data_as_np = np.array(new_data)

    #  now change the dimensions of the numpy array
    reshaped_array = input_data_as_np.reshape(1, -1)

    # Standardized the input data.
    # std_data = scalar.transform(reshaped_array)

    prediction = loaded_model.predict(reshaped_array)
    print(prediction)

    if prediction[0] == 0:
        return "The person is not Diabetic"
    else:
        return "The person is Diabetic"


# #  Call the function.
# new_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)
# diabetes_prediction(new_data)


def main():
    # Giving the title for the Project.
    st.title("Diabetes Prediction Model")
    # "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
    # "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("BloodPressure Value")
    SkinThickness = st.text_input("SkinThickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")
    Age = st.text_input("Person Age")

    #  The Code for the Prediction.
    diagnosis = ""

    #  Creation a button for Prediction.
    if st.button("Diabetes Test"):
        diagnosis = diabetes_prediction(
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]
        )
    if diagnosis != "":
        st.success(diagnosis)


if __name__ == "__main__":
    main()
