import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL)
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL)
        ''')


def add_product():
    for i in range(1, 5):
        cursor.execute("INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                    (i, f"Продукт: {i}", f"Описание: {i}", i * 100))
    connection.commit()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                (username, email, age, 1000))
    connection.commit()

def is_included(username):
    user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    if user is None:
        return False
    else:
        return True

def get_all_products():
    cursor.execute('SELECT * FROM Products' )
    return cursor.fetchall()

connection.commit()

if __name__ == '__main__':
    initiate_db()
    add_product()