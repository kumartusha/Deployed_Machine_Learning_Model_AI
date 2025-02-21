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
