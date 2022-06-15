# Test case www.saucedemo.com

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1 lancer le navigateur
service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.maximize_window()

# 2 acceder a l'adresse
driver.get("https://www.saucedemo.com/")

# 3 remplir le formulaire
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
time.sleep(2)
driver.find_element(By.ID, "checkout").click()
time.sleep(2)
driver.find_element(By.ID, "cancel").click()
time.sleep(2)

#  4 Fermer le navigateur
driver.close()