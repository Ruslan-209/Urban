# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))
#
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', ('500', f'{i}'))
#
# for i in range(1, 10, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))
#
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', ('60',))
# users = cursor.fetchall()
#
# for username, email, age, balance in users:
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# Удалите из базы данных not_telegram.db запись с id = 6:
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчитать общее количество записей:
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
# print(total_users)

# Посчитать сумму всех балансов:
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
# print(all_balance)

# Вывести в консоль средний баланс всех пользователей:
print(float(round((all_balance / total_users))))

connection.commit()
connection.close()