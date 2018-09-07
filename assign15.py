import sqlite3
def create_table():
    c.execute('CREATE TABLE student(name TEXT,marks REAL)')
def dynamicDataEntry():
    name=input("enter name->")
    marks=input("enter marks->")
    c.execute('INSERT INTO student(name,marks) VALUES(?,?)',(name,marks))
    conn.commit()
def read_from_db():
    c.execute('SELECT * FROM student WHERE marks>=80')
    for row in c.fetchall():
        print("Name:",row[0])
try:
    conn=sqlite3.connect('test.db')
    c=conn.cursor()
    create_table()
    for i in range(3):
        dynamicDataEntry()
    print("-"*50)
    read_from_db()
except Exception as e:
    print(e)
finally:
    c.close()
    conn.close()
