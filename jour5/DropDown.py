import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")


drop_country = driver.find_element(By.ID,"input-country")
country = Select(drop_country)

# Selection par texte visible(dynamique)
# country.select_by_visible_text("China")

# selection par index(Statique),1 commence le 1er rang
# country.select_by_index(1)

# selection par value
country.select_by_value("44")

# recup de toutes les options dans Select
all_options = country.options
total_options = len(all_options)
print("Le nombre total d'options : ", total_options)
# Afficher toutes les options dans la console
# for opt in all_options:
#     print(opt.text)

# select le Canada dans country et cliquer dessus
for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break


#google搜索selenium动态结果
#//ul[@role='listbox']//li/descendant::div/span



time.sleep(5)

driver.close()