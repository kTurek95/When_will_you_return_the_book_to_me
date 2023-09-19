def create_table(connection):
    table = '''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    author TEXT,
    book_title TEXT,
    return_at DATE
    )'''

    cursor = connection.cursor()
    cursor.execute(table)
    connection.commit()


def insert_into_table(connection):
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO books 
    (email, author, book_title, return_at) VALUES
    (
    'andy@test.email',
    'Harper Lee',
    'To Kill a Mockingbird',
    '2023-08-22'
),(
    'bryan@test.email',
    'George Orwell',
    '1984',
    '2023-08-01'
),(
    'wendy@test.email',
    'F. Scott Fitzgerald',
    'The Great Gatsby',
    '2023-08-05'
),(
   'lucas@test.email',
   'Jane Austen',
   'Pride and Prejudice',
   '2023-07-31'
),(
   'james@test.email',
   'J.R.R. Tolkien',
   'The Lord of the Rings',
   '2023-09-11'
),(
   'ryan@test.email',
   'Aldous Huxley',
   'Brave New World',
   '2023-08-29'
),(
   'paul@test.email',
   'Gabriel Garcia Marquez',
   'One Hundred Years of Solitude',
   '2023-07-15'
),(
   'tammy@test.email',
   'Fyodor Dostoevsky',
   'Crime and Punisfhment',
   '2023-09-16'
),(
   'garry@test.email',
   'J.D. Salinger',
   'The Catcher in the Rye',
   '2023-10-07'
),(
   'jordan@test.email',
   'Virginia Woolf',
   'To the Lighthouse',
   '2023-06-19'
);''')
