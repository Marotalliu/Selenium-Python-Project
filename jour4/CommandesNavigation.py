import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

driver.get("https://www.google.com/")
time.sleep(2)
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)





driver.quit()