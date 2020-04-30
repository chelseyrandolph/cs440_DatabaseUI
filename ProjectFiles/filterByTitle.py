from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def filterByTitle(title):
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
                text = executeQuerySelect(conn, query)
            else:
                query = "SELECT * FROM DOCTOR WHERE Title='" + title[0] + "';"
                print(query)
                text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Title not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please select a title to filter by.'
    return text
