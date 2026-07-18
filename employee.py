import json
from utils import get_valid_amount, get_valid_name

employee_data = {}

def add_employee():
    employee_id = input ("Enter employee ID: ")
    name = get_valid_name("Enter Employee name: ")
    department = input ("Enter Department: ")
    salary = get_valid_amount("Enter Salary: ")

    employee_data[employee_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
    save_data()
    print("Employee added Successfully.")

def view_employees():
    if not employee_data:
        print("No employees found.")
    else:
        for emp_id, details in employee_data.items():
            print(f"ID: {emp_id}, Name: {details['name']}, "   f"Department: {details['department']}, Salary: ${details['salary']}")

def save_data():
    with open("employees.json", "w") as f:
        json.dump(employee_data, f, indent=4)

def load_data():
    global employee_data
    try:
        with open("employees.json", "r") as f:
            employee_data = json.load(f)
    except FileNotFoundError:
        employee_data = {}