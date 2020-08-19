#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#import time
#driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#driver.get('http://suninjuly.github.io/selects1.html')
#driver.maximize_window()
#x = str(int(driver.find_element_by_id('num1').text) + int(driver.find_element_by_id('num2').text))
#select = Select(driver.find_element_by_tag_name('select'))
#select.select_by_value(x)
#driver.find_element_by_css_selector('.btn.btn-default').click()
#time.sleep(8)
#driver.quit()

#import time
#from selenium import webdriver
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#browser.execute_script("document.title='Script executing';")
#browser.execute_script("alert('Robots at work');")

#browser.execute_script("document.title='Script executing';alert('Robots at work');")
#time.sleep(8)
#browser.quit()
#
#from selenium import webdriver
#
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#
##button = browser.find_element_by_tag_name("button")
##button.click()
#
#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
#
#assert True
#
#from selenium import webdriver
#import time
#from math import log, sin
#try:
#    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#    driver.get('http://suninjuly.github.io/execute_script.html')
#    x = int(driver.find_element_by_id('input_value').text)
#    y = str(log(abs(12*sin(x))))
#    driver.find_element_by_id('answer').send_keys(y)
#    driver.execute_script("window.scrollBy(0, 100);")
#    driver.find_element_by_id('robotCheckbox').click()
#    driver.find_element_by_id('robotsRule').click()
#    driver.find_element_by_css_selector('.btn.btn-primary').click()
#    time.sleep(8)
#finally:
#    driver.quit()
#
from selenium import webdriver
import time, os
try:
    driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element_by_css_selector('.form-group .form-control:nth-child(2)').send_keys('Name')
    driver.find_element_by_css_selector('.form-group .form-control:nth-child(4)').send_keys('Last name')
    driver.find_element_by_css_selector('.form-group .form-control:nth-child(6)').send_keys('Email')
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, '1.txt')
    driver.find_element_by_id('file').send_keys(file_path)
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(8)
finally:
    driver.quit()