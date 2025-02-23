#  Here we write the code for the Flask Application of our ml model.
from flask import Flask, render_template, request, redirect, jsonify, url_for
import mysql
import pickle
import mysql.connector


# Create the App.
app = Flask(__name__)

# Load the Model.
best_model = pickle.load(open("best_model.pkl", "rb"))

# Code for connect the flask app with the SQL Database.  (1st Step is to connect the Flask app with the MySql Connector)

db = mysql.connector.connect(
    user="root", password="1234!@#$Tushar", host="localhost", database="wscubetech"
)

cursor = db.cursor()


#  Build the Endpoints for Our Application.
@app.route("/")
def default():
    return render_template("index.html")


@app.route("/prediction", methods=["post"])
def prediction():
    # Here we write the code for the Prediction and build the UI for Our ml model.
    Location = int(request.form["Location"])
    Rainfall = int(request.form["Rainfall"])
    Evaporation = int(request.form["Evaporation"])
    Sunshine = int(request.form["Sunshine"])
    WindGustDir = int(request.form["WindGustDir"])
    WindGustSpeed = int(request.form["WindGustSpeed"])
    WindDir9am = int(request.form["WindDir9am"])
    WindDir3pm = int(request.form["WindDir3pm"])
    WindSpeed9am = int(request.form["WindSpeed9am"])
    WindSpeed3pm = int(request.form["WindSpeed3pm"])
    RainToday = int(request.form["RainToday"])
    Year = int(request.form["Year"])
    Month = int(request.form["Month"])
    Day = int(request.form["Day"])
    Temp_diff = int(request.form["Temp_diff"])
    Temp_3pm_9am_diff = int(request.form["Temp_3pm_9am_diff"])
    Cloud_avg = int(request.form["Cloud_avg"])
    Humidity3pm_9am_Diff = int(request.form["Humidity3pm_9am_Diff"])
    Pressure3pm_9am_Diff = int(request.form["Pressure3pm_9am_Diff"])

    new_data = [
        Location,
        Rainfall,
        Evaporation,
        Sunshine,
        WindGustDir,
        WindGustSpeed,
        WindDir9am,
        WindDir3pm,
        WindSpeed9am,
        WindSpeed3pm,
        RainToday,
        Year,
        Month,
        Day,
        Temp_diff,
        Temp_3pm_9am_diff,
        Cloud_avg,
        Humidity3pm_9am_Diff,
        Pressure3pm_9am_Diff,
    ]

    predict = best_model.predict([new_data])

    #  Make Prediction.
    if predict[0] == 0:
        Prediction = "Tomorrow have chance for the Rainfall"
    else:
        Prediction = "Tomorrow don't have the chance for the Rainfall"

    #  Here we write the code for the SQL Database.
    print(new_data)
    print(type(Prediction))
    print(Prediction)

    try:
        cursor.execute(
            """INSERT INTO rainfall_prediction(
        Location,
        Rainfall,
        Evaporation,
        Sunshine,
        WindGustDir,
        WindGustSpeed,
        WindDir9am,
        WindDir3pm,
        WindSpeed9am,
        WindSpeed3pm,
        RainToday,
        Year,
        Month,
        Day,
        Temp_diff,
        Temp_3pm_9am_diff,
        Cloud_avg,
        Humidity3pm_9am_Diff,
        Pressure3pm_9am_Diff,
        Prediction)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)""",
            (
                Location,
                Rainfall,
                Evaporation,
                Sunshine,
                WindGustDir,
                WindGustSpeed,
                WindDir9am,
                WindDir3pm,
                WindSpeed9am,
                WindSpeed3pm,
                RainToday,
                Year,
                Month,
                Day,
                Temp_diff,
                Temp_3pm_9am_diff,
                Cloud_avg,
                Humidity3pm_9am_Diff,
                Pressure3pm_9am_Diff,
                Prediction,
            ),
        )
        #  Commit into the database.
        db.commit()
        print("Data Saved Successfully")

    except Exception as e:
        print(f"The error are:-{e}")
    finally:
        cursor.close()
        db.close()

    # print(finalResult)
    return render_template("index.html", result=Prediction)


# For run the App.
if __name__ == "__main__":
    app.run(debug=True, port=8000)
