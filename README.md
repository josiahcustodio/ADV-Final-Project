
IF THE CODE HAS BUGS ON FUNCTIONS AFTER REGISTERING USE THIS LOGIN INFO
username: josh
password: 123

# ADV-Final-Project
CS121 Final Projecy

Table of Contents
Introduction
Features
System Requirements
Installation
Usage Instructions
Contributing
License
Introduction
The SkillMatch App is a skill exchange platform where users can register, trade skills, and learn from others. It focuses on connecting people with varying skill sets, enabling them to either exchange services (via skill trade) or learn from professionals. The app integrates a credit-based system where users can top up their credits to learn new skills from professionals or use credits for skill trades.

The app aims to create a collaborative environment where users can improve their skills and offer services to others, contributing to Decent Work and Economic Growth and promoting Quality Education (aligned with SDG 4 and SDG 8). By fostering skill-sharing, the system also enables users to access learning opportunities, particularly for those from underrepresented backgrounds, ensuring equal access to education and economic opportunities.

Features
User Registration: Register by providing basic personal details, skills, and other necessary information.
User Login: Allows registered users to log in and access their profile.
Skill Trading: Users can exchange skills with each other.
Learning Opportunities: Users can pay credits to learn new skills from professional users.
Top-Up Credits: Users can purchase credits to use for learning or trading skills.
View All Registered Users: A feature to view the profiles of all users in the system.
Account Management: Options for users to delete their accounts or log out.
Admin Features: Admin can delete all users from the database (use with caution).
Database Integration: Utilizes a database to store user information and credits.
System Requirements
Python 3.x
SQLite (or another supported relational database)
Basic command-line interface (CLI) environment
The skillmatchDB Python module must be configured for database interactions.
Required Python Libraries
os (for clearing the screen)
time (for delays)
sqlite3 (or any other relevant DB library)
skillmatchDB (custom database handler module)
Ensure you have all necessary libraries installed before running the app. You may need to install the required libraries using pip.

Installation
Clone the Repository:

bash
Copy code
https://github.com/josiahcustodio/ADV-Final-Project
cd SkillMatchApp
Set up the Database: The system uses a SQLite database. Ensure that skillmatchDB.py handles the creation of tables and any necessary database setup.

You can create the database by running the Python script:

bash
Copy code
python setup_db.py
This will create all the required tables for the app to function properly.

Install Dependencies: If any external dependencies are required, install them using pip:

bash
Copy code
pip install -r requirements.txt
Run the Application: Once everything is set up, run the app using:

bash
Copy code
python skillmatch_app.py
Usage Instructions
Main Menu
Upon starting the application, you'll be prompted with the following main menu options:

Login: Allows you to log in using your registered credentials.
Register: Create a new account by providing your personal details, skills, and username/password.
Exit: Close the application.
After Login
Once logged in, the main menu will show options based on your account status:

Trade Skills: Trade skills with other users.
Learn a Skill: Learn skills from professional users by using credits.
Top Up Credits: Purchase additional credits to be used for learning or skill trading.
View All Registered Users: View a list of all users in the system.
Logout: Log out from the current session.
Delete Account: Permanently delete your account and all associated data.
Delete All Users (Admin-only feature): Delete all users from the system (irreversible action).
Exit: Close the application.
Top Up Credits
You can purchase credits using the following options:

1000 credits for 799 Pesos
499 credits for 449 Pesos
200 credits for 189 Pesos
100 credits for 99 Pesos
Once you choose an option, the credits will be added to your balance, and the system will confirm the new balance.

Trade Skills
You can trade skills with other users by selecting a skill tag (e.g., Music, Coding). The system will display matching profiles, and you can choose to initiate a trade.

Learn a Skill
Select a skill tag and view a list of professionals offering that skill. Each session costs 50 credits.

Account Management
Logout: Logs the user out and returns to the main menu.
Delete Account: Permanently deletes your account from the system. This action is irreversible.
Delete All Users: Admin can delete all users from the system (use with caution).
Contributing
Contributions to the SkillMatch App are welcome! If you would like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Create a pull request.
Please ensure that your changes align with the current code structure and are well-documented.

License
This project is licensed under the MIT License - see the LICENSE file for details.
