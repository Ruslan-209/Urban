import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL);
    ''')
    connection.commit()

def add_product():
    for i in range(1, 5):
        cursor.execute("INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                    (i, f"Продукт: {i}", f"Описание: {i}", i * 100))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products' )
    return cursor.fetchall()


connection.commit()
if __name__ == '__main__':
    initiate_db()
    add_product()