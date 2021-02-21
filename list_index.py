# coding:utf-8

numbers = [i for i in range(1, 11)]
print(numbers)
print(numbers[-3::-1])
print(numbers[2::-1])
numbers[3] = 9
print(numbers.index(9))