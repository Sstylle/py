# coding:utf-8

from common.baidu_page_poium import BaiduPage
import unittest
from time import sleep
from selenium import webdriver


class TestBaidu(unittest.TestCase):
    """123123123"""

    @classmethod
    def setUpClass(cls) -> None:
        opt = webdriver.ChromeOptions()
        # opt.add_argument('--headless')
        # opt.add_argument('--start-maximized')
        opt.add_argument('-window-size=1920x1080')
        cls.driver = webdriver.Chrome(options=opt)
        # cls.driver.implicitly_wait(5)
        cls.base_url = 'http://www.baidu.com'
        # print(self.driver.get_window_size())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.get('http://www.baidu.com')
        page.search_input = 'selenium'
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title, 'selenium_百度搜索')


if __name__ == '__main__':
    unittest.main()