import random
import string
import barnum
import names
from create_doctor import *
from faker import Faker

fake = Faker()
for x in range(0, 50):
    firstName = names.get_first_name()
    middleInitial = random.choice(string.ascii_uppercase)
    lastName = names.get_last_name()
    pnum1 = random.randint(100, 999)
    pnum2 = random.randint(100, 999)
    pnum3 = random.randint(1000, 9999)
    phoneNumber = str(pnum1) + "-" + str(pnum2) + "-" + str(pnum3)
    address = fake.address()
    email = fake.email()
    insurN = barnum.create_company_name(biz_type="Health Insurance")
    insurID = random.randint(100000, 99999999)
    date = barnum.create_date()
    hours = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5]
    morning = [8, 9, 10, 11]
    hour = random.choice(hours)
    minutes = [00, 15, 30, 45]
    minute = random.choice(minutes)
    if hour in morning:
        time = str(hour) + ":" + str(minute) + "AM"
    else:
        time = str(hour) + ":" + str(minute) + "PM"
    height = random.randint(58, 78)
    weight = random.randint(120, 275)
    allergies = ''
    medications = ''
    titles = ['General Practitioner', 'Pediatrician', 'Gynecologist', 'Family Physician', 'Psychiatrist']
    title = random.choice(titles)
    # addNewPatient(firstName, middle-initial, last_name, phone_number, address, email, insurance, insurance_id)

    r = create_new_doctor(first_name, middle_initial, last_name, phone_number, email, title)
    print(r + " " + str(x))
# addNewExam(doctorID, patientID, date, time, height, weight, allergies, medications)
# Select doctorID FROM DOCTOR
# Select patientID FROM PATIENT
# combine one from each to make an exam and prescription
# addNewPrescription(doctorID, patientID, medication, instructions)
