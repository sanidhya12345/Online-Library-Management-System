import sqlite3
try:
    con=sqlite3.connect('p.db')
    create="create table maintain(cno integer,bcode integer,cname text,issuedate date,E_returndate date,R_returndate date,fine integer,foreign key(cno) references customers,foreign key(bcode) references stock)"
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