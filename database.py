import sqlite3
from datetime import datetime
from convert import Convert


class Database(Convert):
    def __init__(self):
        self.cursor = None
        self.data =[]

    def create_connection(self, database):
        with sqlite3.connect(database) as connection:
            self.cursor = connection.cursor()
            return self.cursor

    def check_if_the_return_date_of_the_book_has_passed(self, today=None):
        if today is None:
            today = datetime.today().date()
        self.cursor.execute('SELECT email FROM books WHERE return_at < ?', (today,))
        for book in self.cursor.fetchall():
            book_email = book
            self.data.append(book_email)

        return self.data

    def when_was_return_date(self):
        date_from_db = []
        self.cursor.execute('SELECT return_at FROM books')
        for book in self.cursor.fetchall():
            date_from_db.append(book[0])

        dates = [self.convert_to_date(date) for date in date_from_db]

        return dates
