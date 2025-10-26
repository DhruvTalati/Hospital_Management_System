from database import get_connection
from utils import validate_email, validate_mobile

class Doctor:
    def __init__(self, name, specialty, email, mobile):
        if not validate_email(email):
            raise ValueError("Invalid email")
        if not validate_mobile(mobile):
            raise ValueError("Invalid mobile")
        self.name = name
        self.specialty = specialty
        self.email = email
        self.mobile = mobile

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO doctors (name, specialty, email, mobile)
            VALUES (%s, %s, %s, %s)
        """, (self.name, self.specialty, self.email, self.mobile))
        conn.commit()
        conn.close()
