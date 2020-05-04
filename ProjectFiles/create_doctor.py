import random

from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def create_new_doctor(first_name, middle_initial, last_name, phone_number, email, title):
    doctor_id = random.randint(1000, 9999)
    conn = create_connection()
    list = [first_name, middle_initial, last_name, phone_number, email, title]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if first_name != '' and middle_initial != '' and last_name != '' and phone_number != '' and email != '' and title != '':
            try:
                query = """INSERT INTO DOCTOR(DoctorID, FirstName, MiddleInitial, LastName, PhoneNumber, Email, Title) 
                VALUES (?,?,?,?,?,?,?)"""
                values = (doctor_id, first_name, middle_initial, last_name, phone_number, email, title)
                result = execute_query(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to create doctor.'
                else:
                    text = "Added doctor to table: DOCTOR"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to create doctor.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill out all boxes.'
        return text
