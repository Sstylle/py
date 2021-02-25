# coding:utf-8

with(open("./data_file/user_info.txt", "r")) as user_file:
    data = user_file.readlines()

users = []
for line in data:
    # print(line[:-1])
    user = line[:-1].split(":")
    users.append(user)

print(users)