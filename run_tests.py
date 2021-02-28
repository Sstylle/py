# coding:utf-8

import unittest
import time
from HTMLTestRunner import HTMLTestRunner
# from TestRunner import HTMLTestRunner

test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    fp = open('./test_report/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='这是描述啊', tester='苏少霖')
    # runner = unittest.TextTestRunner()
    runner.run(suits)
    fp.close()