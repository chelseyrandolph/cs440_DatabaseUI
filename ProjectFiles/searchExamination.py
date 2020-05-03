from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def getExamination(examID, patientID):
    conn = create_connection()
    if examID:
        try:
            query = "SELECT * FROM EXAMINATION WHERE ExamID='" + examID + "';"
            text = executeQuerySelect(conn, query)
            if not text:
                text = 'ERROR: Examination not found.'
        # If the query fails it prints an error
        except:
            text = 'ERROR: Examination not found.'
    elif patientID != '':
        try:
            query = "SELECT * FROM EXAMINATION WHERE Attendee=" + patientID + ";"
            text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Examination not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please fill all boxes.'
    return text
