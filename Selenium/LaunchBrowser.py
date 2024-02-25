import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service #service package

service_obj = Service("C:/Driver/chromedriver.exe") #chromedriver path

driver = webdriver.Chrome(service=service_obj) #service obj passed in webdriver
driver.get("https://axcendautomation.greythr.com/") #open url
print(driver.title)
print(driver.current_url)
driver.back()
driver.forward()
time.sleep(10)