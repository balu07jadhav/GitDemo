import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name='Balu'
service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert=driver.switch_to.alert#it switch browser to alert
print(alert.text) #text printing available on alerts
alerttext = alert.text
assert name in alerttext #validate name in alerts text
alert.accept() #axcept the ok button
alert.dismiss() #axcept the cancel button

