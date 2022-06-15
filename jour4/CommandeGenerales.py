import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# 1 obtenir url de la page
driver.get("https://demo.nopcommerce.com/")
url_page = driver.current_url
print(url_page)

# 2 obtenir title page
titre_page = driver.title
print(titre_page)

# 3 obtenir title page
source_page = driver.page_source
print(source_page)


time.sleep(2)
driver.close()