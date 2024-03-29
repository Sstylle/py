# coding:utf-8

import time
from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def open(self, url=None):
        if url is None:
            print(self.url)
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_title(self):
        return self.driver.title

    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    def js(self, script):
        self.driver.execute_script(script)


# if __name__ == '__main__':
#     a = BasePage(1)
#     a.open()
