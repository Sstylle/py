# coding:utf-8

import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack
import csv
import codecs

data_path = '../data_file/baidu_data.csv'

def getCsvDate(path):
    value = []
    with codecs.open(path, 'r', 'GBK')as f:
        data = csv.reader(f)
        next(data)
        for i in data:
            value.append(i)
        print(value)
        return value


@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        opt = webdriver.ChromeOptions()
        opt.add_argument('--headless')
        opt.add_argument('-windows-size=1920x1080')
        cls.driver = webdriver.Chrome(options=opt)
        cls.base_url = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    # @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    # @unpack
    # def test_search1(self, case, search_key):
    #     print('第一组测试用例：', case)
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')
    #
    # @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    # @unpack
    # def test_search2(self, case, search_key):
    #     print('第二组测试用例：', case)
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')
    #
    # @data({"search_key": "selenium"}, {"search_key": "ddt"}, {"search_key": "python"})
    # @unpack
    # def test_search3(self, search_key):
    #     print('第三组测试用例：', search_key)
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')
    #
    # @file_data('../data_file/ddt_data_file.json')
    # def test_search4(self, search_key):
    #     print('第四组测试用例：', search_key)
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')

    # @file_data('../data_file/ddt_data_file.yaml')
    # def test_search5(self, case):
    #     print(case)
    #     search_key = case[0]['search_key']
    #     print('第五组测试用例：', search_key)
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @data(*getCsvDate(data_path))
    @unpack
    def test_search5(self, name, search_keys):
        search_key = search_keys
        print('第五组测试用例：', search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')


if __name__ == '__main__':
    data_path = './data_file/baidu_data.csv'
    unittest.main(verbosity=2)
    '''问问别人'''