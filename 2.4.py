#from selenium import webdriver
#
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#browser.get("http://suninjuly.github.io/wait1.html")
#
#button = browser.find_element_by_id("verify")
#button.click()
#message = browser.find_element_by_id("verify_message")
#
#assert "successful" in message.text
#
#from selenium import webdriver
#
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#browser.get("http://suninjuly.github.io/cats.html")
#browser.find_element_by_id("button")
#
#from selenium import webdriver
#
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
## говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(5)
#
#browser.get("http://suninjuly.github.io/wait2.html")
#
#button = browser.find_element_by_id("verify")
#button.click()
#message = browser.find_element_by_id("verify_message")
#
#assert "successful" in message.text
#
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#
#browser = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
#
#browser.get("http://suninjuly.github.io/wait2.html")
#
## говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#button = WebDriverWait(browser, 5).until(
#        EC.element_to_be_clickable((By.ID, "verify"))
#    )
#button.click()
#message = browser.find_element_by_id("verify_message")
#
#assert "successful" in message.text
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import sin, log
import time
driver = webdriver.Chrome(executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
driver.get('http://suninjuly.github.io/explicit_wait2.html')
driver.implicitly_wait(5)
button = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = driver.find_element_by_id('book')
button.click()
x = int(driver.find_element_by_id('input_value').text)
y = str(log(abs(12*sin(x))))
driver.find_element_by_id('answer').send_keys(y)
submit = driver.find_element_by_id('solve')
driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()
time.sleep(5)

