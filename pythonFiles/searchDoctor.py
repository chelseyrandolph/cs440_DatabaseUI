from flask import Flask
from database import *

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def getDoctor(firstName, middleName, lastName, doctorID):
    conn = create_connection()
    if firstName != '' and middleName != '' and lastName != '':
        try:
            query = "SELECT * FROM DOCTOR WHERE FirstName='" + firstName + \
                    "' and MiddleInitial='" + middleName + "' and LastName='" + lastName + "';"
            text = executeQuerySelect(conn, query)
            if not text:
                text = 'ERROR: Doctor not found.'
        # If the query fails it prints an error
        except:
            text = 'ERROR: Doctor not found.'
    elif doctorID != '':
        try:
            query = "SELECT * FROM DOCTOR WHERE DoctorID=" + doctorID + ";"
            text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Doctor not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please fill all boxes.'
    return text
