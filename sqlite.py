import sqlite3
connection=sqlite3.connect('student.db')

cursor=connection.cursor()
table_info='''CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARK INT)'''

cursor.execute(table_info)
cursor.execute('''INSERT INTO STUDENT VALUES('AMIT','SCIENCE','C','80')''')
cursor.execute('''INSERT INTO STUDENT VALUES('SAME','SCIENCE','A','93')''')
cursor.execute('''INSERT INTO STUDENT VALUES('HARI','SCIENCE','D','78')''')
cursor.execute('''INSERT INTO STUDENT VALUES('RAJA','SCIENCE','C','90')''')
cursor.execute('''INSERT INTO STUDENT VALUES('JOEL','SCIENCE','B','67')''')

print('The inserted record are:')
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()

