import pymysql

import settings

conn=pymysql.Connect(**settings.parameters)

cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)


sql="create table user(uid int(10) primary key auto_increment,username varchar(255) unique,usertype  enum('普通用户','管理员') default '普通用户',password varchar(255),retime datetime(6),email varchar(50))"

res=cursor.execute(sql)

if res>0:
    print("创建成功")
else:
    print('创建失败')

cursor.close()

conn.close()