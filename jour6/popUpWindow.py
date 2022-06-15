import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/basic_auth")

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


time.sleep(3)
driver.quit()



