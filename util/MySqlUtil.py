# 导入pymysql包
import pymysql
def get_conn():
    return pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="anziwen777",
        database="users",
        charset="utf8"
    )
def close(cur,conn):
    cur.close()
    conn.close()
