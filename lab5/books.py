from lab5.connect import Connection


class Book:
    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        cur = self.db_connection.cursor()
        cur.execute("INSERT INTO books (bookname, description) VALUES (%s, %s);", (self.name, self.description))
        self.db_connection.commit()
        cur.close()


con = Connection("dbuser", "1234", "lab5")

with con:
    book = Book(con, 'electronic', 'especially for electroded')
    book.save()

