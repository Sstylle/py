# coding:utf-8

# from selenium import webdriver

class BaiduPage():

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver

    def search_input(self, serch_key):
        self.driver.find_element_by_id('kw').send_keys(serch_key)

    def search_button(self):
        self.driver.find_element_by_id('su').click()
