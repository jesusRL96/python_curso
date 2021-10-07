import sqlite3

class Person:
    def __init__(self, pk=-1, first="", last="", age=-1):
        self.pk = pk
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect("mydata.db")
        self.cursor = self.connection.cursor()
    def load_person(self, pk):
        self.cursor.execute("""
            SELECT * FROM people WHERE id == {}
            """.format(pk))
        results = self.cursor.fetchone()
        self.pk = pk
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO people VALUES({},'{}','{}','{}')""".format(self.pk,self.first,self.last,self.age))
        self.connection.commit()



# p1 = Person(30,'pepe','pecas',100 )
# p1.insert_person()

p2 = Person()
p2.load_person(30)
print(p2.first, p2.last, p2.age)



# connection = sqlite3.connect("mydata.db")
# cursor = connection.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS people (
#     id INTEGER PRIMARY KEY,
#     first_name VARCHAR(32),
#     last_name TEXT,
#     age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO people VALUES(1,'jesus', 'Ramirez', 23),(2,'juan', 'perez', 21);
# """)

# cursor.execute("""
# SELECT * FROM people
# """)
# rows = cursor.fetchall()
# print(rows)
# connection.commit()
# connection.close()