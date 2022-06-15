import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://login.salesforce.com/?locale=fr-ca
driver.get("https://login.salesforce.com/?locale=fr-ca")
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("Admin")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("admin123")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title = driver.title
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
exp_title = "Connexion | Salesforce"
if act_title == exp_title:
  print("Le test Login est passed")
else:
  print("Le test Login est failed")

time.sleep(5)
# 8) Fermer le navigateur
driver.close()
