import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Получаем данные о пользователе по его логину
username = 'user123'
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
user = cursor.fetchone()

# Запрашиваем у пользователя фотографию и текст поста
photo_path = input("Введите путь к фотографии: ")
text = input("Введите текст поста: ")

# Добавляем пост в базу данных
cursor.execute("INSERT INTO posts (user_id, photo_path, text) VALUES (?, ?, ?)", (user[0], photo_path, text))
conn.commit()

# Закрываем соединение с базой данных
conn.close()