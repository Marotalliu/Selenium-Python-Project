import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#Trouver le boutton Click for Confirm
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
time.sleep(3)

#recuperer l'alerte a l'aide d'une variable dans le cas du'utilisation repete
confirmWindow = driver.switch_to.alert
print(confirmWindow.text)

#Cliquer sur le button cancel du confirm
confirmWindow.dismiss()

time.sleep(3)
driver.quit()



