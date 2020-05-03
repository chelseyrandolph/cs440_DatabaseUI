from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def filterPrescription(doctorID, patientID, medication):
    conn = create_connection()
    if medication != '' or doctorID != '' or patientID != '':
        whereclauses = []
        if medication != '':
            whereclauses.append("medication='" + medication + "'")
        if doctorID != '':
            whereclauses.append("Doctor=" + doctorID)
        if patientID != '':
            whereclauses.append("Patient=" + patientID)

        endofquery = " AND ".join(whereclauses)

        try:
            query = "SELECT * FROM PRESCRIPTION WHERE " + endofquery + ";"
            text = executeQuerySelect(conn, query)
            if not text:
                text = 'ERROR: Prescription not found.'
        # If the query fails it prints an error
        except:
            text = 'ERROR: Prescription not found.'

    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please fill at least one box.'
    return text
