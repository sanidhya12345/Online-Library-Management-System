import sqlite3
try:
    con=sqlite3.connect('p.db')
    cur=con.cursor()
    q1="""insert into stock values(001,'ENGLISH',10,10);"""
    q2="""insert into stock values(002,'HINDI',20,20);"""
    q3="""insert into stock values(003,'PHYSICS',15,15);"""
    q4="""insert into stock values(004,'BIOLOGY',25,25);"""
    q5="""insert into stock values(005,'CHEMISTRY',10,10);"""
    q6="""insert into stock values(006,'MATH',15,15);"""
    q7="""insert into stock values(007,'SCIENCE',20,20);"""
    q8="""insert into stock values(008,'SST',10,10);"""
    q9="""insert into stock values(009,'ART',50,50);"""
    q10="""insert into stock values(010,'GK',40,40);"""
    cur.execute(q1)
    cur.execute(q2)
    cur.execute(q3)
    cur.execute(q4)
    cur.execute(q5)
    cur.execute(q6)
    cur.execute(q7)
    cur.execute(q8)
    cur.execute(q9)
    cur.execute(q10)
    con.commit()
    cur.close()
except sqlite3.Error as error:
    print("Error occurred is",error)
finally:
    if(con):
        con.close()
        print("connection closed")