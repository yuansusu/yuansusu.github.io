#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("10.10.10.10", "yuansusu", "11111112222222222222", "yuansusu_mysql", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = "select * from mydatabase where id=1"

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print data

# 关闭数据库连接
db.close()
