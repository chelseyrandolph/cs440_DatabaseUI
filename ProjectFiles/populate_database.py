import random
import string
import barnum
import names
from create_doctor import *
from create_patient import *
from create_examination import *
from create_prescription import *
from faker import Faker


def populate():
    fake = Faker()
    for x in range(0, 50):
        first_name = names.get_first_name()
        middle_initial = random.choice(string.ascii_uppercase)
        last_name = names.get_last_name()
        pnum1 = random.randint(100, 999)
        pnum2 = random.randint(100, 999)
        pnum3 = random.randint(1000, 9999)
        phone_number = str(pnum1) + "-" + str(pnum2) + "-" + str(pnum3)
        address = fake.address()
        email = fake.email()
        insurance = barnum.create_company_name(biz_type="Health Insurance")
        insurance_id = random.randint(100000, 99999999)
        titles = ['General Practitioner', 'Pediatrician', 'Gynecologist', 'Family Physician', 'Psychiatrist']
        title = random.choice(titles)
        create_new_patient(first_name, middle_initial, last_name, phone_number, address, email, insurance, insurance_id)
        create_new_doctor(first_name, middle_initial, last_name, phone_number, email, title)

    query = "SELECT DoctorID from DOCTOR"
    conn = create_connection()
    result = execute_query_select(conn, query)
    query2 = "SELECT PatientID from PATIENT"
    result2 = execute_query_select(conn, query2)
    doctor_ids = []
    patient_ids = []
    instructions_list = ['Take one pill daily.', 'Take with food.', '10mg daily.', 'Take for 6 days.',
                         'Take one pill twice daily.', 'Take before bed.', '200mg twice a day.', 'Take as needed.',
                         'Take 5 pills for day 1, 4 pills for day 2, 3 pills for day 3, 2 pills for day 4, 1 pill for day 4']
    medications_list = ['Vicodin', 'Simvastatin', 'Lisinopril', 'Levothyroxine', 'Azithromycin', 'Metformin', 'Lipitor',
                        'Amlodipine', 'Amlodipine', 'Amoxicillin', 'Hydrochlorothiazide', 'Synthroid', 'Crestor',
                        'Ventolin', 'Nexium', 'Advair Diskus', 'Lantus Solostar', 'Vyvanse', 'Lyrica',
                        'Spiriva Handihaler', 'Januvia', 'Humira', 'Abilify', 'Sovaldi', 'Albuterol', 'Losartan']
    allergies_list = ['amoxicillin', 'ampicillin', 'penicillin', 'tetracycline', ' ibuprofen', 'naproxen', 'bactrium']
    hours = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5]
    morning = [8, 9, 10, 11]
    minutes = [00, 15, 30, 45]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    thirty_days = [9, 4, 6, 11]

    for x in result:
        doctor_ids.append(x[0])
    for x in result2:
        patient_ids.append(x[0])

    for y in range(0, 50):
        instructions = random.choice(instructions_list)
        patient_id = random.choice(patient_ids)
        doctor_id = random.choice(doctor_ids)
        patient_id2 = random.choice(patient_ids)
        doctor_id2 = random.choice(doctor_ids)
        hour = random.choice(hours)
        minute = random.choice(minutes)
        month = random.choice(months)
        if month not in thirty_days and month != 2:
            day = random.randint(1, 31)
        else:
            if month == 2:
                day = random.randint(1, 28)
            else:
                day = random.randint(1, 30)
        year = random.randint(2018, 2020)
        date = str(month) + "-" + str(day) + "-" + str(year)
        if hour in morning:
            time = str(hour) + ":" + str(minute)
        else:
            time = str(hour) + ":" + str(minute)
        height = random.randint(58, 78)
        weight = random.randint(120, 275)
        allergies = ''
        medications = ''
        if y % 9 == 0:
            allergies = random.choice(allergies_list)
        if y % 3 == 0:
            medications = random.choice(medications_list)
        medication = random.choice(medications_list)
        create_new_examination(date, time, allergies, medications, height, weight, doctor_id, patient_id)
        create_new_prescription(doctor_id2, patient_id2, medication, instructions)
    print("Populated database.")


populate()
