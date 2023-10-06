#!/usr/bin/python3
"""
Defines functions for handling the menu in Maisha Sacco
"""

from sqlalchemy.orm import sessionmaker
from tables import Accounts, Deposits, Withdrawals

def prompt_message():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. View Deposit History")
    print("5. View Withdrawal History")
    print("6. Logout")

def deposit(user_details, session):
    """
    Function to handle deposits
    """
    amn_to_dep = int(input("Enter Amount To Deposit: "))
    if amn_to_dep <= 500:
        print("You can only deposit > 500\=")
    else:
        account = session.query(Accounts).filter(Accounts.user_id == user_details.user_id).first()
        deposit = Deposits(user_id=user_details.user_id, amt_deposited=amn_to_dep, acc_balance=account.acc_balance + amn_to_dep)
        session.add(deposit)
        account.acc_balance += amn_to_dep
        session.commit()
        print("Successful deposit of", amn_to_dep)

def withdraw(user_details, session):
    """
    Function to handle withdrawals
    """
    amn_to_withdr = int(input("Enter Amount To Withdraw: "))
    account = session.query(Accounts).filter(Accounts.user_id == user_details.user_id).first()
    
    if amn_to_withdr > account.acc_balance:
        print("Insufficient Funds")
    else:
        withdrawal = Withdrawals(user_id=user_details.user_id, amt_withdrawn=amn_to_withdr, acc_balance=account.acc_balance - amn_to_withdr)
        session.add(withdrawal)
        account.acc_balance -= amn_to_withdr
        session.commit()
        print("Successfully withdrawn:", amn_to_withdr)

def view_balance(user_details, session):
    """
    Function to view account balance
    """
    account = session.query(Accounts).filter(Accounts.user_id == user_details.user_id).first()
    print("Your Account Balance is:", account.acc_balance)

def view_deposit_history(user_details, session):
    """
    Function to view deposit history
    """
    deposits = session.query(Deposits).filter(Deposits.user_id == user_details.user_id).all()
    if not deposits:
        print("No deposit history found.")
    else:
        print("Deposit History:")
        for deposit in deposits:
            print(f"Date: {deposit.dep_date}, Amount: {deposit.amt_deposited}, Balance: {deposit.acc_balance}")

def view_withdrawal_history(user_details, session):
    """
    Function to view withdrawal history
    """
    withdrawals = session.query(Withdrawals).filter(Withdrawals.user_id == user_details.user_id).all()
    if not withdrawals:
        print("No withdrawal history found.")
    else:
        print("Withdrawal History:")
        for withdrawal in withdrawals:
            print(f"Date: {withdrawal.withd_date}, Amount: {withdrawal.amt_withdrawn}, Balance: {withdrawal.acc_balance}")

def menu(session, user_details):
    """
    Function to display and handle the user menu
    """
    while True:
        prompt_message()
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit(user_details, session)
        elif choice == '2':
            withdraw(user_details, session)
        elif choice == '3':
            view_balance(user_details, session)
        elif choice == '4':
            view_deposit_history(user_details, session)
        elif choice == '5':
            view_withdrawal_history(user_details, session)
        elif choice == '6':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")
