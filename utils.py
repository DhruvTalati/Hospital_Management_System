import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_mobile(mobile):
    pattern = r'^\d{10}$'
    return re.match(pattern, mobile)

def save_report(patient_name, report):
    filename = f"{patient_name}_report.txt"
    with open(filename, 'w') as f:
        f.write(report)
