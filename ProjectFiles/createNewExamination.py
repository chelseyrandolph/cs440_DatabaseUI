import random
from datetime import datetime

from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def createNewExamination(date, time, allergies, medications, height, weight, doctor, patient):
    examID = random.randint(1000, 9999)
    conn = create_connection()
    if not isinstance(datetime.strptime(date, '%m-%d-%Y'), datetime) or not isinstance(datetime.strptime(time, '%H:%M'), datetime):
        text = 'ERROR: Invalid input.'
        return text
    list = [allergies, medications]
    list2 = [height, weight, doctor, patient]
    try:
        for item in list:
            if isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return
        for item in list2:
            if not isinstance(int(item), int):
                text = 'ERROR: Invalid input.'
                return
    except:
        if date != '' and time != '' and allergies != '' and medications != '' and height != '' and weight != '' and doctor != '' and patient != '':
            try:
                date = datetime.strftime(datetime.strptime(date, '%m-%d-%Y'), '%m-%d-%Y')
                time = datetime.strftime(datetime.strptime(time, '%H:%M'), '%H:%M')
                query = """INSERT INTO EXAMINATION(ExamID, Date, Time, Allergies, Medications, Height_in, Weight_lbs, Doctor, Attendee) VALUES (?,?,?,?,?,?,?,?,?)"""
                values = (examID, date, time, allergies, medications, height, weight, doctor, patient)
                result = executeQuery(conn, query, values)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    text = 'ERROR: Unable to add Examination.'
                else:
                    text = "Added patient to table: Examination"
            # If the query fails it prints an error
            except:
                text = 'ERROR: Unable to add Examination.'
        # If the fields aren't filled
        else:
            text = 'ERROR: Missing Information. Please fill out all boxes.'
        return text
