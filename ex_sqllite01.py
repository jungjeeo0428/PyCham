import sqlite3
conn = sqlite3.connect('mydb.db')

sql="""
    CREATE TABLE if not exists tb_coin (
        market varchar(20) primary key,
        kr_nm varchar(100),
        en_nm varchar(100)
    )
"""

cur =  conn.cursor()
cur.execute(sql)
cur.close()
conn.close()
