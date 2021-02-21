from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("https://mail.163.com/")
dr.maximize_window()
iframe = dr.find_element_by_css_selector('#loginDiv iframe')
dr.switch_to.frame(iframe)
dr.find_element_by_css_selector('[name=email]').send_keys('123')
dr.find_element_by_css_selector('div.m-unlogin > a.forgetpwd').click()
handle = dr.window_handles
dr.switch_to.window(handle[1])
dr.find_element_by_css_selector('#app > div > div.g-bd.f-cf > div > div.m-op-box > form > div.nop-form-item.nop-form-item- > div > div.nop-form-item-input-inner > div.bview-suggest-wrapper > div > input').send_keys('123')

sleep(3)
dr.quit()