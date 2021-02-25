# coding:utf-8

import csv
import codecs
from itertools import islice


data = csv.reader(codecs.open('./data_file/user_info.csv', 'r', 'GBK'))

users = []

for line in islice(data, 1, None):
    users.append(line)

print(users)