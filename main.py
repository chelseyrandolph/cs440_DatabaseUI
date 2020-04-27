from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/patient")
def patient():
    return render_template("patient.html")


@app.route("/searchPatient")
def searchPatient():
    return render_template("searchPatient.html")


@app.route("/addPatient")
def addPatient():
    return render_template("addPatient.html")


@app.route("/updatePatient")
def updatePatient():
    return render_template("updatePatient.html")


@app.route("/deletePatient")
def deletePatient():
    return render_template("deletePatient.html")


@app.route("/doctor")
def doctor():
    return render_template("doctor.html")


@app.route("/searchDoctor")
def searchDoctor():
    return render_template("searchDoctor.html")


@app.route("/addDoctor")
def addDoctor():
    return render_template("addDoctor.html")


@app.route("/updateDoctor")
def updateDoctor():
    return render_template("updateDoctor.html")


@app.route("/deleteDoctor")
def deleteDoctor():
    return render_template("deleteDoctor.html")


@app.route("/filterDoctor")
def filterDoctor():
    return render_template("filterDoctor.html")


@app.route("/examination")
def examination():
    return render_template("examination.html")


@app.route("/searchExam")
def searchExam():
    return render_template("searchExam.html")


@app.route("/createExam")
def createExam():
    return render_template("createExam.html")


@app.route("/updateExam")
def updateExam():
    return render_template("updateExam.html")


@app.route("/filterExams")
def filterExam():
    return render_template("filterExams.html")


@app.route("/deleteExam")
def deleteExam():
    return render_template("deleteExam.html")


@app.route("/prescription")
def prescription():
    return render_template("prescription.html")


@app.route("/searchPrescription")
def searchPrescription():
    return render_template("searchPrescription.html")


@app.route("/addPrescription")
def addPrescription():
    return render_template("addPrescription.html")


@app.route("/updatePrescription")
def updatePrescription():
    return render_template("updatePrescription.html")


@app.route("/filterPrescriptions")
def filterPrescriptions():
    return render_template("filterPrescriptions.html")


if __name__ == "__main__":
    app.run(debug=True)
