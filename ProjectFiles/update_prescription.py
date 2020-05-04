from database import *
from flask import Flask
from search_prescription import *

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def update_prescription_entry(doctor_id, patient_id, medication, instructions):
    conn = create_connection()
    list = [instructions]
    no_update_flag = 0
    for item in list:
        if item == '':
            continue
        else:
            no_update_flag = 1
    if no_update_flag == 0:
        result = 'ERROR: Missing information. Please fill out the field(s) you would like to update.'
        return result
    attributes_to_update = []
    try:
        for item in list:
            if isinstance(int(item), int):
                result = 'ERROR: Invalid input.'
                return result
    except:
        list2 = [doctor_id, patient_id, medication, instructions]
        if doctor_id == '':
            result = "ERROR: Doctor ID is required."
            return result
        elif patient_id == '':
            result = "ERROR: Patient ID is required."
            return result
        elif medication == '':
            result = "ERROR: Medication is required."
            return result
        else:
            row = get_prescription(doctor_id, patient_id, medication)
            if not row:
                result = 'ERROR: Unable to update prescription.'
                return result
            else:
                prescription = row[0]
            try:
                query = """UPDATE PRESCRIPTION SET 
                Instructions = ?
                WHERE Doctor = ? AND Patient = ? AND Medication = ?"""
                result = execute_query(conn, query, [instructions, doctor_id, patient_id, medication])
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to update prescription'
                else:
                    result = "Updated prescription."
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to update prescription.'
    return result
