from init_db import init_db
from db import engine

"""
This module is made to initiate the database and read the data from it.
It will call the init_db() function from init_db.py to create the database.
It will call the read_db() function to read the data from the database.
The engine is imported from db.py.
"""
def read_db():
    # Select all users from the database from the engine
    users = engine.execute('SELECT * FROM users')
    for user in users:
        print(user)

    # Select all items from the database from the engine
    items = engine.execute('SELECT * FROM items')
    for item in items:
        print(item)


if __name__ == '__main__':
    # Initiate the database
    init_db()
    # Select all users from the database from the engine
    read_db()

