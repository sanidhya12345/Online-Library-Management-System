import sqlite3
try:
    con=sqlite3.connect('p.db')
    create="create table stock(bcode integer primary key,bname text,tb integer,ab integer);"
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