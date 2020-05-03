from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def getPrescription(doctorID, patientID, medication):
    conn = create_connection()
    if medication != '' and doctorID != '' and patientID != '':
        try:
            query = "SELECT * FROM PRESCRIPTION WHERE Doctor=" + doctorID + \
                    " and Patient=" + patientID + " and medication='" + medication + "';"
            text = executeQuerySelect(conn, query)
            if not text:
                text = 'ERROR: Prescription not found.'
        # If the query fails it prints an error
        except:
            text = 'ERROR: Prescription not found.'
    elif patientID != '':
        try:
            query = "SELECT * FROM PRESCRIPTION WHERE Patient=" + patientID + ";"
            text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Prescription not found.'
    elif doctorID != '':
        try:
            query = "SELECT * FROM PRESCRIPTION WHERE Doctor=" + doctorID + ";"
            text = executeQuerySelect(conn, query)
            # If the query fails it prints an error
        except:
            text = 'ERROR: Prescription not found.'
    elif medication != '':
        try:
            query = "SELECT * FROM PRESCRIPTION WHERE Medication='" + medication + "';"
            print(query)
            text = executeQuerySelect(conn, query)
            # If the query fails it prints an error
        except:
            text = 'ERROR: Prescription not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please fill at least one box.'
    return text
