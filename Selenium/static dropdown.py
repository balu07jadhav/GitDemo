import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
options = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
options.select_by_index(1)
options.select_by_visible_text("Female")
time.sleep(4)