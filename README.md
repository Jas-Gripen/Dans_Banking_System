# Dans_Banking_System
This is a simple banking system where the userinformation is stored on a database which is utalizing MySQL. The GUI was created using the python library tkinter and the database is handled with MySQL. To run the code you need a database in MySQL name "root" with the password "root". The database should have the columns: id_accounts, username, password, assets.

## Goal of this project
To better understand how to use and implement Python with MySQL.

## Functions
#### Implemented so far
- GUI
- Register user
- Login
- Deposit, withdraw, transfer, view assets, delete account and logout
- Check if user input is valid
- Protect agains SQL injections

#### Upcoming functions
- Confirm that the deposit, withdraw or transfer was succesfull
- Allow the user to upload a profile picture
- Add more user info
- Send confirmation emails to the user when registering and transfering assets to another account

## Future work
- Deploy the database on the cloud
- Figure out the safest way of connecting to the database
- Conduct a threat analysis of the code
- Try to hack the program and steal user credentials
