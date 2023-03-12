import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Получаем список чатов пользователя
cursor.execute("SELECT * FROM chats WHERE user1_id=? OR user2_id=?", (user[0], user[0]))
chats = cursor.fetchall()

# Выводим список чатов на экран
print("Список чатов:")
for chat in chats:
    if chat[1] == user[0]:
        cursor.execute("SELECT username FROM users WHERE id=?", (chat[2],))
        partner = cursor.fetchone()[0]
    else:
        cursor.execute("SELECT username FROM users WHERE id=?", (chat[1],))
        partner = cursor.fetchone()[0]
    print(partner)

# Закрываем соединение с базой данных
conn.close()