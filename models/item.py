from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
# Declare the base for the ORM classes


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(String)
    category = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="items")
