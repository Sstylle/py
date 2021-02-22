# coding: utf-8

# import sys
# from os.path import abspath, dirname
#
# project_path = dirname(abspath(__file__))
# sys.path.append(project_path + "\\module")
# # print(sys.path)
#
# if __name__ == '__main__':
#     print(sys.path, end='\n')

def sayhello(name=None):
    if name is None:
        raise NameError('"Name" cannot be empty')
    else:
        print("hello, {}".format(name))


if __name__ == '__main__':
    try:
        open("abc.txt", 'r')
    except FileNotFoundError:
        print('找不到文件！')
    except Exception:
        print('123')
    else:
        print('1')

    try:
        print('1')
    except Exception as msg:
        print(msg)
    except NameError:
        print('没有这个变量!')
    else:
        print('1')
    sayhello('Tom')