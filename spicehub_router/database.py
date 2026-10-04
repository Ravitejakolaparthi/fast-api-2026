import sqlite3
connection = sqlite3.connect("spicehub.db",check_same_thread=False)

cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE if not exists customers (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     active BOOLEAN
# )
# """)
# cursor.execute("""
# create table tables(
#     id integer primary key,
#     table_number integer,
#     capacity integer
# )
# """)
# cursor.execute("""
# insert into customers (name,active)
# values ('Ravi',TRUE)
# """)


# cursor.execute("""
# insert into customers (name,active) values
# ('Teja',TRUE),('Sai',FALSE)
# """)

# cursor.execute("""
#     update customers set active = FALSE
#     where id = 1
# """)
# cursor.execute("""
# delete from customers
# where id = 3""")
# cursor.execute("""
# select * from customers
# """)

# cursor.execute("""
# insert into tables (id,table_number,capacity) values (1,1,2),(2,2,4),(3,3,6)
# """)
# cursor.execute("drop table tables")
# connection.commit()
cursor.execute("""select * from tables""")
print(cursor.fetchall())