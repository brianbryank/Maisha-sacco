#!/usr/bin/python3
"""
Main application for Maisha Sacco
"""

import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import User, Accounts, Deposits, Withdrawals
from menu import menu
from tables import Base

# Database connection string
DATABASE_URL = 'sqlite:///database.db'

# Create the database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_account(session):
    """
    Function to create a user account
    """
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")
    
    # Check if the username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("Username already exists. Please choose another one.")
        return
    
    firstname = input("Enter Your First Name: ")
    lastname = input("Enter Your Last Name: ")
    
    try:
        id_no = int(input("Enter Your ID Number: "))
        phone_number = int(input("Enter Your Phone Number: "))
    except ValueError:
        print("Allowed Characters are Integers Only")
        return
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    user = User(username=username, firstname=firstname, lastname=lastname,
                id_no=id_no, PhoneNumber=phone_number, Password=hashed_password)
    
    account = Accounts(user=user, acc_balance=0)
    
    session.add(user)
    session.add(account)
    session.commit()
    print("Account created successfully.")

def login(session):
    """
    Function to handle user login
    """
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.Password):
        print("Successfully Logged In")
        menu(session, user)
    else:
        print("Invalid credentials. Please try again.")

def main():
    while True:
        print("Welcome to Maisha Sacco")
        print("Press 1 to Create Account")
        print("Press 2 to Login")
        print("Press 3 to Exit")
        
        choice = input()
        
        if choice == '1':
            with Session() as session:
                create_account(session)
        elif choice == '2':
            with Session() as session:
                login(session)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
