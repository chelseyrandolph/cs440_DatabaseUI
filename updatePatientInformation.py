from flask import Flask
from database import *
from searchPatient import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def updatePatientInformation(patientID, firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID):
    # connecting to database, REPLACE WITH YOUR PATH
    conn = create_connection("C:/sqlite/440.db")
    list = [firstName, middleName, lastName, phoneNumber, address, email, insurN]
    attributesToUpdate = []
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        list2 = [patientID, firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID]
        if patientID == '':
            text = "ERROR: PatientID is required."
            return text
        else:
            row = getPatient(firstName, middleName, lastName, patientID)
            if not row:
                text = 'ERROR: Unable to update patient: ' + patientID
                return text
            else:
                patient = row[0]
            attributesToUpdate.append(patient[0])
            for x in range(1, len(patient)):
                if patient[x] != list2[x] and list2[x] != '':
                    try:
                        if isinstance(int(list2[x]), int):
                            attributesToUpdate.append(list2[x])
                    except:
                        attributesToUpdate.append(str(list2[x]))
                elif patient[x] != list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(patient[x]), int):
                            attributesToUpdate.append(patient[x])
                    except:
                        attributesToUpdate.append(str(patient[x]))
            attributesToUpdate.append(patient[0])
            attributesToUpdate = tuple(attributesToUpdate)
            try:
                query = """UPDATE patient SET 
                PatientID = ?,
                FirstName = ?,
                MiddleInitial = ?,
                 LastName = ?,
                 PhoneNumber = ?,
                 Address = ?,
                 Email = ?,
                 InsuranceName = ?,
                 InsuranceID = ?
                 WHERE PatientID = ?"""
                result = executeQuery(conn, query, attributesToUpdate)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to update patient: ' + patientID
                else:
                    text = "Updated patient: " + patientID
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to update patient: ' + patientID
    return text
