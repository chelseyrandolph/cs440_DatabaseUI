from database import *
from flask import Flask
from searchPrescription import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def updatePrescriptionInformation(doctorID, patientID, medication, instructions):
    conn = create_connection()
    list = [instructions]
    noUpdateFlag = 0
    for item in list:
        if item == '':
            continue
        else:
            noUpdateFlag = 1
    if noUpdateFlag == 0:
        text = 'ERROR: Missing information. Please fill out the field you want to update.'
        return text
    attributesToUpdate = []
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        list2 = [doctorID, patientID, medication, instructions]
        if doctorID == '':
            text = "ERROR: DoctorID is required."
            return text
        elif patientID == '':
            text = "ERROR: PatientID is required."
            return text
        elif medication == '':
            text = "ERROR: Medication is required."
            return text
        else:
            row = getPrescription(doctorID, patientID, medication)
            if not row:
                text = 'ERROR: Unable to update prescription'
                return text
            else:
                prescription = row[0]
            try:
                query = """UPDATE PRESCRIPTION SET 
                Instructions = ?
                WHERE Doctor = ? AND Patient = ? AND Medication = ?"""
                print([instructions, doctorID, patientID, medication])
                result = executeQuery(conn, query, [instructions, doctorID, patientID, medication])
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to update prescription'
                else:
                    text = "Updated prescription"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to update prescription'
    return text
