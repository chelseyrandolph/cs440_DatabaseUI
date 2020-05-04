from database import *
from flask import Flask
from search_doctor import *

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def update_doctor_entry(doctor_id, first_name, middle_initial, last_name, phone_number, email, title):
    conn = create_connection()
    list = [first_name, middle_initial, last_name, phone_number, email, title]
    no_update_flag = 0
    for item in list:
        if item == '':
            continue
        else:
            no_update_flag = 1
    if no_update_flag == 0:
        result = 'ERROR: Missing information. Please fill out the field(s) you would like to update.'
        return result
    attributes_to_update = []
    try:
        for item in list:
            if isinstance(int(item), int):
                result = 'ERROR: Invalid input.'
                return result
    except:
        list2 = [doctor_id, first_name, middle_initial, last_name, phone_number, email, title]
        if doctor_id == '':
            result = "ERROR: Doctor ID is required."
            return result
        else:
            row = get_doctor(first_name, middle_initial, last_name, doctor_id)
            if not row:
                result = 'ERROR: Unable to update doctor: ' + doctor_id
                return result
            else:
                doctor = row[0]
            attributes_to_update.append(doctor[0])
            for x in range(1, len(doctor)):
                if doctor[x] != list2[x] and list2[x] != '':
                    try:
                        if isinstance(int(list2[x]), int):
                            attributes_to_update.append(list2[x])
                    except:
                        attributes_to_update.append(str(list2[x]))
                elif doctor[x] != list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(doctor[x]), int):
                            attributes_to_update.append(doctor[x])
                    except:
                        attributes_to_update.append(str(doctor[x]))
            attributes_to_update.append(doctor[0])
            attributes_to_update = tuple(attributes_to_update)
            try:
                query = """UPDATE DOCTOR SET 
                DoctorID = ?,
                FirstName = ?,
                MiddleInitial = ?,
                LastName = ?,
                PhoneNumber = ?,
                Email = ?,
                Title = ?
                WHERE DoctorID = ?"""
                result = execute_query(conn, query, attributes_to_update)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to update doctor: ' + doctor_id
                else:
                    result = "Updated doctor: " + doctor_id
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to update doctor: ' + doctor_id
    return result
