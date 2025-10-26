import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # leave blank if no MySQL password
        database="hospital_db"
    )
    return conn
