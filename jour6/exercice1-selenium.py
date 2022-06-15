import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Entrer dans le frame
driver.switch_to.frame("packageListFrame")
time.sleep(3)

# Cliquer sur le lien
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)

# Sortir de frame et retourner a la page principale
driver.switch_to.default_content()

# Entrer dans 2ere frame
driver.switch_to.frame("packageFrame")
time.sleep(3)

# Cliquer sur le lien
#driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[14]/a/span").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

time.sleep(3)
driver.quit()
