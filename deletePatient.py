from flask import Flask, request, render_template, redirect, url_for
from database import *
from searchPatient import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def deleteAPatient(patientID):
    # connecting to database, REPLACE WITH YOUR PATH
    conn = create_connection("C:/sqlite/440.db")
    if patientID != '':
        try:

            patient = []
            patient.append(patientID)
            values = tuple(patient)
            query = "DELETE FROM patient WHERE PatientID=?"
            result = executeQuery(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find patient: ' + patientID
            else:
                text = "Deleted patient: " + patientID
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find patient: ' + patientID
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Patient ID.'
    return text
