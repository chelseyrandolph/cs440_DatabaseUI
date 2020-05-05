from database import *
from datetime import datetime
from flask import Flask
from search_examination import *

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def update_examination_entry(examination_id, date, time, allergies, medications, height, weight, doctor_id, patient_id):
    conn = create_connection()
    # Sanitized date/time input
    if date:
        date = datetime.strftime(datetime.strptime(date, '%m-%d-%Y'), '%m-%d-%Y')
    if time:
        time = datetime.strftime(datetime.strptime(time, '%H:%M'), '%H:%M')
    list = [date, time, allergies, medications, height, weight, doctor_id]
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
        for x in range(0, len(list)):
            if x < 4 and isinstance(int(list[x]), int):
                result = 'ERROR: Invalid input.'
                return result
            elif x >= 4 and not isinstance(int(list[x]), int):
                result = 'ERROR: Invalid input.'
                return result
    except:
        list2 = [examination_id, date, time, allergies, medications, height, weight, doctor_id, patient_id]
        if examination_id == '':
            result = 'ERROR: Examination ID is required.'
            return result
        else:
            row = get_examination(examination_id, patient_id)
            if not row:
                result = 'ERROR: Unable to update examination: ' + examination_id
                return result
            else:
                examination = row[0]
            attributes_to_update.append(examination[0])
            for x in range(1, len(examination)):
                if examination[x] != list2[x] and list2[x] != '':
                    try:
                        if isinstance(int(list2[x]), int):
                            attributes_to_update.append(list2[x])
                    except:
                        attributes_to_update.append(str(list2[x]))
                elif examination[x] != list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(examination[x]), int):
                            attributes_to_update.append(examination[x])
                    except:
                        attributes_to_update.append(str(examination[x]))
                elif examination[x] == list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(examination[x]), int):
                            attributes_to_update.append(examination[x])
                    except:
                        attributes_to_update.append(str(examination[x]))
            attributes_to_update.append(examination[0])
            attributes_to_update = tuple(attributes_to_update)
            try:
                query = """UPDATE EXAMINATION SET 
                ExamID = ?, 
                Date = ?, 
                Time = ?, 
                Allergies = ?, 
                Medications = ?, 
                Height_in = ?, 
                Weight_lbs = ?, 
                Doctor = ?, 
                Attendee = ? 
                WHERE ExamID = ?"""
                result = execute_query(conn, query, attributes_to_update)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to update examination: ' + examination_id
                else:
                    result = "Updated examination: " + examination_id
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to update examination: ' + examination_id
        return result
