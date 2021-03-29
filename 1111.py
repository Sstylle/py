#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 登录页面的自动化测试
# import sys
# import importlib
# reload(sys)
# sys.setdefaultencoding("utf-8")
from selenium import webdriver
import unittest
from time import sleep

# importlib.reload(sys)


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        # 设置网页加载时间
        self.driver.implicitly_wait(5)
        # 定义url(setUP创建时首次执行的url）
        self.url = 'https://mvimapp.test.iauto360.cn/#/login'

    def test_login(self):
        # 发起请求
        self.driver.get(self.url)
        # 定位两个输入框的列表
        inputspace = self.driver.find_elements_by_css_selector('.van-field__control')
        # 输入用户名
        inputspace[0].send_keys('mhc123')
        # 输入密码
        inputspace[1].send_keys('sxcg@201')
        # 点击登录按钮
        self.driver.find_element_by_css_selector('.btn').click()
        if self.driver.find_elements_by_css_selector('.van-tabbar-item__text'):
            print('登录成功')
        else:
            # 设置网页加载时间
            # self.driver.implicitly_wait(15)
            sleep(3)
            # 获取页面错误信息
            text = self.driver.find_element_by_xpath('/html/body/div[2]/div').get_attribute('textContent')
            # text = self.driver.find_element_by_css_selector('.van-toast__text').get_attribute('textContent')
            print(text, "11111")
        # 结束请求

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
