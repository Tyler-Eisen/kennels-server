EMPLOYEES = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
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
