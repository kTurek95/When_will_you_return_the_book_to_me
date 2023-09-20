"""
Main module for sending an email using the Message class.

Usage:
    Run this module directly to send an email.

Example:
    $ python main.py
"""

import os
import socket
from message.message import Message


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
