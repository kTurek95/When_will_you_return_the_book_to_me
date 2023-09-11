import os
import socket

from message import Message


def main():
    db_file = 'Information.db'

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
