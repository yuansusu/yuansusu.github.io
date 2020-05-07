#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = "select * from myorder where user_id='470001902'"

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print(data)
# 关闭数据库连接
db.close()
