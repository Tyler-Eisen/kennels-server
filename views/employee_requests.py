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
  return EMPLOYEES


def get_single_employee(id):
    requested_employee = None
  
    for employee in EMPLOYEES:
     if employee["id"] == id:
      requested_employee = employee

    return requested_employee
  
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
