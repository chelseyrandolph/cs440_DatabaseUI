from addNewDoctor import *
from addNewPatient import *
from deletePatient import *
from searchDoctor import *
from flask import Flask, render_template, request
from updatePatientInformation import *
from updateDoctorInformation import *
from filterByTitle import *
from deleteDoctor import *
from addNewPrescription import *
from searchPrescription import *
from updatePrescriptionInformation import *
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
            text = "Patient " + patientID + " has been deleted from table 'PATIENT.'"
            return render_template("deletePatient.html", message=text)
    else:
        return render_template("deletePatient.html")


@app.route("/doctor")
def doctor():
    return render_template("doctor.html")


@app.route("/searchDoctor", methods=['GET', 'POST'])
def searchDoctor():
    if request.method == "POST":
        firstName = request.form["first"]
        middleInitial = request.form["middle"]
        lastName = request.form["last"]
        doctorID = request.form["doctorID"]
        text = getDoctor(firstName, middleInitial, lastName, doctorID)
        if text == '':
            text = 'ERROR: Doctor not found.'
            return render_template("searchDoctor.html", message=text)
        else:
            if 'ERROR' in text:
                text = 'ERROR: Doctor not found.'
                return render_template("searchDoctor.html", message=text)
            else:
                header = ['Doctor ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Email', 'Title']
                table = printTable(text, header)
                return render_template("searchDoctor.html", message=table)
    else:
        return render_template("searchDoctor.html")


@app.route("/addDoctor", methods=['GET', 'POST'])
def addDoctor():
    if request.method == "POST":
        firstName = request.form["first"]
        middleInitial = request.form["middle"]
        lastName = request.form["last"]
        phoneNumber = request.form["phone"]
        email = request.form["email"]
        title = request.form["title"]
        text = addNewDoctor(firstName, middleInitial, lastName, phoneNumber, email, title)
        if text == '':
            text = 'ERROR:  Unable to add doctor.'
            return render_template("addDoctor.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("addDoctor.html", message=text)
            else:
                return render_template("addDoctor.html", message=text)
    else:
        return render_template("addDoctor.html")


@app.route("/updateDoctor", methods=['GET', 'POST'])
def updateDoctor():
    if request.method == "POST":
        doctorID = request.form["dID"]
        firstName = request.form["fname"]
        middleInitial = request.form["minit"]
        lastName = request.form["lname"]
        phoneNumber = request.form["pnum"]
        email = request.form["email"]
        title = request.form["title"]
        text = updateDoctorInformation(doctorID, firstName, middleInitial, lastName, phoneNumber, email, title)
        if text == '':
            text = 'ERROR:  Unable to update doctor.'
            return render_template("updateDoctor.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("updateDoctor.html", message=text)
            else:
                text = "Updated patient information for doctor: " + doctorID
                return render_template("updateDoctor.html", message=text)
    else:
        return render_template("updateDoctor.html")


@app.route("/deleteDoctor", methods=['GET', 'POST'])
def deleteDoctor():
    if request.method == "POST":
        doctorID = request.form["dID"]
        text = deleteADoctor(doctorID)
        if 'ERROR' in text:
            return render_template("deleteDoctor.html", message=text)
        else:
            text = "Doctor " + doctorID + " has been deleted from table 'DOCTOR.'"
            return render_template("deleteDoctor.html", message=text)
    else:
        return render_template("deleteDoctor.html")


@app.route("/filterDoctor", methods=['GET', 'POST'])
def filterDoctor():
    if request.method == "POST":
        list = ['gp', 'ped', 'gyn', 'fp', 'psych']
        filterList = []
        for item in list:
            r = request.form.get(item)
            if not r:
                continue
            else:
                filterList.append(item)
        text = filterByTitle(filterList)
        if text == '':
            text = 'ERROR: Title not found.'
            return render_template("filterDoctor.html", message=text)
        else:
            if 'ERROR' in text:
                text = 'ERROR: Title not found.'
                return render_template("filterDoctor.html", message=text)
            else:
                header = ['Doctor ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Email', 'Title']
                table = printTable(text, header)
                return render_template("filterDoctor.html", message=table)
    else:
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


@app.route("/searchPrescription", methods=['GET', 'POST'])
def searchPrescription():
    if request.method == "POST":
        doctorID = request.form["doctorID"]
        patientID = request.form["patientID"]
        medication = request.form["medication"]
        text = getPrescription(doctorID, patientID, medication)
        if text == '':
            text = 'ERROR: Prescription not found.'
            return render_template("searchPrescription.html", message=text)
        else:
            if 'ERROR' in text:
                text = 'ERROR: Prescription not found.'
                return render_template("searchPrescription.html", message=text)
            else:
                header = ['Doctor ID', 'Patient ID', 'Medication', 'Instructions']
                table = printTable(text, header)
                return render_template("searchPrescription.html", message=table)
    else:
        return render_template("searchPrescription.html")


@app.route("/addPrescription", methods=['GET', 'POST'])
def addPrescription():
    if request.method == "POST":
        doctorId = request.form["doctorID"]
        patientId = request.form["patientID"]
        medication = request.form["medication"]
        instructions = request.form["instructions"]
        text = addNewPrescription(doctorId, patientId, medication, instructions)
        if text == '':
            text = 'ERROR:  Unable to add prescription.'
            return render_template("addPrescription.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("addPrescription.html", message=text)
            else:
                return render_template("addPrescription.html", message=text)
    else:
        return render_template("addPrescription.html")


@app.route("/updatePrescription", methods=['GET', 'POST'])
def updatePrescription():
    if request.method == "POST":
        doctorID = request.form["doctorID"]
        patientID = request.form["patientID"]
        medication = request.form["medication"]
        instructions = request.form["instructions"]
        text = updatePrescriptionInformation(doctorID, patientID, medication, instructions)
        if text == '':
            text = 'ERROR:  Unable to update prescription.'
            return render_template("updatePrescription.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("updatePrescription.html", message=text)
            else:
                text = "Updated prescription information"
                return render_template("updatePrescription.html", message=text)
    else:
        return render_template("updatePrescription.html")

if __name__ == "__main__":
    app.run(debug=True)
