import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Sh@Rf1MSQL#234$",
    database="IMDB"
    )

cursor=conn.cursor(dictionary=True)
cursor.execute("select * from movies")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("select * from media")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("select * from genres order by genre_id")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("select * from movies, genres")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("SELECT m.movie_id, m.title, GROUP_CONCAT(g.genre_name ORDER BY g.genre_name) AS genres FROM movies m JOIN movie_genres mg ON m.movie_id = mg.movie_id JOIN genres g ON mg.genre_id = g.genre_id GROUP BY m.movie_id, m.title")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("SELECT a.artist_id, a.artist_name, s.skill_name FROM artists a JOIN artist_skills askl ON a.artist_id = askl.artist_id JOIN skills s ON askl.skill_id = s.skill_id ORDER BY a.artist_id, s.skill_name")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("SELECT r.review_id, r.movie_id, r.rating, r.review_text, r.review_date, u.user_id, u.username, u.email FROM reviews r JOIN users u ON r.user_id = u.user_id ORDER BY r.review_date DESC")
rows=cursor.fetchall()
print(rows)