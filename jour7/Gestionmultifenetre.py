import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

#Mettre le driver 1ere fenetre dans une variable
parentWindowId = driver.current_window_handle
#L'identifiant de la 1ere fenetre: CDwindow-33A6791FE4968DD3954303CDF6E47355
print(parentWindowId)
time.sleep(3)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
#recup la liste des ids de fenetres ouvertes
windowsHandlesIDs = driver.window_handles
#1ere fenetre : CDwindow-8A8BE6B92A0377B0FB09BA917760C474
parentWindowId = windowsHandlesIDs[0]
#2éme fenetre : CDwindow-0733A2BE0E71D1F99F3A34927C41953E
childWindowId = windowsHandlesIDs[1]

print("parentWindowId : ", parentWindowId)
print("childWindowId : ", childWindowId)
#Basculer vers la 2eme fenetre, recup url et titre(2eme fenetre)

url1 = driver.current_url
title1 = driver.title
print(url1)
print(title1)
print("#########################################")
driver.switch_to.window(childWindowId)
url2 = driver.current_url
title2 = driver.title
print(url2)
print(title2)

#2eme approche: parcourrir la liste de windowHandleIds et verifer le titre
for winId in windowsHandlesIDs:
    driver.switch_to.window(winId)
    if driver.title == title1:
        driver.close()


time.sleep(3)

driver.quit()
