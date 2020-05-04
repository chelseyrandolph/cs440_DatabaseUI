from database import *
import random
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def create_new_prescription(doctor_id, patient_id, medication, instructions):
    doctorID = random.randint(1000, 9999)
    conn = create_connection()
    list = [medication, instructions]
    try:
        for item in list:
            if isinstance(int(item), int):
                result = 'ERROR: Invalid input.'
                return result
    except:
        if doctor_id != '' and patient_id != '' and medication != '' and instructions != '':
            try:
                query = """INSERT INTO PRESCRIPTION(Doctor, Patient, Medication, Instructions) VALUES (?,?,?,?)"""
                values = (doctor_id, patient_id, medication, instructions)
                result = execute_query(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to add prescription.'
                else:
                    result = "Added prescription to table: PRESCRIPTION."
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to add prescription.'
        # If the fields aren't filled
        else:
            result = 'ERROR: Missing Information. Please fill out all boxes.'
        return result
