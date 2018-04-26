import sqlite3

conn = sqlite3.connect('students.db')

teilnehmer = {
    'Martin':     1976,
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':    1998,
    'Christoph':  1981,
    'RolandS':    1974,
}

for name, birth_year in teilnehmer.items():
    conn.execute("insert into student(name, birth_year) values (?,?)", (name, birth_year))
    
conn.commit()
