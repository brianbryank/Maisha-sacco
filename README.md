# Maisha Sacco

- Maisha Sacco is a project meant to assist small financial groups automate their transaction processes such as deposits, withdrawals, and loan processing targeting small financial groups such as "CHAMA" in Kenya.
- Maisha Sacco simply provides solutions such as:
	1. Storage of the user data in a database
	2. Automated transactions
---

# PROCESSES
## Creation of an Account
- The system allows creation of an account to new users and ensures each of the users are eligible to the requirementsof the roup such as registration fees and age.
- When a user creates an account he or she is prompted to fill all the fields which upon completion is stored in the database.



## Logging into the System
- The system validates logging into the system. Fisrt, the user is prompted to enter the username. During account creation, the system ensures that a unique username is created.
- The system then prompts the user to enter their password where the entered password is subjected to validation. The system counterchecks the existing password and the entered password for validation. If the account exists, the user is sucessfully logs into the system where they view the menu.
- On the contrary, if there is a mismatch between the created and entered credentials, the system displays the appropriate error message where they are taken back to the login page.


# Components of a Menu
- The system consists of modules such as:
	1. Deposits
	2. Withrawals
	3. Checking account balances
	4. Checking deposit history
	5. Checking withdrawal history
- The system prompts the user upon validation to enter the specified option in which to transact.

  ![Alt text](/img/menu.png)
---

### Deposits
- The system prompts the user to enter the amount of money to deposit into the account. The system verifies whether the inputted amount meets the group requirement or not. If it does not, the appropriate message is displayed to the user.
- If the amount meets the system requirements, the amount is deposited with the transaction registered into the database and the user displayed with the success message.

  ![Alt text](/img/deposits.png)
---

### Withdrawals
- The system prompts the user to enter the withdrawal amount where it undergoes some system validation to ensure the amount inputted meets the group requirement. If the amount is greater than the account balance, an appropriate error message is displayed to the user.
- But upon successful validation, the system records the transaction details and update the balance of the customer. Additionally, the success message will be displayed to the user on complete transaction.

  ![ALt text](/img/withdrawals.png)
---

### Other Processes
- The system returns the outputs of account balance, withdrawals and deposits upon queried by the user.

   ![Alt text](/img/balance.png "Account balance")


   ![Alt text](/img/with_hist.png "Withdrawal history")


   ![Alt text](/img/dep_his.png "Deposits history")
---

## Features yet to be Implemented
1. Loan Processing
2. Monthly and Weekly contributions.


## Project Highlights

### Code Implementation
- Successfully implemented core functionalities, including user registration, login, and transaction processing.
- Users can create accounts, deposit funds, and withdraw funds.

### Database Setup
- Set up an SQLite database to store user information, account details, and transaction history.
- The database is fully operational and integrated with the application.

### User-Friendly Menu System
- Created a menu system for easy navigation through various options such as checking balances, viewing transaction history, and logging out.

### Database Migrations
- Integrated Alembic for managing database schema changes.
- Ensures that the database remains up-to-date as code improvements are made.

### Documentation
- Documented the project's structure and components for better understanding and contribution.
- The documentation provides insights into the project's code organization and usage.

## Usage

To run the Maisha Sacco Banking Application:

1. Ensure you have Python 3 installed on your system.
2. Clone this repository.
3. Set up a virtual environment (optional but recommended).
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Create the SQLite database by running `alembic upgrade head`.
6. Run the application with `python main.py`.

## Project Structure
The project directory structure is organized as follows:

1. main.py: The main script for user authentication and interaction.
2. menu.py: A script handling the user menu and transaction options.
3. tables.py: Defines the database tables using SQLAlchemy ORM.
4. database.db: SQLite database file.
5. alembic/: Directory containing database migrations for SQLAlchemy.
6. alembic/env.py: Configuration file for Alembic migrations.
7. requirements.txt: A list of required Python packages.

## Database
The project uses an SQLite database with the following tables:

users: Stores user information, including username, name, ID number, phone number, and hashed password.
accounts: Stores account information, including user account balance.
deposits: Records deposit transactions, including the deposit amount and date.
withdrawals: Records withdrawal transactions, including the withdrawal amount and date.

## Main Script (main.py)
main.py is the main entry point for the application.
It handles user registration, authentication, and menu navigation.

Functions:

create_account(session): Allows users to create new accounts.
login(session): Handles user login and redirects to the menu.
main(): The main application loop to display the menu.
## Menu Script (menu.py)
menu.py manages user interaction with the menu options.

* Functions:

1. prompt_message(): Displays the menu options.
2. deposit(user_details, session): Handles deposit transactions.
3. withdraw(user_details, session): Handles withdrawal transactions.
4. view_balance(user_details, session): Displays the account balance.
5. view_deposit_history(user_details, session): Displays deposit transaction history.
6. view_withdrawal_history(user_details, session): Displays withdrawal transaction history.
7. menu(user_details, session): The main menu loop.
## Tables Script (tables.py)
tables.py defines the database tables using SQLAlchemy ORM.

* Tables:

1. User: Stores user information.
2. Accounts: Stores account information.
3. Deposits: Records deposit transactions.
4. Withdrawals: Records withdrawal transactions.

## Alembic Migrations
The alembic/ directory contains database migration files for SQLAlchemy.
Alembic is used to manage database schema changes.
Migrations are automatically applied when necessary to keep the database schema up-to-date.



## Contributing

We welcome contributions from the open-source community. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the open-source community for their contributions and support.

For more information, please contact [brian kiplangat] at [brianbryan0125@gmail.com].