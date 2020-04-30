from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def deleteADoctor(doctorID):
    conn = create_connection()
    if doctorID != '':
        try:
            doctor = []
            doctor.append(doctorID)
            values = tuple(doctor)
            query = "DELETE FROM DOCTOR WHERE DoctorID=?"
            result = executeQuery(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find doctor: ' + doctorID
            else:
                text = "Deleted doctor: " + doctorID
                # TODO: DELETE PRESCRIPTION & EXAM WHERE ID WAS USED
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find doctor: ' + doctorID
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Doctor ID.'
    return text
