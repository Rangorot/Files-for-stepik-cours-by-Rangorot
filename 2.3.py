#from selenium import webdriver
#import time
#from math import log, sin
#try:
#    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#    driver.get('http://suninjuly.github.io/alert_accept.html')
#    driver.find_element_by_css_selector('.btn.btn-primary').click()
#    confirm = driver.switch_to.alert
#    confirm.accept()
#    x = int(driver.find_element_by_id('input_value').text)
#    y = str(log(abs(12*sin(x))))
#    driver.find_element_by_id('answer').send_keys(y)
#    driver.find_element_by_css_selector('.btn.btn-primary').click()
#    time.sleep(8)
#finally:
#    driver.quit()
#
from selenium import webdriver
import time
from math import log, sin
try:
    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    driver.find_element_by_css_selector('.trollface.btn.btn-primary').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x = int(driver.find_element_by_id('input_value').text)
    y = str(log(abs(12*sin(x))))
    driver.find_element_by_id('answer').send_keys(y)
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(8)
finally:
    driver.quit()
