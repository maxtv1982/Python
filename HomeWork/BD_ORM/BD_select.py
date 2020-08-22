import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:******@localhost:5432/BD_musician')
# посмотрим, какие таблицы есть
# pprint(engine.table_names())
# установим соединение
connection = engine.connect()

print(' название и год выхода альбомов, вышедших в 2018 году ')
info1 = connection.execute("SELECT title, date FROM album WHERE EXTRACT(year FROM date) = 2018;").fetchall()
pprint(info1)

print(' название и продолжительность самого длительного трека ')
# info2 = connection.execute("SELECT title, duration FROM track ORDER BY duration DESC;").fetchone()
info2 = connection.execute("SELECT title, duration FROM track "
                           "WHERE duration = (SELECT MAX(duration) FROM track);").fetchall()
pprint(info2)

print(' название треков, продолжительность которых не менее 3,5 минуты ')
info3 = connection.execute("SELECT title, duration FROM track WHERE duration >= '3:5';").fetchall()
pprint(info3)

print(' названия сборников, вышедших в период с 2018 по 2020 год включительно ')
info4 = connection.execute("SELECT name FROM collection WHERE EXTRACT(year FROM year) "
                           "BETWEEN '2018' AND '2020';").fetchall()
pprint(info4)

print(' исполнители, чье имя состоит из 1 слова ')
info5 = connection.execute("SELECT name FROM musician "
                           "WHERE (length(name) - length(replace(name, ' ', ''))) = 0;").fetchall()
pprint(info5)

print(' название треков, которые содержат слово "Мой"/"Ты" ')
info6 = connection.execute("SELECT title FROM track WHERE title LIKE ANY (array['%%Мой%%', '%%Ты%%']);").fetchall()
pprint(info6)

