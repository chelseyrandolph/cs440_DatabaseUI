from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def get_doctor(first_name, middle_name, last_name, doctor_id):
    conn = create_connection()
    if first_name != '' and middle_name != '' and last_name != '':
        try:
            query = "SELECT * FROM DOCTOR WHERE FirstName = '" + first_name + \
                    "' and MiddleInitial = '" + middle_name + "' and LastName = '" + last_name + "';"
            result = execute_query_select(conn, query)
            if not result:
                result = 'ERROR: Doctor not found.'
        # If the query fails it prints an error
        except:
            result = 'ERROR: Doctor not found.'
    elif doctor_id != '':
        try:
            query = "SELECT * FROM DOCTOR WHERE DoctorID = " + doctor_id + ";"
            result = execute_query_select(conn, query)
        # If the query fails it prints an error
        except:
            result = 'ERROR: Doctor not found.'
    # If the fields aren't filled
    else:
        result = 'ERROR: Missing Information. Please fill out all boxes.'
    return result
