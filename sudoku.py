# coding:utf-8

from random import randint
from time import perf_counter

start = perf_counter()
sudo, hole = [[0 for i in range(9)] for i in range(9)], [[0 for i in range(9)] for i in range(9)]


# print(sudo)
# print(hole)

def set(x, y, val):
    if sudo[y][x] != 0:
        return False
    for x0 in range(9):
        if sudo[y][x0] == val:
            return False
    for y0 in range(9):
        if sudo[y0][x] == val:
            return False
    for y0 in range(int(y / 3) * 3, int(y / 3) * 3 + 3):
        for x0 in range(int(x / 3) * 3, int(x / 3) * 3 + 3):
            if sudo[y0][x0] == val:
                return False
    sudo[y][x] = val
    return True


def reset(x, y):
    sudo[y][x] = 0


def initXOrd(xord):
    for i in range(9):
        xord[i] = i
    for i in range(9):
        k = randint(1, 100) % 9
        xord[i], xord[k] = xord[k], xord[i]


def fillFrom(y, val):
    xord = [0 for i in range(9)]
    initXOrd(xord)
    for i in range(9):
        x = xord[i]
        if set(x, y, val):
            if y == 8:
                if val == 9 or fillFrom(0, val + 1):
                    return True
            else:
                if fillFrom(y + 1, val):
                    return True
            reset(x, y)
    return False


def digHole(holecount):
    idx = [i for i in range(81)]
    for i in range(holecount):
        k = randint(0, 80)
        idx[i], idx[k] = idx[k], idx[i]
    for i in range(holecount):
        hole[int(idx[i] / 9)][int(idx[i] % 9)] = 1


def printSudo():
    for y in range(9):
        print('\n-------------------------------\n|' if y % 3 == 0 else ' \n|', end=' ')
        for x in range(9):
            print(sudo[y][x] if hole[y][x] else ' ', end=' ')
            print('|' if x % 3 == 2 else '', end=' ')
    print('\n-------------------------------\n')


if __name__ == '__main__':
    while not fillFrom(0, 1):
        pass
    digHole(35)
    printSudo()
    print('运行耗时：', perf_counter() - start)
