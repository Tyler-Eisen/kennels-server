import json
import sqlite3
from models import Location

LOCATIONS = []


def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        
        locations = []

        
        dataset = db_cursor.fetchall()
        for row in dataset:

        
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__) 

    return locations


def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        
        data = db_cursor.fetchone()

        
        location = Location(data['id'], data['name'], data['address'],
                            )

        return location.__dict__

def delete_location(id):
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location ["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)
        
def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
