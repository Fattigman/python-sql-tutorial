from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from db import session
from models import User, Item

from db import engine, Base

"""
When init_db is run, it will create the database and add a new user to the database.
It will also add a new item to the database, that belongs to the user.
It imports the User and Item classes from models. It also imports the engine and Base from db.
"""
def init_db():
    if not database_exists(engine.url):
        print('Creating database...')

        # Create the tables in the database
        # Base class uses the models to create the tables which is declared in the models/<model>.py file.
        # This is when NOT using alembic
        Base.metadata.create_all(engine)
        # Add a new user and item to the database
        user = User(name='John', email='john@example.com')
        # The user is added to the database, and since we use the relationship in the Item class, the user is also added to the item with no extra code.
        # Just remember to use the user class object when creating the item object.
        item = Item(name='Item 1', description='Description 1', price='10.00', category='Category 1', user=user)
        # I hope I dont need to explain this
        # But these are the functions that add the data to the database
        session.add(user)
        session.add(item)
        # Commit the changes to the database
        # This will save the changes to the database
        # Otherwise the changes will be lost
        session.commit()
        print('Database created!')
