from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
# Declare the base for the ORM classes

"""
This is the Item class. It is used to create the items table in the database.
It has a relationship with the User class, which means that it will add the user to the item when it is added to the database.
"""

class Item(Base):
    # Declare the table name
    __tablename__ = 'items'

    # Declare the columns
    # primary_key=True means that this is the primary key for the table
    # each primary key must be unique and will aways an integer
    id = Column(Integer, primary_key=True)


    # String is the type of the column, it can be Integer, Float, String, Boolean, Date, DateTime, Time, LargeBinary, PickleType, Unicode, UnicodeText
    # The length of the string can be declared by adding a number in the brackets
    # Example: String(255)
    # The default value can be declared by adding a default value in the brackets
    # Example: String(255, default='John')
    # The nullable value can be declared by adding a nullable value in the brackets
    # Example: String(255, nullable=False)
    # The unique value can be declared by adding a unique value in the brackets
    # Example: String(255, unique=True)
    name = Column(String)
    description = Column(String)
    price = Column(String)
    category = Column(String)

    # The ForeignKey is used to declare a foreign key
    # The foreign key is used to connect the tables together
    # The foreign key must be the same type as the primary key of the table it is connected to (in this case the User class)
    # The foreign key must be unique
    # The foreign key must be an integer
    user_id = Column(Integer, ForeignKey('users.id'))

    # The relationship is used to declare a relationship between the tables
    # The relationship is used to connect the tables together
    # The relationship must be the same type as the primary key of the table it is connected to (in this case the User class)
    user = relationship("User", back_populates="items")
