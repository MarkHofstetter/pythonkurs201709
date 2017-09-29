import sqlite3

conn = sqlite3.connect('test.db')

'''
mysql

import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
'''

# ab hier ist es bei allen Datenbanken gleich

teilnehmer = {
    'Martin':     {'year': 1976, 'height': 180, 'education': ['VS', 'Gym', 'Uni']},
    'Harald':     1970,
    'Gerald':     1973,
    'RolandW':     1998,
    'Christoph':  1981,
    'RolandS':     1974,
}

'''
id = 10
for name in teilnehmer:
    conn.execute("insert into namen(id, name) values (?,?)", (id, name))
    id += 1
    
conn.commit()
'''
# cursor = conn.execute("select id, name from namen where name = ?", ('Mark',))
cursor = conn.execute("select id, name from namen")
for row in cursor:
    print(row)
    
conn.close()    