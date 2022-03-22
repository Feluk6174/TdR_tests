import sqlite3

DB_FILE = "db/test.db"

def querry(command):
    global DB_FILE
    
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(command)

    r = cursor.fetchall()

    print(r)

    connection.close()

    return r


def create_tables():
    command = """CREATE TABLE users (
        id int,
        username varchar(32),
        public_key varchar(128),
        chain varchar(128));"""

    querry(command)

    command = """CREATE TABLE posts (id int, username varchar(32), content varchar(512), chain varchar(128));"""

    querry(command)


def print_users():
    command = """SELECT * FROM users"""

    print(querry(command))

def add_user():
    sql = "SELECT * FROM Table_Name ORDER BY id DESC LIMIT 1; "
    

#querry('INSERT INTO users VALUES (0, "temp", "cosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosescosacosa", "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");')
print_users()
