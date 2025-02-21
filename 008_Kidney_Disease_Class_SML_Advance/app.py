# In this file we will be using the Python Backend Code.

from flask import Flask, render_template, request
import pickle

#  Build the app.
app = Flask(__name__)

#  Load the Model.
best_model = pickle.load(open("bestModel.pkl", "rb"))


#  Define the Endpoints for the webpage.
@app.route("/")
def first():
    return render_template("index.html")


@app.route("/prediction", methods=["post"])
def prediction():
    #  we need the data that will be enter by the user.
    age = int(request.form["age"])
    blood_pressure = int(request.form["blood_pressure"])
    specific_gravity = int(request.form["specific_gravity"])
    albumin = int(request.form["albumin"])
    sugar = int(request.form["sugar"])
    red_blood_cell = int(request.form["red_blood_cell"])
    pus_cell = int(request.form["pus_cell"])
    pus_cell_clumps = int(request.form["pus_cell_clumps"])
    bacteria = int(request.form["bacteria"])
    blood_glucose_random = int(request.form["blood_glucose_random"])
    blood_urea = int(request.form["blood_urea"])
    serum_creatinine = int(request.form["serum_creatinine"])
    sodium = int(request.form["sodium"])
    potassium = int(request.form["potassium"])
    hemoglobin = int(request.form["hemoglobin"])
    packed_cell_volume = int(request.form["packed_cell_volume"])
    white_blood_cell_count = int(request.form["white_blood_cell_count"])
    red_blood_cell_count = int(request.form["red_blood_cell_count"])
    hypertension = int(request.form["hypertension"])
    diabetes_mellitus = int(request.form["diabetes_mellitus"])
    coronary_artery_disease = int(request.form["coronary_artery_disease"])
    appetite = int(request.form["appetite"])
    pedal_edema = int(request.form["pedal_edema"])
    anemia = int(request.form["anemia"])

    #   Make the input list for the prediction.
    new_data_list = [
        age,
        blood_pressure,
        specific_gravity,
        albumin,
        sugar,
        red_blood_cell,
        pus_cell,
        pus_cell_clumps,
        bacteria,
        blood_glucose_random,
        blood_urea,
        serum_creatinine,
        sodium,
        potassium,
        hemoglobin,
        packed_cell_volume,
        white_blood_cell_count,
        red_blood_cell_count,
        hypertension,
        diabetes_mellitus,
        coronary_artery_disease,
        appetite,
        pedal_edema,
        anemia,
    ]

    #  Till here i have the input list now we need to predict.with the model.
    prediction = best_model.predict([new_data_list])

    final_result = ""
    #  Make Prediction.
    if prediction[0] == 0:
        final_result = "The person have the Kidney Disease"
    else:
        final_result = "The person dont have the Kidney Disease"

    return render_template("index.html", final_result=final_result)


@app.route("/templates/about.html")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
