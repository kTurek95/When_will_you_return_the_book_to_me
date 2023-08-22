from datetime import datetime
import datetime
import sqlite3
from database import Database


def create_database():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        author TEXT,
        book_title TEXT,
        return_at DATE)''')

    sample_data = [
        ('example@email.com', 'exampleAuthor', 'exampleBook', '2023-08-01'),
        ('test@email.com', 'testAuthor', 'testBook', '2023-08-02'),
        ('random@email.com', 'randomAuthor', 'randomBook', '2023-08-03'),
    ]

    cursor.executemany('INSERT INTO books('
                       'email, author, book_title, return_at)'
                       ' VALUES (?, ?, ?, ?)', sample_data,)

    connection.commit()
    connection.close()


def remove_database():
    import os
    os.remove('library.db')


def test_check_if_the_return_date_of_the_book_has_passed():
    create_database()
    today = datetime.date(2023, 8, 8)
    expected_emails = [
        ('example@email.com',),
        ('test@email.com',),
        ('random@email.com',)
    ]
    library = Database()
    library.create_connection('library.db')
    remove_database()
    assert library.check_if_the_return_date_of_the_book_has_passed(today) == expected_emails


def test_len_check_if_the_return_date_of_the_book_has_passed():
    create_database()
    library = Database()
    library.create_connection('library.db')
    remove_database()
    assert len(library.check_if_the_return_date_of_the_book_has_passed()) == 3


def test_when_was_return_date():
    create_database()
    expected_outcome = [
        datetime.date(2023, 8, 1),
        datetime.date(2023, 8, 2),
        datetime.date(2023, 8, 3)
    ]
    library = Database()
    library.create_connection('library.db')
    remove_database()
    assert library.when_was_return_date() == expected_outcome


def test_len_when_was_return_date():
    create_database()
    library = Database()
    library.create_connection('library.db')
    remove_database()
    assert len(library.when_was_return_date()) == 3