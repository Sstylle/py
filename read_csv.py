# coding:utf-8

import csv
import codecs
from itertools import islice


data = csv.reader(codecs.open('./data_file/user_info.csv', 'r', 'GBK'))

users = []

for line in islice(data, 1, None):
    users.append(line)

print(users)

users = []

with codecs.open('./data_file/user_info.csv', 'r', 'GBK') as f:
    f_csv = csv.reader(f)
    # next(f_csv)
    for r in f_csv:
        users.append(r)

print(users)