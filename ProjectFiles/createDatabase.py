import sqlite3
from database import *

conn = create_connection()
c = conn.cursor()
queries = [
    "CREATE TABLE IF NOT EXISTS PATIENT("
    "PatientID INTEGER NOT NULL PRIMARY KEY UNIQUE, "
    "FirstName VARCHAR(50) NOT NULL, "
    "MiddleInitial CHAR(1) NOT NULL, "
    "LastName VARCHAR(50) NOT NULL, "
    "PhoneNumber VARCHAR(12) NOT NULL, "
    "Address VARCHAR(250) NOT NULL, "
    "Email VARCHAR(250), "
    "InsuranceName VARCHAR(250) NOT NULL, "
    "InsuranceID VARCHAR(100) NOT NULL"
    "CONSTRAINT insurance UNIQUE (InsuranceName,InsuranceID))",

    "CREATE TABLE IF NOT EXISTS DOCTOR("
    "DoctorID INTEGER NOT NULL PRIMARY KEY UNIQUE, "
    "FirstName VARCHAR(50) NOT NULL, "
    "MiddleInitial CHAR(1) NOT NULL, "
    "LastName VARCHAR(50) NOT NULL, "
    "PhoneNumber VARCHAR(12) NOT NULL UNIQUE, "
    "Email VARCHAR(250) NOT NULL UNIQUE, "
    "Title VARCHAR(50) NOT NULL)",

    "CREATE TABLE IF NOT EXISTS EXAMINATION("
    "ExamID INTEGER NOT NULL PRIMARY KEY UNIQUE, "
    "Date DATE NOT NULL, "
    "Time VARCHAR(7) NOT NULL, "
    "Allergies VARCHAR(250), "
    "Medications VARCHAR(250), "
    "Height_in INTEGER NOT NULL, "
    "Weight_lbs INTEGER NOT NULL, "
    "Doctor INTEGER NOT NULL, "
    "Attendee INTEGER NOT NULL, "
    "FOREIGN KEY (Doctor) REFERENCES Doctor(DoctorID), "
    "FOREIGN KEY (Attendee) REFERENCES Patient(PatientID))",

    "CREATE TABLE IF NOT EXISTS PRESCRIPTION("
    "Doctor INTEGER NOT NULL, "
    "Patient INTEGER NOT NULL, "
    "Medication VARCHAR(100) NOT NULL PRIMARY KEY UNIQUE, "
    "Instructions VARCHAR(250) NOT NULL, "
    "FOREIGN KEY (Doctor) REFERENCES Doctor(DoctorID), "
    "FOREIGN KEY (Patient) REFERENCES Patient(PatientID))"]
try:
    for query in queries:
        c.execute(query)
except sqlite3.OperationalError as e:
    print('sqlite error:', e.args[0])

conn.commit()

conn.close()

print('done')
