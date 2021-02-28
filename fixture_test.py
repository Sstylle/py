# coding:utf-8

import unittest


def setUpModule():
    print("test module start >>>>>>>>")


def tearDownModule():
    print("test module end >>>>>>>>")


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('test class start =====>')

    @classmethod
    def tearDownClass(cls) -> None:
        print('test class end =====>')

    def setUp(self) -> None:
        print('test case start -->')

    def tearDown(self) -> None:
        print('test case end -->')

    def test_case1(self):
        print('test case1')

    def test_case2(self):
        print('test case2')


class Test(unittest.TestCase):

    def test_case3(self):
        print('333')


if __name__ == '__main__':
    unittest.main()