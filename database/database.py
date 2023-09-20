"""Module with Database class"""

import sqlite3
from datetime import datetime
from convert.convert import Convert


class Database(Convert):
    """
    Class handling a database of books and their return dates.
    Inherits from the Convert class, allowing date conversion.
    """
    def __init__(self):
        """
        Initializes a Database object.

        self.cursor: database cursor object
        self.data: list to store query results
        """
        self.cursor = None
        self.data =[]

    def create_connection(self, database):
        """
        Creates a connection to the database.

        :param database: path to the database file
        :return: database cursor object
        """
        with sqlite3.connect(database) as connection:
            self.cursor = connection.cursor()
            return self.cursor

    def check_if_the_return_date_of_the_book_has_passed(self, today=None):
        """
        Checks if the return date of a book has passed.

        :param today: current date (default is None)
        :return: list of email addresses of people whose book return date has passed
        """
        if today is None:
            today = datetime.today().date()
        self.cursor.execute('SELECT email FROM books WHERE return_at < ?', (today,))
        for book in self.cursor.fetchall():
            book_email = book
            self.data.append(book_email)

        return self.data

    def when_was_return_date(self):
        """
        Retrieves return dates of books from the database and converts them to a list of datetime objects.

        :return: list of datetime objects representing book return dates
        """
        date_from_db = []
        self.cursor.execute('SELECT return_at FROM books')
        for book in self.cursor.fetchall():
            date_from_db.append(book[0])

        dates = [self.convert_to_date(date) for date in date_from_db]

        return dates
