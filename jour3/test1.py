# Test case register

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

# 3 cliquer sur le lien register
driver.find_element(By.LINK_TEXT, "Register").click()
# cliquer sur le lien register, en utilise le localisateur Partial_linktext
# driver.find_element(By.PARTIAL_LINK_TEXT, "Regi").click()

# 4 remplir le formulaire
driver.find_element(By.ID, "FirstName").send_keys("Bing")
driver.find_element(By.ID, "LastName").send_keys("LIU")
driver.find_element(By.ID, "Email").send_keys("marotalliu@gmail.com")
driver.find_element(By.ID, "Password").send_keys("098765")
driver.find_element(By.ID, "ConfirmPassword").send_keys("098765")

# 5 cliquer sur le bouton Register
driver.find_element(By.ID, "register-button").submit()
# driver.find_element(By.CLASS_NAME, "button-1").submit()
time.sleep(4)

# 6 Fermer le navigateur
driver.close()

