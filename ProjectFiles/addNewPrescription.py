import random

from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def addNewPrescription(doctorId, patientId, medication, instructions):
    print("INSIDE NEW PRESCRIPTION")
    doctorID = random.randint(1000, 9999)
    conn = create_connection()
    list = [medication, instructions]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if doctorId != '' and patientId != '' and medication != '' and instructions != '':
            try:
                query = """INSERT INTO PRESCRIPTION(Doctor, Patient, Medication, Instructions) VALUES (?,?,?,?)"""
                values = (doctorId, patientId, medication, instructions)
                print(values)
                result = executeQuery(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to add prescription.'
                else:
                    text = "Added prescription to table: prescription"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to add prescription.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill all boxes.'
        return text
