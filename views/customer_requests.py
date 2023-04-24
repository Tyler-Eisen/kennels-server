import json
import sqlite3
from models import Customer

CUSTOMERS = []
def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM customer a
        """)

        
        customers = []

        
        dataset = db_cursor.fetchall()
        for row in dataset:

        
            customer = Customer(row['id'], row['name'], row['address'])

            customers.append(customer.__dict__) 

    return customers


def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        
        data = db_cursor.fetchone()

        
        customer = Customer(data['id'], data['name'], data['address'],
                            )

        return customer.__dict__
  
def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer ["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
