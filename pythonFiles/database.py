import sqlite3
from tabulate import tabulate


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None

    if connection object = None. The connection failed.
    """
    conn = None
    try:
        conn = sqlite3.connect("../Delta_Health_Clinic.db")
    except sqlite3.Error as e:
        print(e)
    return conn


"""
This function selects rows from a table based on a query. 
"""
def executeQuerySelect(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


"""
This function will execute a (INSERT INTO, UPDATE, DELETE) query.
Tested: INSERT INTO, 
"""


def executeQuery(conn, query, values):
    try:
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()
    except:
        text = "Query Failed."
        return text


"""
This function will print a formatted table onto the webpage.
"""
def printTable(rows, header):
    return tabulate(rows, headers=header)
