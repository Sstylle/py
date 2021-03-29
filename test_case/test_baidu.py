# coding:utf-8

import unittest
from time import sleep
from selenium import webdriver
from common.baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):
    """123123123"""

    @classmethod
    def setUpClass(self) -> None:
        opt = webdriver.ChromeOptions()
        opt.add_argument('--headless')
        # opt.add_argument('--start-maximized')
        opt.add_argument('-window-size=1920x1080')
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(4)
        self.base_url = 'http://www.baidu.com'
        # print(self.driver.get_window_size())

    def test_search_key_selenium(self):
        # self.driver.get(self.base_url)
        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # self.driver.find_element_by_id('su').click()
        # sleep(2)
        # title = self.driver.title
        # self.assertEqual(title, 'selenium_百度搜索')
        search_key = 'selenium'
        # self.baidu_search(search_key)
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        sleep(1)
        bd.search_input(search_key)
        bd.search_button()
        sleep(1)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')



    def test_search_key_unittest(self):
        """试一下能不能看到注释"""
        # self.driver.get(self.base_url)
        # self.driver.find_element_by_id('kw').send_keys('unittest')
        # self.driver.find_element_by_id('su').click()
        # sleep(2)
        # title = self.driver.title
        # self.assertEqual(title, 'unittest_百度搜索')
        search_key = 'unittest'
        # self.baidu_search(search_key)
        # self.assertEqual(self.driver.title, search_key + '_百度搜索')
        bd = BaiduPage(self.driver)
        bd.search_input(search_key)
        bd.search_button()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
