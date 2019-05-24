import  settings

import pymysql
import hashlib
import time

conn=pymysql.Connect(**settings.parameters)

cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)




while 1:
    username = input("请输入账号")
    usql = 'select username from user where username=%s'
    res1=cursor.execute(usql,[username])

    if res1>0:
        print('账号已存在请重新输入')
        continue
    if len(username)<=2 or username.isspace():
        print('账户名输入格式有误请重新输入')

    else:
        break




password=input("请输入密码")
password=hashlib.sha1(password.encode('utf-8')).hexdigest()
email=input('请输入你的邮箱')
rtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


sql="insert into user(username,password,email,rtime) values('%s','%s','%s','%s');"%(username,password,email,rtime)





try:
    res=cursor.execute(sql)
    if res>0:

        conn.commit()
    else:
        conn.rollback()
except Exception as e:
    print(e)
    conn.rollback()
    conn.close()
    cursor.close()
