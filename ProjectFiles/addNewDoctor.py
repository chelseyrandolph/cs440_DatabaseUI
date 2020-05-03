import random

from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def addNewDoctor(firstName, middleName, lastName, phoneNumber, email, title):
    print("INSIDE NEW DOC")
    doctorID = random.randint(1000, 9999)
    conn = create_connection()
    list = [firstName, middleName, lastName, phoneNumber, email, title]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if firstName != '' and middleName != '' and lastName != '' and phoneNumber != '' and email != '' and title != '':
            try:
                query = """INSERT INTO DOCTOR(DoctorID, FirstName, MiddleInitial, LastName, PhoneNumber, Email, Title) VALUES (?,?,?,?,?,?,?)"""
                values = (doctorID, firstName, middleName, lastName, phoneNumber, email, title)
                print(values)
                result = executeQuery(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to add Doctor.'
                else:
                    text = "Added doctor to table: Doctor"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to add Doctor.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill out all boxes.'
        return text
