from db import init_db, engine, session
from models import User, Item
"""
This module is made to initiate the database and read the data from it.
It will call the init_db() function from init_db.py to create the database.
It will call the read_db() function to read the data from the database.
The engine is imported from db.py.
"""
def read_db():
    # Select all users from the database from the engine
    users = session.query(User).all()
    for user in users:
        print('user name: ', user.name)

    # Select all items from the database from the engine
    items = session.query(Item).all()
    for item in items:
        print('item name: ', item.name)


if __name__ == '__main__':
    # Initiate the database
    init_db()
    # Select all users from the database from the engine
    read_db()