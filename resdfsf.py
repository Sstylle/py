# coding:utf-8

import codecs
import csv

data_path = './data_file/baidu_data.csv'

def getCsvDate():
    value = []
    with codecs.open(data_path, 'r', 'GBK')as f:
        data = csv.reader(f)
        next(data)
        for i in data:
            value.append(i)
        print(value)
        return value

if __name__ == '__main__':
    getCsvDate()
    data_path = '../data_file/baidu_data.csv'
    getCsvDate()
