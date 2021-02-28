# coding:utf-8

import unittest


class MyTest(unittest.TestCase):

    @unittest.skip('直接跳过')
    def test_skip(self):
        print('test aaa')

    @unittest.skipIf(3 > 2,'当条件为真时跳过')
    def test_skip_if(self):
        print('test bbb')

    def test_skip_ifs(self):
        print('test eee')

    @unittest.skipUnless(3 > 2, '当条件为真时执行')
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure
    def test_expected_failure(self):
        print('test ddd')
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()