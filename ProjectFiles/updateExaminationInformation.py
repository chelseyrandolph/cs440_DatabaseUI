from database import *
from flask import Flask
from searchExamination import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def updateExaminationInformation(examID, date, time, allergies, medications, height, weight, doctor, patient):
    conn = create_connection()
    list = [firstName, middleName, lastName, phoneNumber, email, title]
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
        list2 = [doctorID, firstName, middleName, lastName, phoneNumber, email, title]
        if doctorID == '':
            text = "ERROR: DoctorID is required."
            return text
        else:
            row = getDoctor(firstName, middleName, lastName, doctorID)
            if not row:
                text = 'ERROR: Unable to update doctor: ' + doctorID
                return text
            else:
                doctor = row[0]
            attributesToUpdate.append(doctor[0])
            for x in range(1, len(doctor)):
                if doctor[x] != list2[x] and list2[x] != '':
                    try:
                        if isinstance(int(list2[x]), int):
                            attributesToUpdate.append(list2[x])
                    except:
                        attributesToUpdate.append(str(list2[x]))
                elif doctor[x] != list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(doctor[x]), int):
                            attributesToUpdate.append(doctor[x])
                    except:
                        attributesToUpdate.append(str(doctor[x]))
            attributesToUpdate.append(doctor[0])
            attributesToUpdate = tuple(attributesToUpdate)
            try:
                query = """UPDATE DOCTOR SET 
                DoctorID = ?,
                FirstName = ?,
                MiddleInitial = ?,
                LastName = ?,
                PhoneNumber = ?,
                Email = ?,
                Title = ?
                WHERE DoctorID = ?"""
                result = executeQuery(conn, query, attributesToUpdate)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to update doctor: ' + doctorID
                else:
                    text = "Updated doctor: " + doctorID
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to update doctor: ' + doctorID
    return text
