#  Here is the Python Code for Our Application.


from flask import Flask, request, render_template

import pickle
import joblib

#  Flask App Creation.
app = Flask(__name__)

# Load the model
with open("gradient_boost.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# Create the Different Routes for Our Model.
@app.route("/")
def main():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    #  here we need to take the input of the form data and need ts to perform the Operation.
    gender = int(request.form["gender"])
    SeniorCitizen = int(request.form["SeniorCitizen"])
    Partner = int(request.form["Partner"])
    Dependents = int(request.form["Dependents"])
    tenure = int(request.form["tenure"])
    PhoneService = int(request.form["PhoneService"])
    MultipleLines = int(request.form["MultipleLines"])
    InternetService = int(request.form["InternetService"])
    OnlineSecurity = int(request.form["OnlineSecurity"])
    OnlineBackup = int(request.form["OnlineBackup"])
    DeviceProtection = int(request.form["DeviceProtection"])
    TechSupport = int(request.form["TechSupport"])
    StreamingTV = int(request.form["StreamingTV"])
    StreamingMovies = int(request.form["StreamingMovies"])
    Contract = int(request.form["Contract"])
    PaperlessBilling = int(request.form["PaperlessBilling"])
    PaymentMethod = int(request.form["PaymentMethod"])
    MonthlyCharges = int(request.form["MonthlyCharges"])
    TotalCharges = int(request.form["TotalCharges"])

    #  Till here we have the list of inputs and we ned to save into the list.
    new_data = [
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges,
    ]

    # Perform the Prediction of the Model.
    prediction = model.predict([new_data])

    if prediction[0] == 0:
        final_result = "The customer has churned."
    else:
        final_result = "The customer has not churned."

    return render_template("index.html", final_result=final_result)


@app.route("/templates/about.html")
def about():
    return render_template("about.html")


#  Main Function.
if __name__ == "__main__":
    app.run(debug=True, port=5001)
