from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .item import Item

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    items = relationship("Item", back_populates="user")