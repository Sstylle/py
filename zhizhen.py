def pass_by_cal(a):
    a.append(1)
    a.append(2)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c = a[:]
    c.append(5)
    pass_by_cal(a)
    print("{}\n{}\n{}".format(a, b, c))
