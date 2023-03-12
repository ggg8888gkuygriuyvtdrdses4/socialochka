import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Получаем данные о пользователе, на которого нужно подписаться
subscribe_username = 'user456'
cursor.execute("SELECT * FROM users WHERE username=?", (subscribe_username,))
subscribe_user = cursor.fetchone()

# Если оба пользователя найдены, добавляем подписку в базу данных
if user and subscribe_user:
    cursor.execute("INSERT INTO subscriptions (user_id, subscribe_user_id) VALUES (?, ?)", (user[0], subscribe_user[0]))
    conn.commit()
    print(f"{user[1]} has subscribed to {subscribe_user[1]}")
else:
    print("User not found")

# Закрываем соединение с базой данных
conn.close()