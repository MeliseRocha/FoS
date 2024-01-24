import sqlite3

from sqlite3 import Error

db_filename = "/home/enacom/FoS/db/database.db"
def create_database(db_file): 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print("ok")
    
    except Error as e:
        print(e)

    return conn
        
    
create_database(db_filename)

def create_table(conn, create_table_sql):
    try: 
        c = conn.cursor()
        c.execute(create_table_sql)
    
    except Error as e:
        print(e)


def sql_table():
    sql_create_user_table = "CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY, firstname text NOT NULL, lastname text NOT NULL);"
    
    sql_create_task_table =  "CREATE TABLE IF NOT EXISTS task (id integer PRIMARY KEY, name text, start_date text, end_date text, priority integer, user_id integer, FOREIGN KEY (user_id) REFERENCES user (id));"

    conn = create_database(db_filename)

    if conn is not None:

        print('creating')

        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_task_table)
    
    else:
        print("not today")

def create_user(conn, user):
    sql = "INSERT INTO user(firstname, lastname) VALUES(?, ?)"
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()
    return c.lastrowid


def create_task(conn, task):
    sql = "INSERT INTO task(name, start_date, end_date, priority, user_id) VALUES(?, ?, ?, ?, ?)"
    c = conn.cursor()
    c.execute(sql, user)
    conn.commit()
    return c.lastrowid

def insert_content():
    conn = create_database(db_filename)

    with conn:
        user = ('Mia','Meier')
        create_user(conn.user)

        task_1 = create_task("learn python", "24/01/2023", "25/01/2023", "2", user_id)

        create_task(conn.task_1)


    #sql_table()

    insert_content()