# 导入工具类
from util import MySqlUtil

# 获取连接
conn=MySqlUtil.get_conn()
# 获取游标
cur=conn.cursor()
try:
    # 定义sql语句
    username=input("请输入用户名：")
    password=input("请输入密码：")
    sql="insert into `user` values(%s,%s);"
    # 执行sql语句
    row=cur.execute(sql,[username,password])
    print("受影响的行数：",row)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    MySqlUtil.close(cur,conn)