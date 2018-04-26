import sqlite3

conn = sqlite3.connect('students.db')

user_name = input('name: ')
birth_year =  input('birth year: ')

sql = 'SELECT * FROM student WHERE name ="' + user_name + '" AND birth_year ="' + birth_year + '"'

cursor = conn.execute(sql)
for row in cursor:
    print(row)
    
conn.close()
 