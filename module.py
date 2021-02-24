# coding:utf-8

from selenium.common.exceptions import NoSuchElementException


class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        #登录
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_css_selector('[id^=x-URS-iframe]'))
            self.driver.find_element_by_name('email').clear()
            self.driver.find_element_by_name('email').send_keys(username)
            self.driver.find_element_by_name('password').clear()
            self.driver.find_element_by_name('password').send_keys(password)
            self.driver.find_element_by_id('dologin').click()
            self.driver.switch_to.default_content()
        except NoSuchElementException as msg:
            self.driver.quit()
            print(msg)