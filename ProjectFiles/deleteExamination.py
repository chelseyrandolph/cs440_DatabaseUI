from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def deleteExamination(examID):
    conn = create_connection()
    if examID != '':
        try:
            exam = []
            exam.append(examID)
            values = tuple(exam)
            query = "DELETE FROM EXAMINATION WHERE ExamID=?"
            result = executeQuery(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find Examination: ' + examID
            else:
                text = "Deleted Examination: " + examID
                # TODO: DELETE PRESCRIPTION & EXAM WHERE ID WAS USED
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find exam: ' + examID
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Examination ID.'
    return text
