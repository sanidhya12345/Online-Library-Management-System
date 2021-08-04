import sqlite3
try:
    con=sqlite3.connect('p.db')
    create="create table customers(cno integer primary key,cname varchar2(20),phone integer not null, email varchar2(20) not null);"
    con.execute(create)
    print("table created successfully")
    con.commit()
    con.close()
except sqlite3.Error as error:
    print("Error occurred is",error)
finally:
    if(con):
        con.close()
        print("connection closed")