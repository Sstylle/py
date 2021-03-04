# coding:utf-8

import yaml


with open('./data_file/ddt_data_file.yaml', 'r') as f:
    data = yaml.load(f)
    print(type(data))
    print(data)
    print(data['one'][0]['search_key'])