from flask import Flask, render_template, request
from searchPatient import *
from addNewPatient import *
from updatePatientInformation import *
from database import printTable
from deletePatient import *

# global database = "C:\sqlite\440.db"

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


@app.route("/searchPatient", methods=['GET', 'POST'])
def searchPatient():
    if request.method == "POST":
        firstName = request.form["first"]
        middleInitial = request.form["middle"]
        lastName = request.form["last"]
        patientID = request.form["patientID"]
        text = getPatient(firstName, middleInitial, lastName, patientID)
        if text == '':
            text = 'ERROR: Patient not found.'
            return render_template("searchPatient.html", message=text)
        else:
            if 'ERROR' in text:
                text = 'ERROR: Patient not found.'
                return render_template("searchPatient.html", message=text)
            else:
                header = ['Patient ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Address', 'Email',
                          'Insurance Name', 'Insurance ID']
                table = printTable(text, header)
                return render_template("searchPatient.html", message=table)
    else:
        return render_template("searchPatient.html")


@app.route("/addPatient", methods=['GET', 'POST'])
def addPatient():
    if request.method == "POST":
        firstName = request.form["first"]
        middleInitial = request.form["middle"]
        lastName = request.form["last"]
        phoneNumber = request.form["phone"]
        address = request.form["address"]
        email = request.form["email"]
        insurN = request.form["insurance"]
        insurID = request.form["insuranceID"]
        text = addNewPatient(firstName, middleInitial, lastName, phoneNumber, address, email, insurN, insurID)
        if text == '':
            text = 'ERROR:  Unable to add patient.'
            return render_template("addPatient.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("addPatient.html", message=text)
            else:
                text = "Added patient to table: patient"
                return render_template("addPatient.html", message=text)
    else:
        return render_template("addPatient.html")


@app.route("/updatePatient", methods=['GET', 'POST'])
def updatePatient():
    if request.method == "POST":
        patientID = request.form["pID"]
        firstName = request.form["fname"]
        middleInitial = request.form["minit"]
        lastName = request.form["lname"]
        phoneNumber = request.form["pnum"]
        address = request.form["addr"]
        email = request.form["email"]
        insurN = request.form["insurN"]
        insurID = request.form["insurID"]
        text = updatePatientInformation(patientID, firstName, middleInitial, lastName, phoneNumber, address, email,
                                        insurN, insurID)
        if text == '':
            text = 'ERROR:  Unable to update patient.'
            return render_template("updatePatient.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("updatePatient.html", message=text)
            else:
                text = "Updated patient information for patient: " + patientID
                return render_template("updatePatient.html", message=text)
    else:
        return render_template("updatePatient.html")


@app.route("/deletePatient", methods=['GET', 'POST'])
def deletePatient():
    if request.method == "POST":
        patientID = request.form["paID"]
        text = deleteAPatient(patientID)
        if 'ERROR' in text:
            return render_template("deletePatient.html", message=text)
        else:
            text = "Patient " + patientID + " has been deleted from table 'patient.'"
            return render_template("deletePatient.html", message=text)
    else:
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
