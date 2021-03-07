# coding:utf-8

from selenium import webdriver
from common.base import BasePage


class BaiduPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome()
    url = 'https://www.baidu.com'

    # def __init__(self, driver):
    #     self.driver = driver

    def search_input(self, serch_key):
        # self.driver.find_element_by_id('kw').send_keys(serch_key)
        self.by_id('kw').send_keys(serch_key)

    def search_button(self):
        # self.driver.find_element_by_id('su').click()
        self.by_id('su').click()