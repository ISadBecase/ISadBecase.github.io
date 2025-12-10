# 导入pymysql包
import pymysql
# 通过pymysql的connect函数，获取连接对象
"""
    connect函数：
        通过数据库的连接信息，返回一个数据库连接对象
        参数：
            1.host：连接数据库服务器所在的ip地址，127.0.0.1
            2.port:连接数据库服务器启动的端口号：3306
            3.user:连接数据库服务器的账号，root
            4.password:数据库服务器账号对应的密码，就是root账号对应的密码
            5.database:连接数据库服务器之后想要操作数据库的名字
            6.charset:字符集，utf8
"""
conn=pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="anziwen777",
    database="users",
    charset="utf8"
)
# print(conn)
# 通过连接对象调用方法cursor()，得到一个游标对象
"""
    cursor()方法：
        作用：用来获取操作数据库的对象，这个对象称为游标对象
        参数:没有参数
"""
cur=conn.cursor()
# 定义操作数据库的sql语句
sql="SELECT * FROM `user`;"
# 通过游标对象调用方法execute(参数1，参数2)执行sql语句
"""
    execute方法：
        非批量操作，执行一条sql语句，返回值是影响数据的行数
        参数：
            1. sql语句
            2. 为sql语句中的占位符赋值，赋值是数据类型必须是字典or元组or列表
    executemany方法：
        需要批量操作的数据选择这个方法，返回值是影响数据的行数
        参数：
            1. sql语句
            2. 批量操作的数据
"""
row=cur.execute(sql)
print("影响数据的行数为：",row)
# 通过游标对象.fetchall()方法获取查询的结果
"""
    fetchall方法：
        返回执行sql语句的查询结果
        至于执行的sql语句是查询命令时，才可以用这个方法来获取结果，增删改操作不能用
"""
result=cur.fetchall()
print("查询结果为：",result)