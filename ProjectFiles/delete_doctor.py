from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def delete_doctor_entry(doctor_id):
    conn = create_connection()
    if doctor_id != '':
        try:
            doctor = []
            doctor.append(doctor_id)
            values = tuple(doctor)
            query = "DELETE FROM DOCTOR WHERE DoctorID = ?"
            result = execute_query(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find doctor: ' + doctor_id
            else:
                text = "Deleted doctor: " + doctor_id
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find doctor: ' + doctor_id
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Doctor ID.'
    return text
