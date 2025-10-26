import tkinter as tk
from tkinter import messagebox
from database import get_connection
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from utils import save_report

root = tk.Tk()
root.title("Hospital Management System")

# ------------------- Patient Registration -------------------
def register_patient():
    try:
        patient = Patient(
            entry_name.get(),
            int(entry_age.get()),
            gender_var.get(),
            entry_email.get(),
            entry_mobile.get(),
            entry_history.get("1.0", tk.END)
        )
        patient.save()
        messagebox.showinfo("Success", "Patient registered successfully")
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_mobile.delete(0, tk.END)
        entry_history.delete("1.0", tk.END)
        refresh_patients_doctors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_patient_report():
    save_report(entry_name.get(), entry_history.get("1.0", tk.END))
    messagebox.showinfo("Saved", "Report saved successfully")

# Patient Widgets
tk.Label(root, text="Patient Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Gender").grid(row=2, column=0)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2)

tk.Label(root, text="Email").grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

tk.Label(root, text="Mobile").grid(row=4, column=0)
entry_mobile = tk.Entry(root)
entry_mobile.grid(row=4, column=1)

tk.Label(root, text="Medical History").grid(row=5, column=0)
entry_history = tk.Text(root, height=5, width=30)
entry_history.grid(row=5, column=1, columnspan=2)

tk.Button(root, text="Register Patient", command=register_patient).grid(row=6, column=1)
tk.Button(root, text="Save Report", command=save_patient_report).grid(row=6, column=2)

# ------------------- Doctor Registration -------------------
def register_doctor():
    try:
        doctor = Doctor(
            entry_doc_name.get(),
            entry_specialty.get(),
            entry_doc_email.get(),
            entry_doc_mobile.get()
        )
        doctor.save()
        messagebox.showinfo("Success", "Doctor registered successfully")
        entry_doc_name.delete(0, tk.END)
        entry_specialty.delete(0, tk.END)
        entry_doc_email.delete(0, tk.END)
        entry_doc_mobile.delete(0, tk.END)
        refresh_patients_doctors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Doctor Widgets
tk.Label(root, text="Doctor Name").grid(row=7, column=0)
entry_doc_name = tk.Entry(root)
entry_doc_name.grid(row=7, column=1)

tk.Label(root, text="Specialty").grid(row=8, column=0)
entry_specialty = tk.Entry(root)
entry_specialty.grid(row=8, column=1)

tk.Label(root, text="Email").grid(row=9, column=0)
entry_doc_email = tk.Entry(root)
entry_doc_email.grid(row=9, column=1)

tk.Label(root, text="Mobile").grid(row=10, column=0)
entry_doc_mobile = tk.Entry(root)
entry_doc_mobile.grid(row=10, column=1)

tk.Button(root, text="Register Doctor", command=register_doctor).grid(row=11, column=1)

# ------------------- Appointment Booking -------------------
def get_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients

def get_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT doctor_id, name FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def book_appointment():
    try:
        appointment = Appointment(
            patient_var.get(),
            doctor_var.get(),
            entry_date.get(),
            entry_time.get()
        )
        appointment.save()
        messagebox.showinfo("Success", "Appointment booked successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Appointment Widgets
tk.Label(root, text="Select Patient").grid(row=12, column=0)
patient_var = tk.IntVar()
patient_menu = tk.OptionMenu(root, patient_var, ())
patient_menu.grid(row=12, column=1)

tk.Label(root, text="Select Doctor").grid(row=13, column=0)
doctor_var = tk.IntVar()
doctor_menu = tk.OptionMenu(root, doctor_var, ())
doctor_menu.grid(row=13, column=1)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=14, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=14, column=1)

tk.Label(root, text="Time (HH:MM)").grid(row=15, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=15, column=1)

tk.Button(root, text="Book Appointment", command=book_appointment).grid(row=16, column=1)

# ------------------- Refresh Dropdowns -------------------
def refresh_patients_doctors():
    patients_list = get_patients()
    doctors_list = get_doctors()

    patient_menu['menu'].delete(0, 'end')
    for p in patients_list:
        patient_menu['menu'].add_command(label=f"{p[1]} ({p[0]})", command=tk._setit(patient_var, p[0]))

    doctor_menu['menu'].delete(0, 'end')
    for d in doctors_list:
        doctor_menu['menu'].add_command(label=f"{d[1]} ({d[0]})", command=tk._setit(doctor_var, d[0]))

# Initialize dropdowns
refresh_patients_doctors()

root.mainloop()
