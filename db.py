from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# Declare the base for the ORM classes
Base = declarative_base()

# Create the SQLite3 engine
engine = create_engine('sqlite:///database.db')