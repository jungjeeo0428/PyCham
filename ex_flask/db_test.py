import pymysql
import pymysql.cursors
DB_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'member_db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
def get_member():
    member_all = ()
    try:
        conn = pymysql.connect(**DB_config)
        print("success")
        with conn.cursor() as cursor:
            cursor.execute('select * from member')
            member_all = cursor.fetchall()
            print(f"조화된 회원수{len(member_all)}")
            for m in member_all:
                print(f"{m['mem_name']}: {m['mem_mail']}")
    except Exception as e:
        print("Error")
    return member_all

