import sqlite3

# izveido datu baze un japiesledzas tai
conn=sqlite3.connect('piemers.db')
cursor=conn.cursor()

#tabula
cursor.execute('''
               CREATE TABLE IF NOT EXISTS lietotaji(
                    id INTEGER PRIMARY KEY,
                    vards TEXT NOT NULL,
                    uzvards TEXT NOT NULL,
                    epasts TEXT NOT NULL UNIQUE
               )
               ''')












conn.comit()
conn.close()