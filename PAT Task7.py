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
cursor.execute("select * from movies, genres")
rows=cursor.fetchall()
print(rows)

cursor=conn.cursor(dictionary=True)
cursor.execute("select * from artists, skills, roles")
rows=cursor.fetchall()
print(rows)