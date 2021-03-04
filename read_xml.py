# coding:utf-8

from xml.dom.minidom import parse
# import sys
# print(sys.path)

dom = parse('./data_file/config.xml')
root = dom.documentElement

tag_name = root.getElementsByTagName('platform')

for item in tag_name:
    print(item.firstChild.data)

login_info = root.getElementsByTagName('login')
usernames, passwords = [], []
for item in login_info:
    usernames.append(item.getAttribute('username'))
    passwords.append(item.getAttribute('password'))

for username in usernames:
    print(username, passwords[usernames.index(username)])