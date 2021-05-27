import sqlite3

conn = sqlite3.connect('bdd.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS SCORES(id INT, score INT)")
cur.execute("INSERT INTO SCORES(id, score) VALUES(1, 300)")

conn.commit()

cur.close()
conn.close()