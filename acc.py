 
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Если пользователь найден, выводим его данные на страницу
if user:
    print(f"Username: {user[1]}")
    print(f"Password: {user[2]}")
else:
    print("User not found")

    import sqlite3

 
# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Получаем список всех постов пользователя
cursor.execute("SELECT * FROM posts WHERE user_id=?", (user[0],))
posts = cursor.fetchall()

# Выводим список всех постов на экран
print("Список всех постов пользователя:")
for post in posts:
    print(post[2])

# Получаем список всех подписчиков пользователя
cursor.execute("SELECT * FROM followers WHERE user_id=?", (user[0],))
followers = cursor.fetchall()

# Выводим список всех подписчиков на экран
print("Список всех подписчиков пользователя:")
for follower in followers:
    cursor.execute("SELECT username FROM users WHERE id=?", (follower[2],))
    print(cursor.fetchone()[0])
 

# Закрываем соединение с базой данных
conn.close()
 