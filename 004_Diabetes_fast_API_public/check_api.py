import json
import requests
import streamlit as st

#  Build the UI for the Streamlit eb App.
st.title("Diabetes Prediction API Tester")

# User Input Fields
pregnancies = int(
    st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
)
glucose = int(st.number_input("Glucose Level", min_value=0, max_value=300, value=100))
blood_pressure = int(
    st.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
)
skin_thickness = int(
    st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
)
insulin = int(st.number_input("Insulin Level", min_value=0, max_value=900, value=80))
bmi = int(st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0, step=0.1))
diabetes_pedigree = int(
    st.number_input(
        "Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01
    )
)
age = int(st.number_input("Age", min_value=0, max_value=120, value=25))


#  Button Handling.
if st.button("Predict"):
    # API URL (Change it if hosted online)
    url = "https://b051-2402-8100-2050-55be-4d04-9cdb-6a99-7e72.ngrok-free.app/diabetes_prediction"

    #     # Prepare input data
    input_data = {
        "pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age,
    }

    #     # Call the FastAPI endpoint
    input_json = json.dumps(input_data)
    response = requests.post(url, data=input_json)
    # st.write(response)

    # Handle response
    if response.status_code == 200:
        st.success(response.text)
    else:
        st.error("Error in API request. Check FastAPI server.")
