import sqlite3

from flask import jsonify

con = sqlite3.connect('demo.db')
cur = con.cursor();

cur.execute("""create table if not exists students(rollno int, name varchar(25))""");

con.commit();

con.close();