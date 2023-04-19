CUSTOMERS = [
    {
        "id": 1,
        "name": "Ben Dover",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Seymour Butts",
        "address": "209 Emory Drive"
    }
]

def get_all_customers():
  return CUSTOMERS


def get_single_customer(id):
    requested_customer = None
  
    for employee in CUSTOMERS:
     if employee["id"] == id:
      requested_customer = employee

    return requested_customer
  
def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer ["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
