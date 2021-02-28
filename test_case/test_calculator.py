# coding:utf-8

import unittest
from test_case.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        print('test start:')

    def tearDown(self) -> None:
        print('test end')

    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        # assert result == 8, '加法运算失败！'
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(7, 2)
        result = c.sub()
        # assert result == 5, '减法运算失败！'
        self.assertEqual(result, 5)

    def test_mul(self):
        c = Calculator(3, 3)
        result = c.mul()
        # assert result == 10, '乘法运算失败！'
        self.assertEqual(result, 10)

    def test_div(self):
        c = Calculator(6, 2)
        result = c.div()
        # assert result == 3, '除法运算失败！'
        self.assertEqual(result, 3)

    def test_equal(self):
        self.assertEqual(2+2, 4)
        self.assertEqual('python', 'python')
        self.assertNotEqual('hello', 'python')

    def test_in(self):
        self.assertIn('hello', 'hello world')
        self.assertNotIn('hi', 'hello')

    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(False)


class TestAdd(unittest.TestCase):

    def test_add_integer(self):
        c = Calculator(3, 5)
        self.assertEqual(c.add(), 8)

    def test_add_decimals(self):
        c = Calculator(3.2, 5.5)
        self.assertEqual(c.add(), 8)

    def test_add_string(self):
        c = Calculator('7', '9')
        self.assertEqual(c.add(), 16)


class TestSub(unittest.TestCase):
    pass


if __name__ == '__main__':
    # test_add()
    # test_div()
    # test_mul()
    # test_sub()
    unittest.main(TestCalculator())
    # suit = unittest.TestSuite()
    # suit.addTest(TestCalculator('test_add'))
    # suit.addTest(TestCalculator('test_div'))
    # suit.addTest(TestCalculator('test_mul'))
    # suit.addTest(TestCalculator('test_sub'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
