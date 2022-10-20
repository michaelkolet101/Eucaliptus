

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="12345678",
                             database="testdatabase")

my_curser = db.cursor()

def add_data_Person(name: str, age: int):

    my_curser.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", (name, age))
    db.commit()

def add_data_springs(name: str, area: int, load_level:str, Latitude, longitude ):

    my_curser.execute("INSERT INTO springs (name, area, load_level, Latitude, longitude) VALUES (%s,%s,%s,%s,%s)", (name, area, load_level, Latitude, longitude))
    db.commit()
#
# my_curser.execute("DROP TABLE Springs")
# db.commit()
#my_curser.execute("CREATE TABLE Person (name VARCHAR(50), age smallint, persone_id int PRIMARY KEY AUTO_INCREMENT)")
# my_curser.execute("CREATE TABLE Springs (name VARCHAR(50), area VARCHAR(50), Latitude VARCHAR(50), longitude VARCHAR(50), load_level VARCHAR(50), spring_id int PRIMARY KEY AUTO_INCREMENT)")

my_d = {"name": "lavan",
        "area": "jrusalem",
        "load_level": "high",
        "Latitude": 0,
        "longitude": 0
        }

add_data_springs(**my_d)


my_curser.execute("SELECT * FROM Springs")

for itm in my_curser:
    print(itm)
