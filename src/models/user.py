from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .item import Item

"""
This is the User class. It is used to create the users table in the database.
It has a relationship with the Item class, which means that it will add the item to the user when it is added to the database.
"""

class User(Base):
    # Declare the table name
    __tablename__ = 'users'
    # Declare the columns, for more information see the Item class
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # The relationship is used to declare a relationship between the tables
    # When the model owns another model, only the relationship is needed
    items = relationship("Item", back_populates="user")