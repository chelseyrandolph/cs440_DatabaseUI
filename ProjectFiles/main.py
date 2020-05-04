# CS 440
# Team Delta
# Chelsey Randolph, Jared Knouse, Caleb Burchett

# Patient
from create_patient import *
from search_patient import *
from update_patient import *
from delete_patient import *

# Doctor
from create_doctor import *
from search_doctor import *
from filter_doctor import *
from update_doctor import *
from delete_doctor import *

# Examination
from create_examination import *
from search_examination import *
from filter_examination import *
from update_examination import *
from delete_examination import *

# Prescription
from create_prescription import *
from search_prescription import *
from update_prescription import *

# General
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def start():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")


####################################
#  Beginning of Patient Functions  #
####################################


@app.route("/patient")
def patient():
    return render_template("patient.html")


@app.route("/create-patient", methods=['GET', 'POST'])
def create_patient():
    if request.method == "POST":
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        phone_number = request.form["phone"]
        address = request.form["address"]
        email = request.form["email"]
        insurance_name = request.form["insurance"]
        insurance_id = request.form["insurance_id"]
        result = create_new_patient(first_name, middle_initial, last_name, phone_number, address, email, insurance_name,
                                    insurance_id)
        if result == '':
            result = 'ERROR: Unable to create patient.'
            return render_template("create-patient.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("create-patient.html", message=result)
            else:
                result = "Added patient to table: PATIENT."
                return render_template("create-patient.html", message=result)
    else:
        return render_template("create-patient.html")


@app.route("/search-patient", methods=['GET', 'POST'])
def search_patient():
    if request.method == "POST":
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        patient_id = request.form["patient_id"]
        result = get_patient(first_name, middle_initial, last_name, patient_id)
        if result == '':
            result = 'ERROR: Patient not found.'
            return render_template("search-patient.html", message=result)
        else:
            if 'ERROR' in result:
                result = 'ERROR: Patient not found.'
                return render_template("search-patient.html", message=result)
            else:
                header = ['Patient ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Address', 'Email',
                          'Insurance Name', 'Insurance ID']
                table = print_table(result, header)
                return render_template("search-patient.html", message=table)
    else:
        return render_template("search-patient.html")


@app.route("/update-patient", methods=['GET', 'POST'])
def update_patient():
    if request.method == "POST":
        patient_id = request.form["patient_id"]
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        phone_number = request.form["phone"]
        address = request.form["address"]
        email = request.form["email"]
        insurance_name = request.form["insurance"]
        insurance_id = request.form["insurance_id"]
        result = update_patient_entry(patient_id, first_name, middle_initial, last_name, phone_number, address, email,
                                      insurance_name, insurance_id)
        if result == '':
            result = 'ERROR: Unable to update patient.'
            return render_template("update-patient.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("update-patient.html", message=result)
            else:
                result = "Updated patient information for: " + patient_id
                return render_template("update-patient.html", message=result)
    else:
        return render_template("update-patient.html")


@app.route("/delete-patient", methods=['GET', 'POST'])
def delete_patient():
    if request.method == "POST":
        patient_id = request.form["patient_id"]
        text = delete_patient_entry(patient_id)
        if 'ERROR' in text:
            return render_template("delete-patient.html", message=text)
        else:
            text = "Patient " + patientID + " has been deleted from table PATIENT."
            return render_template("delete-patient.html", message=text)
    else:
        return render_template("delete-patient.html")


###################################
#  Beginning of Doctor Functions  #
###################################


@app.route("/doctor")
def doctor():
    return render_template("doctor.html")


@app.route("/create-doctor", methods=['GET', 'POST'])
def create_doctor():
    if request.method == "POST":
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        title = request.form["title"]
        result = create_new_doctor(first_name, middle_initial, last_name, phone_number, email, title)
        if result == '':
            result = 'ERROR: Unable to create doctor.'
            return render_template("create-doctor.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("create-doctor.html", message=result)
            else:
                return render_template("create-doctor.html", message=result)
    else:
        return render_template("create-doctor.html")


@app.route("/search-doctor", methods=['GET', 'POST'])
def search_doctor():
    if request.method == "POST":
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        doctor_id = request.form["doctor_id"]
        result = get_doctor(first_name, middle_initial, last_name, doctor_id)
        if result == '':
            result = 'ERROR: Doctor not found.'
            return render_template("search-doctor.html", message=result)
        else:
            if 'ERROR' in result:
                result = 'ERROR: Doctor not found.'
                return render_template("search-doctor.html", message=result)
            else:
                header = ['Doctor ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Email', 'Title']
                table = print_table(result, header)
                return render_template("search-doctor.html", message=table)
    else:
        return render_template("search-doctor.html")


@app.route("/filter-doctor", methods=['GET', 'POST'])
def filter_doctor():
    if request.method == "POST":
        list = ['gp', 'ped', 'gyn', 'fp', 'psych']
        filter_list = []
        for item in list:
            r = request.form.get(item)
            if not r:
                continue
            else:
                filter_list.append(item)
        result = filter_by_doctor(filter_list)
        if result == '':
            result = 'ERROR: Title not found.'
            return render_template("filter-doctor.html", message=result)
        else:
            if 'ERROR' in result:
                result = 'ERROR: Title not found.'
                return render_template("filter-doctor.html", message=result)
            else:
                header = ['Doctor ID', 'First Name', 'Middle Initial', 'Last Name', 'Phone Number', 'Email', 'Title']
                table = print_table(result, header)
                return render_template("filter-doctor.html", message=table)
    else:
        return render_template("filter-doctor.html")


@app.route("/update-doctor", methods=['GET', 'POST'])
def update_doctor():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        first_name = request.form["first"]
        middle_initial = request.form["middle"]
        last_name = request.form["last"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        title = request.form["title"]
        result = update_doctor_entry(doctor_id, first_name, middle_initial, last_name, phone_number, email, title)
        if result == '':
            result = 'ERROR: Unable to update doctor.'
            return render_template("update-doctor.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("update-doctor.html", message=result)
            else:
                result = "Updated information for doctor: " + doctor_id
                return render_template("update-doctor.html", message=result)
    else:
        return render_template("update-doctor.html")


@app.route("/delete-doctor", methods=['GET', 'POST'])
def delete_doctor():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        text = delete_doctor_entry(doctor_id)
        if 'ERROR' in text:
            return render_template("delete-doctor.html", message=text)
        else:
            text = "Doctor " + doctor_id + " has been deleted from table DOCTOR."
            return render_template("delete-doctor.html", message=text)
    else:
        return render_template("delete-doctor.html")


########################################
#  Beginning of Examination Functions  #
########################################


@app.route("/examination")
def examination():
    return render_template("examination.html")


@app.route("/create-examination", methods=['GET', 'POST'])
def create_examination():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        patient_id = request.form["patient_id"]
        date = request.form["date"]
        time = request.form["time"]
        height = request.form["height"]
        weight = request.form["weight"]
        allergies = request.form["allergies"]
        medications = request.form["medications"]
        result = create_new_examination(date, time, allergies, medications, height, weight, doctor_id, patient_id)
        if result == '':
            result = 'ERROR: Unable to create examination.'
            return render_template("create-examination.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("create-examination.html", message=result)
            else:
                return render_template("create-examination.html", message=result)
    else:
        return render_template("create-examination.html")


@app.route("/search-examination", methods=['GET', 'POST'])
def search_examination():
    if request.method == "POST":
        examination_id = request.form["examination_id"]
        patient_id = request.form["patient_id"]
        result = get_examination(examination_id, patient_id)
        if result == '':
            result = 'ERROR: Examination not found.'
            return render_template("search-examination.html", message=result)
        else:
            if 'ERROR' in result:
                result = 'ERROR: Examination not found.'
                return render_template("search-examination.html", message=result)
            else:
                header = ['Exam ID', 'Date', 'Time', 'Allergies', 'Medications', 'Height', 'Weight', 'Doctor', 'Attendee']
                table = print_table(result, header)
                return render_template("search-examination.html", message=table)
    else:
        return render_template("search-examination.html")


@app.route("/filter-examination", methods=['GET', 'POST'])
def filter_exam():
    if request.method == "POST":
        list = ['doctor', 'attendee', 'date', 'time']
        filter_list = []
        value_list = []
        for item in list:
            r = request.form[item]
            if not r:
                continue
            else:
                filter_list.append(item)
                if item == 'date':
                    value_list.append('\'' + datetime.strftime(datetime.strptime(r, '%m-%d-%Y'), '%m-%d-%Y') + '\'')
                elif item == 'time':
                    value_list.append('\'' + datetime.strftime(datetime.strptime(r, '%H:%M'), '%H:%M') + '\'')
                else:
                    value_list.append(r)
        result = filter_by_examination(filter_list, value_list)
        if result == '':
            result = 'ERROR: Examination not found.'
            return render_template("filter-examination.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("filter-examination.html", message=result)
            else:
                header = ['Exam ID', 'Date', 'Time', 'Allergies', 'Medications', 'Height', 'Weight', 'Doctor', 'Attendee']
                table = print_table(result, header)
                return render_template("filter-examination.html", message=table)
    else:
        return render_template("filter-examination.html")


@app.route("/update-examination", methods=['GET', 'POST'])
def update_examination():
    if request.method == "POST":
        examination_id = request.form["examination_id"]
        date = request.form["date"]
        time = request.form["time"]
        allergies = request.form["allergies"]
        medications = request.form["medications"]
        height = request.form["height"]
        weight = request.form["weight"]
        doctor_id = request.form["doctor_id"]
        patient_id = request.form["patient_id"]
        result = update_examination_entry(examination_id, date, time, allergies, medications, height, weight, doctor_id, patient_id)
        if result == '':
            result = 'ERROR: Unable to update examination.'
            return render_template("update-examination.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("update-examination.html", message=result)
            else:
                result = "Updated information for examination: " + examination_id
                return render_template("update-examination.html", message=result)
    else:
        return render_template("update-examination.html")


@app.route("/delete-examination", methods=['GET', 'POST'])
def delete_exam():
    if request.method == "POST":
        examination_id = request.form["examination_id"]
        result = delete_examination_entry(examination_id)
        if 'ERROR' in result:
            return render_template("delete-examination.html", message=result)
        else:
            result = "Examination " + examination_id + " has been deleted from table EXAMINATION."
            return render_template("delete-examination.html", message=result)
    else:
        return render_template("delete-examination.html")


#########################################
#  Beginning of Prescription Functions  #
#########################################


@app.route("/prescription")
def prescription():
    return render_template("prescription.html")


@app.route("/create-prescription", methods=['GET', 'POST'])
def create_prescription():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        patient_id = request.form["patient_id"]
        medication = request.form["medication"]
        instructions = request.form["instructions"]
        result = create_new_prescription(doctor_id, patient_id, medication, instructions)
        if result == '':
            result = 'ERROR:  Unable to add prescription.'
            return render_template("create-prescription.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("create-prescription.html", message=result)
            else:
                return render_template("create-prescription.html", message=result)
    else:
        return render_template("create-prescription.html")


@app.route("/search-prescription", methods=['GET', 'POST'])
def search_prescription():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        patient_id = request.form["patient_id"]
        medication = request.form["medication"]
        result = get_prescription(doctor_id, patient_id, medication)
        if result == '':
            result = 'ERROR: Prescription not found.'
            return render_template("search-prescription.html", message=result)
        else:
            if 'ERROR' in result:
                result = 'ERROR: Prescription not found.'
                return render_template("search-prescription.html", message=result)
            else:
                header = ['Doctor ID', 'Patient ID', 'Medication', 'Instructions']
                table = print_table(result, header)
                return render_template("search-prescription.html", message=table)
    else:
        return render_template("search-prescription.html")


@app.route("/update-prescription", methods=['GET', 'POST'])
def update_prescription():
    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        patient_id = request.form["patient_id"]
        medication = request.form["medication"]
        instructions = request.form["instructions"]
        result = update_prescription_entry(doctor_id, patient_id, medication, instructions)
        if result == '':
            result = 'ERROR:  Unable to update prescription.'
            return render_template("update-prescription.html", message=result)
        else:
            if 'ERROR' in result:
                return render_template("update-prescription.html", message=result)
            else:
                result = "Updated prescription information"
                return render_template("update-prescription.html", message=result)
    else:
        return render_template("update-prescription.html")


if __name__ == "__main__":
    app.run(debug=True)