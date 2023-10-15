# When will you return the book to me?

The program is used to check in the database whether the customer has returned the book or not. If not, it sends an email to them with information about the book return deadline and how much time has already passed.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running:
- pip install -r requirements.txt

## Usage

1. Run the **main.py** script to interact with program
2. The program will display a message that the database does not exist and will ask to enter 1 - to create a database, or 0 - to exit the program.
3. After launching the program, information will be displayed about to whom the emails were sent.
4. You can modify the database information in the create_database module within the insert_into_table function.

## Modules

#### **main.py**
The main module containing the main function responsible for the logic of the entire program.
#### **convert.py**
It contains functions for changing the date format.
#### **database.py**
The module contains a class that inherits from the Convert class and is responsible for connecting to the database and retrieving the data contained within it.
#### **information.py**
The module contains a class with three methods, which generate all the necessary information for sending an email.
#### **message.py**
The module with a class that is responsible for creating an email message and setting the necessary parameters for sending the email.
#### **create_database.py**
This module is responsible for the database. It has two functions; one creates the database while the second adds data to it.

## Configuration

This application requires certain environment variables to run correctly. These variables should be defined in a **.env** file at the root of your project.
Create a **.env file**: Start by copying the **.env.dist** file provided in the project root:
- cp .env.dist .env on MacOs
- copy .env.dist .env on Windows
- then you need to add your email details and save it

## Support

If you encounter any issues with my software, please reach out to me:
- Email: k.turek1995@gmail.com

## Dependencies
To run this software, you'll need the libraries and tools listed in requirements.txt

## License

This project is licensed under the MIT License - 
[![Licencja MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
