"""
Main module for sending an email using the Message class.

Usage:
    Run this module directly to send an email.

Example:
    $ python main.py
"""

import os
import socket
import sqlite3

from message.message import Message
from create_database import create_table, insert_into_table


def main():
    """
    This function checks if the specified database file exists, creates a connection to it,
    and attempts to send an email using the Message class.

    Raises:
        Exception: If the email sending process fails.

    Returns:
        None
    """

    db_file = 'database.db'

    if not os.path.isfile(db_file):
        print('The specified database file does not exist.')
        user_answer = input('If you want to create a database, press 1 if not press 0: ')
        if user_answer == '1':
            with sqlite3.connect('database.db') as connection:
                create_table(connection)
                insert_into_table(connection)
                print('The database has been created')
        else:
            quit()
        return

    message = Message()
    message.create_connection(db_file)
    try:
        if not message.send_mail():
            raise Exception
    except socket.gaierror:
        print('The message sending failed')


if __name__ == '__main__':
    main()
