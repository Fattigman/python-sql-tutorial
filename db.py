from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

"""
This module is made to initiate the database.
"""

# Declare the base for the ORM classes, this is used to create the tables in the database by importing it in the models.
Base = declarative_base()

# Create the SQLite3 engine. This is used to interact with the database.
# The input to create_engine is the URI of the database.
# The URI is the location of the database, in this case it is a SQLite3 database.
# The SQLite3 database is stored in the same folder as the app.py file.
# The database is called database.db
engine = create_engine('sqlite:///database.db')