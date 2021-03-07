# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


subject = 'Python email test'

msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login('13425457347@163.com', 'SSTQDRCILQUPBDQB')
smtp.sendmail('13425457347@163.com', '786697810@qq.com', msg.as_string())
smtp.quit()
