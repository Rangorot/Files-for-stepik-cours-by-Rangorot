#from selenium import webdriver
#import time, math
#
#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#try:
#    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#    driver.get('http://suninjuly.github.io/math.html')
#    x = int(driver.find_element_by_id('input_value').text)
#    y = calc(x)
#    driver.find_element_by_id('answer').send_keys(y)
#    driver.find_element_by_id('robotCheckbox').click()
#    driver.find_element_by_id('robotsRule').click()
#    driver.find_element_by_css_selector('.btn.btn-default').click()
#    time.sleep(5)
#finally:
#    time.sleep(5)
#    driver.quit()
#
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
    driver.get('http://suninjuly.github.io/get_attribute.html')
    x = driver.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)
    driver.find_element_by_id('answer').send_keys(y)
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_css_selector('.btn.btn-default').click()
    time.sleep(5)
finally:
    time.sleep(5)
    driver.quit()