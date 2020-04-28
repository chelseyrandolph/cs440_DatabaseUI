from flask import Flask
from database import *
import random

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def addNewPatient(firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID):
    patientID = random.randint(1000, 9999)
    # connecting to database, REPLACE WITH YOUR PATH
    conn = create_connection("C:/sqlite/440.db")
    list = [firstName, middleName, lastName, phoneNumber, address, email, insurN]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if firstName != '' and middleName != '' and lastName != '' and phoneNumber != '' and address != '' and email != '' and insurN != '' and insurID != '':
            try:
                query = """INSERT INTO patient (PatientID, FirstName, MiddleInitial, LastName, PhoneNumber, Address, Email, InsuranceName, InsuranceID) VALUES (?,?,?,?,?,?,?,?,?)"""
                values = (patientID, firstName, middleName, lastName, phoneNumber, address, email, insurN, insurID)
                result = executeQuery(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to add patient.'
                else:
                    text = "Added patient to table: patient"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to add patient.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill all boxes.'
        return text
