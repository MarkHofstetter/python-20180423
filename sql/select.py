import sqlite3

conn = sqlite3.connect('students.db')

user_name = input('name: ')
birth_year =  input('birth year: ')

# asd" or 1 --
'''
sql = 'SELECT * FROM student WHERE name ="' + user_name + \
     '" AND birth_year ="' + birth_year + '"'
cursor = conn.execute(sql)
'''
cursor = conn.execute(
'SELECT * FROM student WHERE name = ? AND birth_year = ?', (user_name, birth_year))
     
     

for row in cursor:
    print(row)
    
conn.close()
