#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

url = "http://baidu.com/admin/login"

payload = "{\"user_name\":\"ysh\",\"passwd\":\"b95495d2b655e0cd832244427261b76a\",\"tn_r\":null}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
