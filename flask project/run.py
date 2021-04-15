# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("db/films_db.sqlite")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
cur.execute("""DELETE FROM films""").fetchall()

# Вывод результатов на экран

con.commit()
con.close()