# from fastapi import FastAPI
# from pydantic import BaseModel
# import pickle
# import json
# import requests


# app = FastAPI()


# class model_input(BaseModel):

#     pregnancies: int
#     Glucose: int
#     BloodPressure: int
#     SkinThickness: int
#     Insulin: int
#     BMI: float
#     DiabetesPedigreeFunction: float
#     Age: int


# # loading the saved model
# diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))


# #  Fast API Route Decorator.
# @app.post("/diabetes_prediction")
# def diabetes_predd(input_parameters: model_input):

#     # input_data = input_parameters.json()  # Convert into the Json String
#     # input_dictionary = json.loads(
#     #     input_data
#     # )  # Convert JSON String into the pythin Dictionary.

#     # preg = input_dictionary["pregnancies"]
#     # glu = input_dictionary["Glucose"]
#     # bp = input_dictionary["BloodPressure"]
#     # skin = input_dictionary["SkinThickness"]
#     # insulin = input_dictionary["Insulin"]
#     # bmi = input_dictionary["BMI"]
#     # dpf = input_dictionary["DiabetesPedigreeFunction"]
#     # age = input_dictionary["Age"]

#     # input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

#     #  Directly Access the Variable from the class.
#     input_list = [
#         input_parameters.pregnancies,
#         input_parameters.Glucose,
#         input_parameters.BloodPressure,
#         input_parameters.SkinThickness,
#         input_parameters.Insulin,
#         input_parameters.BMI,
#         input_parameters.DiabetesPedigreeFunction,
#         input_parameters.Age,
#     ]
#     prediction = diabetes_model.predict([input_list])

#     if prediction[0] == 0:
#         return "The person is not diabetic"
#     else:
#         return "The person is diabetic"


from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import warnings

warnings.filterwarnings("ignore")


app = FastAPI()


# The purpose of this code is to allow the FastAPI app to accept requests from any origin,
# supporting all HTTP methods, headers, and credentials for cross-origin requests.

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


#  Loading the model which is saved in the pickle format.
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))


#  Create the Post method for our project.
@app.post("/diabetes_prediction")
def diabetes_predd(input_parameters: model_input):
    #  Directly Access the Variable from the class.
    input_list = [
        input_parameters.pregnancies,
        input_parameters.Glucose,
        input_parameters.BloodPressure,
        input_parameters.SkinThickness,
        input_parameters.Insulin,
        input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction,
        input_parameters.Age,
    ]
    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


# Ngrok for accessible for the Public URL.
ngrok_tunnel = ngrok.connect(8001)
print("Public URL:", ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8001)
