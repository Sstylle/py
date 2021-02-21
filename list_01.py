#coding:utf-8

names = ['dewei', 'xiaomu','xiaowang']

names_add = names +names
# name_c = names * 10

# print(names_add)
# print(name_c)
# print('name_c length is', len(name_c))

names += names
print(names)
print(names)

book = []
print(id(book))
book.append('abc')
print(book)
print(id(book))
book.append(bool(1))
print(book)
print(id(book))

fruits = ['苹果', '西瓜', '水蜜桃', '西瓜', '香蕉']
print(fruits.count('西瓜'))