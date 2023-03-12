import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Получаем данные о пользователе, с которым нужно начать чат
chat_username = 'user456'
cursor.execute("SELECT * FROM users WHERE username=?", (chat_username,))
chat_user = cursor.fetchone()

# Проверяем, что пользователи подписаны друг на друга
cursor.execute("SELECT * FROM subscriptions WHERE user_id=? AND subscribe_user_id=?", (user[0], chat_user[0]))
subscription1 = cursor.fetchone()
cursor.execute("SELECT * FROM subscriptions WHERE user_id=? AND subscribe_user_id=?", (chat_user[0], user[0]))
subscription2 = cursor.fetchone()

if subscription1 and subscription2:
    print(f"{user[1]} and {chat_user[1]} can chat")
    # Добавляем сообщение в таблицу messages
    message_text = "Hello, how are you?"
    cursor.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", (user[0], chat_user[0], message_text))
    conn.commit()
    print(f"{user[1]} sent a message to {chat_user[1]}")
else:
    print("Users are not subscribed to each other")

# Закрываем соединение с базой данных
conn.close()