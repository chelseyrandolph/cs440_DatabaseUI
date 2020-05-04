from database import *
import random
from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def create_new_examination(date, time, allergies, medications, height, weight, doctor_id, patient_id):
    examination_id = random.randint(1000, 9999)
    conn = create_connection()
    if not isinstance(datetime.strptime(date, '%m-%d-%Y'), datetime) or not isinstance(datetime.strptime(time, '%H:%M'), datetime):
        result = 'ERROR: Invalid input.'
        return result
    list = [allergies, medications]
    list2 = [height, weight, doctor_id, patient_id]
    try:
        for item in list:
            if isinstance(int(item), int):
                result = 'ERROR: Invalid input.'
                return
        for item in list2:
            if not isinstance(int(item), int):
                result = 'ERROR: Invalid input.'
                return
    except:
        if date != '' and time != '' and height != '' and weight != '' \
                and doctor_id != '' and patient_id != '':
            try:
                date = datetime.strftime(datetime.strptime(date, '%m-%d-%Y'), '%m-%d-%Y')
                time = datetime.strftime(datetime.strptime(time, '%H:%M'), '%H:%M')
                query = """INSERT INTO EXAMINATION(ExamID, Date, Time, Allergies, Medications, Height_in, Weight_lbs, 
                Doctor, Attendee) VALUES (?,?,?,?,?,?,?,?,?)"""
                values = (examination_id, date, time, allergies, medications, height, weight, doctor_id, patient_id)
                result = execute_query(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to create Examination.'
                else:
                    result = "Added examination to table: EXAMINATION"
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to add Examination.'
        # If the fields aren't filled
        else:
            result = 'ERROR: Missing Information. Please fill out all boxes.'
        return result
