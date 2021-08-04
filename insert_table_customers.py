import sqlite3
try:
    con=sqlite3.connect('p.db')
    cur=con.cursor()
    q1="""insert into customers values(1,'Akash',9874561230,'akash@gmail.com');"""
    q2="""insert into customers values(2,'Amit',9875642301,'amit@gmaiil.com');"""
    q3="""insert into customers values(3,'Anurag',9999999999,'anurag@gmail.com');"""
    q4="""insert into customers values(4,'Abhishek',9898989898,'abhishek@gmaiil.com');"""
    q5="""insert into customers values(5,'Sneha',9879879870,'sneha@gmaiil.com');"""
    q6="""insert into customers values(6,'Aman',9869869860,'aman@gmaiil.com');"""
    q7="""insert into customers values(7,'Ashutosh',9859859850,'ashutosh@gmaiil.com');"""
    q8="""insert into customers values(8,'Avinash',9849849840,'avinash@gmaiil.com');"""
    q9="""insert into customers values(9,'Mohini',9839839830,'mohini@gmaiil.com');"""
    q10="""insert into customers values(10,'Savita',8745895620,'savita@gmail.com');"""
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