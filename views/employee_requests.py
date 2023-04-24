import json
import sqlite3
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Barb Dwyer",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Ian Snail",
        "address": "209 Emory Drive"
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM employee a
        """)

        
        employees = []

        
        dataset = db_cursor.fetchall()
        for row in dataset:

        
            employee = Employee(row['id'], row['name'], row['address'])

            employees.append(employee.__dict__) 

    return employees


def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        
        data = db_cursor.fetchone()

        
        employee = Employee(data['id'], data['name'], data['address'],
                            )

        return employee.__dict__
  
def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee ["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
