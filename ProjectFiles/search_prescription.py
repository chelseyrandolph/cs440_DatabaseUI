from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def get_prescription(doctor_id, patient_id, medication):
    conn = create_connection()
    if medication != '' or doctor_id != '' or patient_id != '':
        where_clauses = []
        if medication != '':
            where_clauses.append("Medication = '" + medication + "'")
        if doctor_id != '':
            where_clauses.append("Doctor = " + doctor_id)
        if patient_id != '':
            where_clauses.append("Patient = " + patient_id)

        end_of_query = " AND ". join(where_clauses)

        try:
            query = "SELECT * FROM PRESCRIPTION WHERE " + end_of_query + ";"
            result = execute_query_select(conn, query)
            if not result:
                result = 'ERROR: Prescription not found.'
        # If the query fails it prints an error
        except:
            result = 'ERROR: Prescription not found.'
    # If the fields aren't filled
    else:
        result = 'ERROR: Missing Information. Please fill out at least one box.'
    return result
