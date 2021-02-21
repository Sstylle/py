#coding:utf-8

manhua = []
history = []
code = []
empty = ()

new_manhua = ('a', 'b', 'c')
new_history = ('中国历史', '日本历史', '韩国历史')
new_code = ('python', 'django', 'flask')

manhua.extend(new_manhua)
history.extend(new_history)
code.extend(new_code)
empty.extend(new_code, new_manhua, new_history)

print(manhua, history, code, empty)