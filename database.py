# book_database.py

import sqlite3

connection = sqlite3.connect("stationary.db")

def initialize_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Stationary")
    except:
        pass

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stationary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        genre TEXT
    )
    ''')

    for item in [
        {'title': 'Notebook', 'author': 'Stationary Co.', 'genre': 'Office Supplies'},
        {'title': 'Pen Set', 'author': 'Pen Manufacturing', 'genre': 'Writing Tools'},
        {'title': 'Sticky Notes', 'author': 'Stationary Co.', 'genre': 'Office Supplies'},
    ]:
        cursor.execute(f"INSERT INTO Stationary (title, author, genre) VALUES "
                       f"('{item['title']}', '{item['author']}', '{item['genre']}')")

    connection.commit()

def get_all_items():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Stationary")
    columns = [column[0] for column in cursor.description]
    items = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return items

def add_item(title, author, genre):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Stationary (title, author, genre) VALUES "
                   f"('{title}', '{author}', '{genre}')")
    connection.commit()

def get_item_details(item_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Stationary WHERE id = {item_id}")
    columns = [column[0] for column in cursor.description]
    item = dict(zip(columns, cursor.fetchone()))
    return item

def update_item(item_id, title, author, genre):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Stationary SET title = '{title}', author = '{author}', genre = '{genre}' "
                   f"WHERE id = {item_id}")
    connection.commit()

def delete_item(item_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Stationary WHERE id = {item_id}")
    connection.commit()

if __name__ == "__main__":
    initialize_database()
