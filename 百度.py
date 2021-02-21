from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.maximize_window()
ActionChains(dr).move_to_element(dr.find_element_by_css_selector('#s-usersetting-top')).perform()
xialakuang = dr.find_element_by_css_selector('djflk')
Select(xialakuang).select_by_index()
Select(xialakuang).select_by_value()
Select(xialakuang).select_by_visible_text()
dr.switch_to.alert
sleep(5)