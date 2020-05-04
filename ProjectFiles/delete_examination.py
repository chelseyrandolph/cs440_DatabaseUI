from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def delete_examination_entry(examination_id):
    conn = create_connection()
    if examination_id != '':
        try:
            exam = []
            exam.append(examination_id)
            values = tuple(exam)
            query = "DELETE FROM EXAMINATION WHERE ExamID = ?"
            result = execute_query(conn, query, values)
            if result == "Query Failed.":
                text = 'ERROR: Unable to find Examination: ' + examination_id
            else:
                text = "Deleted Examination: " + examination_id
        # If the query fails it prints an error
        except:
            text = 'ERROR: Unable to find exam: ' + examination_id
    # If the fields aren't filled
    else:
        text = 'ERROR: Please input Examination ID.'
    return text
