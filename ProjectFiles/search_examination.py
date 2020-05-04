from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def get_examination(examination_id, patient_id):
    conn = create_connection()
    if examination_id:
        try:
            query = "SELECT * FROM EXAMINATION WHERE ExamID = '" + examination_id + "';"
            result = execute_query_select(conn, query)
            if not result:
                result = 'ERROR: Examination not found.'
        # If the query fails it prints an error
        except:
            result = 'ERROR: Examination not found.'
    elif patient_id != '':
        try:
            query = "SELECT * FROM EXAMINATION WHERE Attendee = " + patient_id + ";"
            result = execute_query_select(conn, query)
        # If the query fails it prints an error
        except:
            result = 'ERROR: Examination not found.'
    # If the fields aren't filled
    else:
        result = 'ERROR: Missing Information. Please fill out all boxes.'
    return result
