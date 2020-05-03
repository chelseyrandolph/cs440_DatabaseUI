from addNewPatient import *
from addNewDoctor import *
from createNewExamination import *
from deletePatient import *
from deleteDoctor import *
from deleteExamination import *
from updatePatientInformation import *
from updateDoctorInformation import *
from updateExaminationInformation import *
from searchPatient import *
from searchDoctor import *
from searchExamination import *
from filterByTitle import *
from filterByExamination import *
from datetime import datetime
from flask import Flask, render_template, request
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


@app.route("/searchExam", methods=['GET', 'POST'])
def searchExam():
    if request.method == "POST":
        examID = request.form["examID"]
        patientID = request.form["patientID"]
        text = getExamination(examID, patientID)
        if text == '':
            text = 'ERROR: Examination not found.'
            return render_template("searchExam.html", message=text)
        else:
            if 'ERROR' in text:
                text = 'ERROR: Examination not found.'
                return render_template("searchExam.html", message=text)
            else:
                header = ['Exam ID', 'Date', 'Time', 'Allergies', 'Medications', 'Height', 'Weight', 'Doctor', 'Attendee']
                table = printTable(text, header)
                return render_template("searchExam.html", message=table)
    else:
        return render_template("searchExam.html")

@app.route("/createExam", methods=['GET', 'POST'])
def createExam():
    if request.method == "POST":
        doctor = request.form["doctor"]
        attendee = request.form["patient"]
        date = request.form["date"]
        time = request.form["time"]
        height = request.form["height"]
        weight = request.form["weight"]
        allergies = request.form["allergies"]
        medications = request.form["medications"]
        text = createNewExamination(date, time, allergies, medications, height, weight, doctor, attendee)
        if text == '':
            text = 'ERROR:  Unable to create examination.'
            return render_template("createExam.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("createExam.html", message=text)
            else:
                return render_template("createExam.html", message=text)
    else:
        return render_template("createExam.html")

@app.route("/updateExam")
def updateExam():
    return render_template("updateExam.html")


@app.route("/filterExams", methods=['GET', 'POST'])
def filterExam():
    if request.method == "POST":
        list = ['doctor', 'attendee', 'date', 'time']
        filterList = []
        valueList = []
        for item in list:
            r = request.form[item]
            if not r:
                continue
            else:
                filterList.append(item)
                if item == 'date':
                    valueList.append('\'' + datetime.strftime(datetime.strptime(r, '%m-%d-%Y'), '%m-%d-%Y') + '\'')
                elif item == 'time':
                    valueList.append('\'' + datetime.strftime(datetime.strptime(r, '%H:%M'), '%H:%M') + '\'')
                else:
                    valueList.append(r)
        text = filterByExamination(filterList, valueList)
        if text == '':
            text = 'ERROR: Examination not found.'
            return render_template("filterExams.html", message=text)
        else:
            if 'ERROR' in text:
                return render_template("filterExams.html", message=text)
            else:
                header = ['Exam ID', 'Date', 'Time', 'Allergies', 'Medications', 'Height', 'Weight', 'Doctor', 'Attendee']
                table = printTable(text, header)
                return render_template("filterExams.html", message=table)
    else:
        return render_template("filterExams.html")

@app.route("/deleteExam", methods=['GET', 'POST'])
def deleteExam():
    if request.method == "POST":
        examID = request.form["examID"]
        text = deleteExamination(examID)
        if 'ERROR' in text:
            return render_template("deleteExam.html", message=text)
        else:
            text = "Examination " + examID + " has been deleted from table 'EXAMINATION.'"
            return render_template("deleteExam.html", message=text)
    else:
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
