import  settings

import pymysql
import hashlib

conn=pymysql.Connect(**settings.parameters)

cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
while 1:
    username = input("请输入用户名")
    password = input('请输入密码')
    password=hashlib.sha1(password.encode('utf-8')).hexdigest()
    sql='select username from user where username=%s and password=%s;'

    res=cursor.execute(sql,[username,password])
    if  res > 0:
        print('登录成功')
        break

    else:
        print('登录失败,账户名或密码错误')
    continue



conn.close()
cursor.close()