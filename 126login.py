# coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from module import Mail

dr = webdriver.Chrome()
dr.get('http://www.126.com')
dr.implicitly_wait(2)

mail = Mail(dr)

mail.login('', 'password')
mail.login('username', '')
mail.login('error', 'error')

dr.quit()
