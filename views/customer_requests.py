import sqlite3
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Derrick Henry",
        "email": "titanup@titans.com"
    },
    {
        "id": 2,
        "name": "Michael Jordan",
        "email": "mjordan@bulls.com"
    },
    {
        "id": 3,
        "name": "Stephen Curry",
        "email": "splashbro@gs.com"
    }
]


def get_all_customers():
    "farts"
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    """notes section"""
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """docstring"""
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def get_customers_by_email(email):
    """docstring"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers
