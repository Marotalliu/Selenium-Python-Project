import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Frames.html")

# Entrer dans le frame
driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Single Frame")
time.sleep(3)

# Sortir de frame et retourner a la page principale
driver.switch_to.default_content()
time.sleep(3)

# Entrer dans 2ere frame
#driver.find_element(By.LINK_TEXT,"Iframe with in an iframe").click()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
driver.switch_to.frame("//*[@id='Multiple']/iframe")
driver.switch_to.frame("/html/body/section/div/div/iframe")


driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Multiple Frames")


time.sleep(3)
driver.quit()
