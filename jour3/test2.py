# Test case login

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1 lancer le navigateur
service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.maximize_window()

# 2 acceder a l'adresse https://demo.nopcommerce.com/
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

# 3 remplir le formulaire
driver.find_element(By.CLASS_NAME, "ico-login").click()
driver.find_element(By.ID, "Email").send_keys("marotalliu@gmail.com")
driver.find_element(By.ID, "Password").send_keys("098765")
time.sleep(2)

# 4 cliquer sur le bouton Login
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
# driver.find_element(By.LINK_TEXT, "LOG IN").submit()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(3)

# 5 Fermer le navigateur
driver.close()