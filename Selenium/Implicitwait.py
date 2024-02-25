import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)#Globally works
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)#Implicit wait not work for list therefor define
results=driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
count=len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()#chaining of web element rule

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(5)
