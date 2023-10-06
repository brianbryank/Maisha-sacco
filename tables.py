from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Database connection string
DATABASE_URL = 'sqlite:///database.db'

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session for database operations
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    id_no = Column(Integer, nullable=False)
    PhoneNumber = Column(Integer)
    Password = Column(String(100))

    # Relationships
    accounts = relationship('Accounts', back_populates='user')
    registration = relationship('Registration', back_populates='user')
    deposits = relationship('Deposits', back_populates='user')
    withdrawals = relationship('Withdrawals', back_populates='user')

class Accounts(Base):
    __tablename__ = 'accounts'

    acc_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    acc_balance = Column(Integer, default=0)

    # Relationships
    user = relationship('User', back_populates='accounts')

class Registration(Base):
    __tablename__ = 'registration'

    reg_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    registrationfee = Column(Integer, default=1000)

    # Relationships
    user = relationship('User', back_populates='registration')

class Deposits(Base):
    __tablename__ = 'deposits'

    dep_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    dep_date = Column(DateTime, default=datetime.now())
    amt_deposited = Column(Integer)
    acc_balance = Column(Integer)

    # Relationships
    user = relationship('User', back_populates='deposits')

class Withdrawals(Base):
    __tablename__ = 'withdrawals'

    withd_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    withd_date = Column(DateTime, default=datetime.now())
    amt_withdrawn = Column(Integer)
    acc_balance = Column(Integer)

    # Relationships
    user = relationship('User', back_populates='withdrawals')

# Create the tables in the database
Base.metadata.create_all(engine)
