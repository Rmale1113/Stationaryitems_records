# book_database.py

import sqlite3

connection = sqlite3.connect("book_store.db")

def initialize_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Books")
    except:
        pass

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        genre TEXT
    )
    ''')

    book_categories = {
        'Stationary': [
            {'title': 'Notebook', 'author': 'Various Authors', 'genre': 'Stationary'},
            {'title': 'Pen Set', 'author': 'Pen Manufacturers', 'genre': 'Stationary'},
        ],
        'Items': [
            {'title': 'Backpack', 'author': 'Bag Designers', 'genre': 'Items'},
            {'title': 'Calendar', 'author': 'Date Keepers', 'genre': 'Items'},
        ]
    }

    for category, books in book_categories.items():
        for book in books:
            cursor.execute(f"INSERT INTO Books (title, author, genre) VALUES "
                           f"('{book['title']}', '{book['author']}', '{book['genre']}')")

    connection.commit()

def get_all_books():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Books")
    columns = [column[0] for column in cursor.description]
    books = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return books

def add_book(title, author, genre):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Books (title, author, genre) VALUES "
                   f"('{title}', '{author}', '{genre}')")
    connection.commit()

def get_book_details(book_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Books WHERE id = {book_id}")
    columns = [column[0] for column in cursor.description]
    book = dict(zip(columns, cursor.fetchone()))
    return book

def update_book(book_id, title, author, genre):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Books SET title = '{title}', author = '{author}', genre = '{genre}' "
                   f"WHERE id = {book_id}")
    connection.commit()

def delete_book(book_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Books WHERE id = {book_id}")
    connection.commit()

if __name__ == "__main__":
    initialize_database()
