from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def get_patient(first_name, middle_initial, last_name, patient_id):
    conn = create_connection()
    if first_name != '' and middle_initial != '' and last_name != '':
        try:
            query = "SELECT * FROM PATIENT WHERE FirstName = '" + first_name + \
                    "' and MiddleInitial = '" + middle_initial + "' and LastName = '" + last_name + "';"
            result = execute_query_select(conn, query)
            if not result:
                result = 'ERROR: Patient not found.'
        # If the query fails it prints an error
        except:
            result = 'ERROR: Patient not found.'
    elif patient_id != '':
        try:
            query = "SELECT * FROM PATIENT WHERE PatientID = " + patient_id + ";"
            result = execute_query_select(conn, query)
        # If the query fails it prints an error
        except:
            result = 'ERROR: Patient not found.'
    # If the fields aren't filled
    else:
        result = 'ERROR: Missing Information. Please fill out all boxes.'
    return result
