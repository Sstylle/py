# coding:utf-8

import unittest


class TestBdd(unittest.TestCase):

    def setUp(self) -> None:
        print('test TestBdd:')

    def test_ccc(self):
        print('test ccc')

    def test_aaa(self):
        print('test aaa')


class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        print('test TestAdd:')

    def test_bbb(self):
        print('test bbb')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests([TestBdd('test_aaa'), TestBdd('test_ccc')])
    # suite.addTest(TestBdd('test_ccc'))
    suite.addTest(TestAdd('test_bbb'))
    runner = unittest.TextTestRunner()
    runner.run(suite)