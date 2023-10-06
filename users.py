#!/usr/bin/python3
"""
defines a class User
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
# contains string for the database
DATABASE_URL = 'sqlite:///database.db'
# creates a connection to our database
engine = create_engine(DATABASE_URL)


class User(Base):
    """
    Table for Users
    """
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    id_no = Column(Integer, nullable=False)
    PhoneNumber = Column(Integer)
    Password = Column(String(50))

Base.metadata.create_all(engine)