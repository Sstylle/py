# coding:utf-8

import yagmail

yag = yagmail.SMTP(user='13425457347@163.com', password='SSTQDRCILQUPBDQB',
                   host='smtp.163.com')

contents = ['冲啊！']

yag.send('786697810@qq.com', 'test yagmail', contents)
yag.send('786697810@qq.com', '测试附件', contents, ['./test_report/result.html'])