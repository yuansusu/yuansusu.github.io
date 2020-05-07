#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import os
import json
import datetime
from flask import Flask, request

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

app = Flask(__name__)


@app.route('/index', methods=['POST'])
def indextest():
    inputData = request.json.get('inputData')
    data1 = getcontent(inputData)
    return data1

def getcontent(inputData):
    # 打开数据库连接
    conn = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8')

    # 使用cursor()方法获取操作游标
    cur = conn.cursor()

    sql = "select * from myorder where user_id='%s'"%(inputData)

    # 使用execute方法执行SQL语句
    cur.execute(sql)

    # 使用 fetchone() 方法获取一条数据
    data = cur.fetchone()

    print(data)
    result = {'order_id': data[0], 'user_id': data[1]}
    return json.dumps(result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5590)
