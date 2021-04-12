# coding:utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep


def login(dr):
    dr.find_element_by_id('username').clear()
    dr.find_element_by_id('username').send_keys('maodayuan')
    dr.find_element_by_id('password').clear()
    dr.find_element_by_id('password').send_keys('Mdy4090@')
    dr.find_element_by_class_name('ant-btn').click()

dr = webdriver.Chrome()

dr.get('http://new.nezha-test.compass.ym/')
dr.maximize_window()
sleep(2)
# button = dr.find_element_by_css_selector('.form-inline-input > div > span')
# print(button)
#
# action = ActionChains(dr)
# action.click_and_hold(button).perform()
#
# for index in range(318):
#     try:
#         action.move_by_offset(50, 0).perform()
#     except:
#         break
#     action.reset_actions()
#     sleep(0.1)
login(dr)
sleep(1)
dr.find_element_by_css_selector(".anticon-api").click()
handle = dr.window_handles[1]
dr.switch_to.window(handle)
sleep(3)
p = dr.find_element_by_xpath('//span[text()="CPU"]')
p.click()
sleep(1)
# f = dr.find_elements_by_css_selector('.actionBox___3N6aR')
print(dr.find_elements_by_css_selector('[class^=actionBox]')[1].get_attribute('style'))


dr.execute_script('document.querySelectorAll("[class^=actionBox]")[1].style="display:block;"')
print(p)
print(dr.find_elements_by_css_selector('[class^=actionBox]')[1].get_attribute('style'))
dr.find_elements_by_css_selector('[class^=actionBox] > img:nth-child(1)')[1].click()

sleep(5)
# dr.quit()
