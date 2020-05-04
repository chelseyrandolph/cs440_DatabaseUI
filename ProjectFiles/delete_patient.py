from database import *
from flask import Flask
app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def delete_patient_entry(patient_id):
    conn = create_connection()
    if patient_id != '':
        try:
            patient = []
            patient.append(patient_id)
            values = tuple(patient)
            query = "DELETE FROM PATIENT WHERE PatientID = ?"
            result = execute_query(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find patient: ' + patient_id
            else:
                # TODO: DELETE PRESCRIPTION & EXAM WHERE ID WAS USED
                text = "Deleted patient: " + patient_id
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find patient: ' + patient_id
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Patient ID.'
    return text
