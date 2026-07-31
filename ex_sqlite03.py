import requests
import sqlite3
import json
url = "https://api.upbit.com/v1/market/all"
res = requests.get(url)

print(res.json())
conn = sqlite3.connect('mydb.db')
try:
    cur = conn.cursor()
    sql = "insert into tb_coin values(:market, :korean_name, :english_name)"
    for row in res.json():
        cur.execute(sql, row)
    conn.commit()
except Exception as e:
    conn.rollback()

cur.close()
conn.close()

