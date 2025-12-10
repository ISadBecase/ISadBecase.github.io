from util import MySqlUtil
def login(username,password):
    """
        验证流程：
            1.验证账号，账号验证不通过，返回账号不存在
            2. 账号验证通过，验证密码，密码验证不通过，返回密码错误
            3. 返回登录成功
    """
    conn=MySqlUtil.get_conn()
    cur=conn.cursor()
    sql="select * from `user` where username=%s;"
    cur.execute(sql,[username])
    result=cur.fetchone()
    print(result)
    # 根据result的结果来判断，如果result为none，则账号不存在
    if result == None:
        MySqlUtil.close(cur,conn)
        return{
            "status":500,
            "msg":"账号不存在"
        }
    else:
        # 账号存在，验证密码
        if result[1]==password:
            # 密码正确
            MySqlUtil.close(cur,conn)
            return {
                "status":200,
                "msg":"登录成功"
            }
        else:
            # 密码错误
            MySqlUtil.close(cur,conn)
            return {
                "status":500,
                "msg":"密码错误"
            }

if __name__=='__main__':
    login("admin","111")