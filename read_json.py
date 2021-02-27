# coding:utf-8

import json

with open('./data_file/user_info.json', 'r') as f:
    data = f.read()


user_list = json.loads(data)
print(user_list)
print(user_list[1]['password'])
print(type(user_list[1]))
a = user_list[1]