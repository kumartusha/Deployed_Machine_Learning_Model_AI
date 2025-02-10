import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np


#  Load the Models.

diabetes_model = pickle.load(
    open(
        "002_multiple_diabetes.pkl",
        "rb",
    )
)
parkinson_disease = pickle.load(
    open(
        "002_multiple_parkinson.pkl",
        "rb",
    )
)
heart_disease = pickle.load(
    open(
        "002_multiple_heart_disease.pkl",
        "rb",
    )
)

#  Create the Side bar for the Option menu.
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinson Disease Prediction",
        ],
        default_index=0,
        icons=["activity", "heart", "person"],
    )


if selected == "Diabetes Prediction":
    #  page title of the model.
    st.title("Diabetes Prediction Using SML")

    #  add the input Fields for the Model.
    Pregnancies = st.number_input("Number of Pregnancies")
    Glucose = st.number_input("Glucose Level")
    BloodPressure = st.number_input("BloodPressure Value")
    SkinThickness = st.number_input("SkinThickness Value")
    Insulin = st.number_input("Insulin Level")
    BMI = st.number_input("BMI Value")
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction Value")
    Age = st.number_input("Person Age")

    #  The Code for the Prediction.
    diabetes_predict = -1

    #  Creation a button for Prediction.
    if st.button("Diabetes Test"):
        diabetes_predict = diabetes_model.predict(
            [
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
            ]
        )
        # st.write(diabetes_predict)
        if diabetes_predict == 0:
            st.success("The Person is not Diabetic")
        else:
            st.error("The Person is Diabetic")


if selected == "Heart Disease Prediction":
    #  page title of the model.
    st.title("Heart Disease Prediction Using SML")

    #  add the input Fields for the Model.
    age = st.number_input("Age")
    sex = st.number_input("Sex")
    cp = st.number_input("Chest_Pain")
    trestbps = st.number_input("Blood_Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.number_input("Fasting_Sugar")
    restecg = st.number_input("ECG_Result")
    thalach = st.number_input("Heart_Rate")
    exang = st.number_input("Exercise_Angina")
    oldpeak = st.number_input("ST_Depression")
    slope = st.number_input("ST_Slope")
    ca = st.number_input("Vessels_Count")
    thal = st.number_input("Thalassemia")

    #  The Code for the Prediction.
    heart_predict = -1

    #  Creation a button for Prediction.
    # st.write("Working Fine")
    if st.button("Heart Disease Test"):
        heart_predict = heart_disease.predict(
            [
                [
                    age,
                    sex,
                    cp,
                    trestbps,
                    chol,
                    fbs,
                    restecg,
                    thalach,
                    exang,
                    oldpeak,
                    slope,
                    ca,
                    thal,
                ]
            ]
        )
        # st.write(heart_predict)

        # st.write("Working Fine")
        if heart_predict == 0:
            st.success("The Person dont have the Heart Disease")
        else:
            st.error("The Person have the Heart Disease")

if selected == "Parkinson Disease Prediction":
    #  page title of the model.
    st.title("Parkinson Disease Prediction Using SML")

    #  add the input Fields for the Model.
    MDVP_Fo = st.text_input("Fo")
    MDVP_Fhi = st.text_input("Fhi")
    MDVP_Flo = st.text_input("Flo")
    MDVP_Jitter = st.text_input("Jitter")
    MDVP_Jitter_Abs = st.text_input("Jitter_Abs")
    MDVP_RAP = st.text_input("RAP")
    MDVP_PPQ = st.text_input("PPQ")
    Jitter_DDP = st.text_input("Jitter_DDP")
    MDVP_Shim = st.text_input("Shim")
    MDVP_Shim_dB = st.text_input("Shim_dB")
    Shim_APQ3 = st.text_input("APQ3")
    Shim_APQ5 = st.text_input("APQ5")
    MDVP_APQ = st.text_input("APQ")
    Shim_DDA = st.text_input("DDA")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    Spread1 = st.text_input("Spread1")
    Spread2 = st.text_input("Spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")

    #  The Code for the Prediction.
    parkinson_predict = -1

    #  Creation a button for Prediction.
    if st.button("Parkinson Test"):
        parkinson_predict = parkinson_disease.predict(
            [
                [
                    MDVP_Fo,
                    MDVP_Fhi,
                    MDVP_Flo,
                    MDVP_Jitter,
                    MDVP_Jitter_Abs,
                    MDVP_RAP,
                    MDVP_PPQ,
                    Jitter_DDP,
                    MDVP_Shim,
                    MDVP_Shim_dB,
                    Shim_APQ3,
                    Shim_APQ5,
                    MDVP_APQ,
                    Shim_DDA,
                    NHR,
                    HNR,
                    RPDE,
                    DFA,
                    Spread1,
                    Spread2,
                    D2,
                    PPE,
                ]
            ]
        )
        # st.write(parkinson_predict)
        if parkinson_predict == 0:
            st.success("The person dont have Parkinson Disease")
        else:
            st.error("The person have parkinson Disease")


# Here is the Main Function.
if __name__ == "__main__":
    pass
