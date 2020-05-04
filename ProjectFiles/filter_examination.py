from database import *
from flask import Flask

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def filter_by_examination(filter_list, value_list):
    conn = create_connection()
    if len(filter_list) != 0:
        try:
            if len(filter_list) == 1:
                query = "SELECT * FROM EXAMINATION WHERE " + filter_list[0] + " = " + value_list[0] + ";"
                text = execute_query_select(conn, query)
            else:
                for x in range(0, len(filter_list)):
                    if x == 0:
                        query = "SELECT * FROM EXAMINATION WHERE " + filter_list[x] + " = " + value_list[x]
                    elif x < len(filter_list) - 1:
                        query += " AND " + filter_list[x] + " = " + value_list[x]
                    else:
                        query += " AND " + filter_list[x] + " = " + value_list[x] + ";"
                        text = execute_query_select(conn, query)
        # If the query fails it prints an error
        except:
            text = 'ERROR: Examination not found.'
    # If the fields aren't filled
    else:
        text = 'ERROR: Missing Information. Please enter a criteria to filter by.'
    return text
