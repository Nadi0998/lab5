import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="1234",
    db="lab5",
    charset='utf8'
)

cursor = db.cursor()

# cursor.execute("INSERT INTO books (bookname, description) VALUES (%s, %s);", ('лол', 'кек'))
# db.commit()

cursor.execute("SELECT * FROM books;")

entries = cursor.fetchall()

for e in entries:
    print(e)

cursor.close()
db.close()
