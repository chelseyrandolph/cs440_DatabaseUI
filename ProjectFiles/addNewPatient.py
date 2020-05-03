import random

from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def addNewPatient(firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID):
    patientID = random.randint(1000, 9999)
    conn = create_connection()
    list = [firstName, middleName, lastName, phoneNumber, address, email, insurN]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if firstName != '' and middleName != '' and lastName != '' and phoneNumber != '' and address != '' and email != '' and insurN != '' and insurID != '':
            try:
                query = """INSERT INTO PATIENT(PatientID, FirstName, MiddleInitial, LastName, PhoneNumber, Address, Email, InsuranceName, InsuranceID) VALUES (?,?,?,?,?,?,?,?,?)"""
                values = (patientID, firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID)
                result = executeQuery(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to add Patient.'
                else:
                    text = "Added patient to table: Patient"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to add Patient.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill out all boxes.'
        return text
