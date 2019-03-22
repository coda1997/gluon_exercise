import pymysql

db = pymysql.connect("localhost", "root", "fv#!EgpkcTZbw#RzDN4M75ff", "smartkeep", charset="utf8")
cursor = db.cursor()

sql = 'INSERT INTO elbow(q0,q1,q2,q3,locs) VALUES (%s,%s,%s,%s,%s);'

data = [
    (0.01, 0.001, 0.01, 0.001, '[1,2,3]'),
    (0.02, 0.001, 0.01, 0.001, '[1,2,3]')
]

cursor.executemany(sql, data)
db.commit()

db.close()
