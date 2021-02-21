# coding:utf-8

info = 'my name is %s,\amy age is %s'

name_01 = '小牧1'
age_01 = 10
name_02 = '这种1'
age_02 = 33
print(info % (name_01, age_01))
print(info % (name_02, age_02))

message = '您好，今天是%s,您的手机号码：%s 已经欠费了，请尽快充值'
print(message % ('星期一', 123456789))


info_3 = 'my name is {}, my age is {}'
print(info_3.format(name_02, age_02))