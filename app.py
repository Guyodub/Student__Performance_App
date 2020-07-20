from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np
app = Flask(__name__)
model = pickle.load(open("student_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():   
    if request.method == "POST":
        age = int(request.form["age"])
        G1 = int(request.form["fp"])
        G2 = int(request.form["sp"])

        #days absent from school
        absences = int(request.form["absence"])
    

        # Mother's level  education
        Medu = request.form["medu"]
        if (Medu =="0"):
            Medu = 0
        elif (Medu =="1"):
            Medu = 1
        elif (Medu=="2"):
            Medu = 2
        elif (Medu =="3"):
            Medu=3
        else: 
            Medu=4
        

        # Father's level  education
        Fedu = request.form['fedu']
        if (Fedu =='0'):
            Fedu = 0
        elif (Fedu =='1'):
            Fedu = 1
        elif (Fedu=='2'):
            Fedu = 2
        elif (Fedu =='3'):
            Fedu = 3
        else:
            Fedu = 4
        

        # Travel time to school
        traveltime = request.form['travel']
        if (traveltime =='0'):
             traveltime  = 0
        elif (traveltime =='1'):
            traveltime = 1
        elif (traveltime=='2'):
            traveltime = 2
        else:
            traveltime = 3

        #Study time: Duration
        studytime = request.form['timestudied']
        if (studytime =='0'):
             studytime  = 0
        elif (studytime =='1'):
             studytime = 1
        elif (studytime=='2'):
            studytime = 2
        else:
             studytime = 3

        
        #past class failures
        failures = request.form['failure']
        if (failures =='0'):
             failures  = 0
        elif (failures =='1'):
             failures = 1
        elif (failures =='2'):
            failures = 2
        else:
             failures = 3

        
        # free time
        freetime = request.form['timefree']
        if (freetime =='0'):
             freetime = 0
        elif (freetime =='1'):
             freetime = 1
        elif (freetime=='2'):
            freetime = 2
        elif (freetime =='3'):
             freetime = 3
        else:
            freetime = 4
        

        # go out with friends
        goout = request.form['goingout']
        if (goout =='0'):
             goout= 0
        elif (goout =='1'):
             goout = 1
        elif (goout=='2'):
            goout = 2
        elif (goout =='3 '):
             goout = 3
        else:
             goout = 4
        
         #  weekend alcohol consumption
        Walc = request.form['alcohol']
        if (Walc =='0'):
             Walc = 0
        elif (Walc =='1'):
             Walc = 1
        elif (Walc=='2'):
            Walc = 2
        elif (Walc =='3'):
             Walc = 3
        else:
             Walc = 4

    prediction=model.predict([[G1, G2, age, Medu, Fedu, traveltime, studytime,failures,freetime, goout,Walc, absences]])

    output=prediction[0]*5
    return render_template('home.html',prediction_text="Your final grade in percentange is: {}".format(output) )



        

if __name__ == "__main__":
    app.run(debug=True)