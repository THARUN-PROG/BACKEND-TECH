import sqlite3
from unicodedata import name

con=sqlite3.connect('demo.db',check_same_thread=False);

cur= con.cursor()

def getAll():
    cur=con.cursor();
    cur.execute("Select * from students");
    data=cur.fetchall();
    con.commit();
    return(data);

def Insert(data):
    print("__data__")
    cur=con.cursor();
   
    if type(data)==list:
        cur.executemany(f'insert into students value(:id,:name,:department)', data);
    else:
        cur.execute (f'insert into students values("{data["rollno"]}","{data["name"]}")');
    con.commit();

def deletestu(id):
    cur=con.cursor();
    cur.execute (f'delete from students where rollno = "{id}"');
    con.commit();

def upd(data):
    cur=con.cursor();
    cur.execute(f'update students set name = "{data["name"]}" where rollno ="{data["rollno"]}" ');
    con.commit();


