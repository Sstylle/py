# coding:utf-8

import yagmail

yag = yagmail.SMTP(user='13425457347@163.com', password='SSTQDRCILQUPBDQB',
                   host='smtp.163.com')

contents = ['冲啊！']

yag.send(to='786697810@qq.com', subject='test yagmail', contents=contents)
yag.send('786697810@qq.com', '测试附件', contents, ['./test_report/result.html'])