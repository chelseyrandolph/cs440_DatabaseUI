from flask import Flask
from database import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def getPatient(firstName, middleName, lastName, patientID):
    conn = create_connection()
    if firstName != '' and middleName != '' and lastName != '':
        try:
            query = "SELECT * FROM PATIENT WHERE FirstName='" + firstName + \
                    "' and MiddleInitial='" + middleName + "' and LastName='" + lastName + "';"
            text = executeQuerySelect(conn, query)
            if not text:
                text = 'ERROR: Patient not found.'
        # If the query fails it prints an error
        except:
            text = 'ERROR: Patient not found.'
    elif patientID != '':
        try:
            query = "SELECT * FROM PATIENT WHERE PatientID=" + patientID + ";"
            text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Patient not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please fill all boxes.'
    return text
