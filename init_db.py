from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from models import User, Item

from db import engine, Base


def init_db():
    if not database_exists(engine.url):
        print('Creating database...')

        # Create the tables in the database
        Base.metadata.create_all(engine)
        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        # Add a new user to the database
        user = User(name='John', email='john@example.com')
        item = Item(name='Item 1', description='Description 1', price='10.00', category='Category 1', user=user)
        session.add(user)
        session.add(item)
        session.commit()
        print('Database created!')
