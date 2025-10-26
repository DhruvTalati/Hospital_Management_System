from database import get_connection

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, date, time)
            VALUES (%s, %s, %s, %s)
        """, (self.patient_id, self.doctor_id, self.date, self.time))
        conn.commit()
        conn.close()
