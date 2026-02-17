from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

urLinput = input("Enter a url: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(urLinput)

time.sleep(5) 

images = driver.find_elements(By.TAG_NAME, "img")

img_urls = []
for img in images:
    src = img.get_attribute("src")
    if src:
        img_urls.append(src)

c = 0
for i in img_urls:
    print(i)

driver.quit(),
