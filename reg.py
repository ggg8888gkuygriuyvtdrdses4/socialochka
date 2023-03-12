import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('social_network.py')
cursor = conn.cursor()

# Запрашиваем данные от пользователя
username = input("Введите логин: ")
password = input("Введите пароль: ")

# Проверяем, что такого пользователя еще нет в базе данных
cursor.execute("SELECT * FROM users WHERE username=?", (username,))
if cursor.fetchone() is not None:
    print("Пользователь с таким логином уже существует")
else:
    # Добавляем нового пользователя в базу данных
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print("Новый пользователь успешно зарегистрирован")