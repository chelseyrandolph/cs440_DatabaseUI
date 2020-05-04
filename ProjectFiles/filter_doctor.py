from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def filter_by_doctor(title):
    conn = create_connection()
    if title != '':
        for x in range(0, len(title)):
            if title[x] == 'gp':
                title[x] = 'General Practitioner'
            elif title[x] == 'ped':
                title[x] = 'Pediatrician'
            elif title[x] == 'gyn':
                title[x] = 'Gynecologist'
            elif title[x] == 'fp':
                title[x] = 'Family Physician'
            elif title[x] == 'psych':
                title[x] = 'Psychiatrist'
        try:
            if len(title) > 1:
                t = tuple(title)
                query = "SELECT * FROM DOCTOR WHERE Title IN " + str(t) + ";"
                result = execute_query_select(conn, query)
            else:
                query = "SELECT * FROM DOCTOR WHERE Title = '" + title[0] + "';"
                result = execute_query_select(conn, query)
        # If the query fails it prints an error
        except:
            result = 'ERROR: Title not found.'
    # If the fields aren't filled
    else:
        result = 'ERROR: Missing Information. Please select a title to filter by.'
    return result
