
import requests
import sqlite3

def fn_get_trade_prcie(market):
    url =f"https://api.upbit.com/v1/ticker?markets={market}"
    res = requests.get(url)

    create_sql = """
        CREATE TABLE IF NOT EXISTS coin_price (
            seq integer primary key autoincrement,
            market TEXT,
            price real,
            collect_det datetime default current_timestamp
    )
    """

    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute(create_sql)
    price = res.json()[0]['trade_price']
    sql = "insert into coin_price (market, price) values(?, ?)"
    cur.execute(sql, [market, price])
    conn.commit()
    conn.close()

fn_get_trade_prcie("BTC-0G")