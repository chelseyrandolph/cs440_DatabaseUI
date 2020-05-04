from database import *
from search_patient import *

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def update_patient_entry(patient_id, first_name, middle_initial, last_name, phone_number, address, email, insurance,
                         insurance_id):
    conn = create_connection()
    list = [first_name, middle_initial, last_name, phone_number, address, email, insurance, insurance_id]
    no_update_flag = 0
    for item in list:
        if not item:
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
        list2 = [patient_id, first_name, middle_initial, last_name, phone_number, address, email, insurance, insurance_id]
        if patient_id == '':
            result = "ERROR: Patient ID is required."
            return result
        else:
            row = get_patient(first_name, middle_initial, last_name, patient_id)
            if not row:
                result = 'ERROR: Unable to update patient: ' + patient_id
                return result
            else:
                patient = row[0]
            attributes_to_update.append(patient[0])
            for x in range(1, len(patient)):
                if patient[x] != list2[x] and list2[x] != '':
                    try:
                        if isinstance(int(list2[x]), int):
                            attributes_to_update.append(list2[x])
                    except:
                        attributes_to_update.append(str(list2[x]))
                elif patient[x] != list2[x] and list2[x] == '':
                    try:
                        if isinstance(int(patient[x]), int):
                            attributes_to_update.append(patient[x])
                    except:
                        attributes_to_update.append(str(patient[x]))
            attributes_to_update.append(patient[0])
            attributes_to_update = tuple(attributes_to_update)
            try:
                query = """UPDATE PATIENT SET 
                PatientID = ?, 
                FirstName = ?, 
                MiddleInitial = ?, 
                LastName = ?, 
                PhoneNumber = ?, 
                Address = ?, 
                Email = ?, 
                InsuranceName = ?, 
                InsuranceID = ? 
                WHERE PatientID = ?"""
                result = execute_query(conn, query, attributes_to_update)
                # If the query fails it prints an error
                if result == "Query Failed.":
                    result = 'ERROR: Unable to update patient: ' + patient_id
                else:
                    result = "Updated patient: " + patient_id
            # If the query fails it prints an error
            except:
                result = 'ERROR: Unable to update patient: ' + patient_id
    return result
