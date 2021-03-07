# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


subject = 'Python send email test'

with open('./test_report/result.html', 'rb') as f:
    send_att = f.read()

att = MIMEText(send_att, 'text', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename="result.html"'

msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login('13425457347@163.com', 'SSTQDRCILQUPBDQB')
smtp.sendmail('13425457347@163.com', '13425457347@163.com', msg.as_string())
smtp.quit()