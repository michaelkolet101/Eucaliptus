

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="12345678",
                             database="Eucaliptus_database")

my_curser = db.cursor()

# my_curser.execute("CREATE DATABASE Eucaliptus_database")
# my_curser.execute("CREATE TABLE Springs (name VARCHAR(50), area VARCHAR(50), Latitude VARCHAR(50), longitude VARCHAR(50), load_level VARCHAR(50), spring_id int PRIMARY KEY AUTO_INCREMENT)")
# my_curser.execute("CREATE TABLE Person (name VARCHAR(50), age smallint, persone_id int PRIMARY KEY AUTO_INCREMENT)")

# create table for users
#
def add_data_Person(name: str, age: int):

    my_curser.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", (name, age))
    db.commit()

def add_data_springs(name: str, area: int, load_level:str, Latitude, longitude ):

    my_curser.execute("INSERT INTO springs (name, area, load_level, Latitude, longitude) VALUES (%s,%s,%s,%s,%s)", (name, area, load_level, Latitude, longitude))
    db.commit()


def update_amount(spring_name: str, count: str):

    msg = ""
    if count < 5:
        msg = "low"
    if count > 5 and count < 15:
        msg = "mid"
    if count >= 15:
        msg = "high"

    uodate = "UPDATE Springs SET load_level=%s WHERE Name=%s"
    my_curser.execute(uodate, (msg, spring_name))
    db.commit()


def fine_in_db(spring_name: str):
    my_curser.execute("SELECT * from Springs where  Name=%s", spring_name)
    db.commit()
    record = my_curser.fetchall()
    for item in record:
        return item[0], item[4]


# my_curser.execute("DROP TABLE Springs")
# db.commit()

my_d = {"name": "lavan",
        "area": "jrusalem",
        "load_level": "high",
        "Latitude": 0,
        "longitude": 0
        }

# add_data_springs(**my_d)
update_amount("lavan", 3)

my_curser.execute("SELECT * FROM Springs")

for itm in my_curser:
    print(itm)

fine_in_db('lavan')