import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#Trouver le boutton Click for JS Alert
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
time.sleep(3)

#recuperer l'alerte a l'aide d'une variable dans le cas du'utilisation repete
alertWindow = driver.switch_to.alert
print(alertWindow.text)

#Cliquer sur le button OK de l'alerte (dismiss = cancel)
alertWindow.accept()

time.sleep(3)
driver.quit() #Fermer touts les fenetres, driver.close() only fermer the first window