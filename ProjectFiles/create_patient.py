from database import *
import random
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def create_new_patient(first_name, middle_initial, last_name, phone_number, address, email, insurance_name, insurance_id):
    patient_id = random.randint(1000, 9999)
    conn = create_connection()
    list = [first_name, middle_initial, last_name, phone_number, address, email, insurance_name]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return text
    except:
        if first_name != '' and middle_initial != '' and last_name != '' and phone_number != '' and address != '' \
                and email != '' and insurance_name != '' and insurance_id != '':
            try:
                query = """INSERT INTO PATIENT(PatientID, FirstName, MiddleInitial, LastName, PhoneNumber, Address, 
                Email, InsuranceName, InsuranceID) VALUES (?,?,?,?,?,?,?,?,?) """
                values = (patient_id, first_name, middle_initial, last_name, phone_number, address, email,
                          insurance_name, insurance_id)
                result = execute_query(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to create Patient.'
                else:
                    text = "Added patient to table: Patient"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to create Patient.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill out all boxes.'
        return text
