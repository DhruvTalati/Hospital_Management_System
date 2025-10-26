from database import get_connection
from utils import validate_email, validate_mobile

class Patient:
    def __init__(self, name, age, gender, email, mobile, medical_history):
        if not validate_email(email):
            raise ValueError("Invalid email")
        if not validate_mobile(mobile):
            raise ValueError("Invalid mobile")
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.mobile = mobile
        self.medical_history = medical_history

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (name, age, gender, email, mobile, medical_history)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.name, self.age, self.gender, self.email, self.mobile, self.medical_history))
        conn.commit()
        conn.close()
