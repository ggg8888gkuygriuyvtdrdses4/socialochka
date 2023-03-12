import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Получаем список пользователей, на которых подписан текущий пользователь
cursor.execute("SELECT subscribe_user_id FROM subscriptions WHERE user_id=?", (user[0],))
subscribed_users = cursor.fetchall()

# Получаем посты всех пользователей, на которых подписан текущий пользователь
posts = []
for subscribed_user in subscribed_users:
    cursor.execute("SELECT * FROM posts WHERE user_id=?", (subscribed_user[0],))
    user_posts = cursor.fetchall()
    posts.extend(user_posts)

# Сортируем посты по дате создания в обратном порядке
posts.sort(key=lambda x: x[3], reverse=True)

# Выводим посты в ленту пользователя
for post in posts:
    print(f"{post[1]} ({post[2]}): {post[4]}")

# Закрываем соединение с базой данных
conn.close()