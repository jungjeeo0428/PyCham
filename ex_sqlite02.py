import sqlite3
conn = sqlite3.connect("mydb.db")
sql = """
    insert into tb_coin values(?, ?, ?)
"""
data = {"market":"test2", "kr":"test2","en":"test2"}
sql2 = """ insert into tb_coin values(:market, :kr, :en)"""
cur = conn.cursor()
cur.execute(sql2, data)
conn.commit()
conn.commit()
conn.close()
