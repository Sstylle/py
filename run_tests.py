# coding:utf-8

import unittest
import time
import yagmail
from HTMLTestRunner import HTMLTestRunner
# from TestRunner import HTMLTestRunner


def send_mail(report):
    yag = yagmail.SMTP(
        user='13425457347@163.com',
        password='SSTQDRCILQUPBDQB',
        host='smtp.163.com'
    )
    subject = '主题，自动化测试报告'
    content = '正文，请查看附件'
    yag.send('786697810@qq.com', subject, content, report)
    print('email has send out !')

test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    html_report = './test_report/' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='这是描述啊', tester='苏少霖')
    # runner = unittest.TextTestRunner()
    runner.run(suits)
    fp.close()
    send_mail(html_report)