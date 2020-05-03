from database import *
from flask import Flask

app = Flask(__name__)
"""
I don't know what but you must include a link '/result' (doesn't actually exist).
ALWAYS INCLUDE methods=['GET','POST'] when retrieving information!!
"""


@app.route('/result', methods=['GET', 'POST'])
def filterByExamination(filterList, valueList):
    conn = create_connection()
    if len(filterList) != 0:
        try:
            if len(filterList) == 1:
                query = "SELECT * FROM EXAMINATION WHERE " + filterList[0] + " = " + valueList[0] + ";"
                text = executeQuerySelect(conn, query)
            else:
                for x in range(0, len(filterList)):
                    if x == 0:
                        query = "SELECT * FROM EXAMINATION WHERE " + filterList[x] + " = " + valueList[x]
                    elif x < len(filterList) - 1:
                        query += " AND " + filterList[x] + " = " + valueList[x]
                    else:
                        query += " AND " + filterList[x] + " = " + valueList[x] + ";"
                        text = executeQuerySelect(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Examination not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please enter a criteria to filter by.'
    return text
