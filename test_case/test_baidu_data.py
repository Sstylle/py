# coding:utf-8

import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        opt = webdriver.ChromeOptions()
        opt.add_argument('--headless')
        opt.add_argument('-windows-size=1920x1080')
        cls.driver = webdriver.Chrome(options=opt)
        cls.base_url = 'https://www.baidu.com'
        cls.test_data = []
        with codecs.open(report_path, 'r', 'GBK') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.test_data.append(line)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    # def test_search(self):
    #     with codecs.open('../data_file/baidu_data.csv', 'r', 'GBK') as f:
    #         data = csv.reader(f)
    #         for line in islice(data, 1, None):
    #             search_key = line[1]
    #             self.baidu_search(search_key)

    def test_search_selenium(self):
        self.baidu_search(self.test_data[0][1])

    def test_search_unittest(self):
        self.baidu_search(self.test_data[1][1])

    def test_search_parameterized(self):
        self.baidu_search(self.test_data[2][1])


report_path = './data_file/baidu_data.csv'

if __name__ == '__main__':
    report_path = '../data_file/baidu_data.csv'
    unittest.main(verbosity=2)
