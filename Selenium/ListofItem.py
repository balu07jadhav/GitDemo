import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expectedlist=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actuallist=[]
service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)#Globally works
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)#Implicit wait not work for list therefor define
results=driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
count=len(results)
assert count > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)#append used to add items in list
    result.find_element(By.XPATH,"div/button").click()#chaining of web element rule

assert expectedlist == actuallist
print(expectedlist)
print(actuallist)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#table column validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
for price in prices:
    sum = sum + int(price.text)

print(sum)

total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(total)
assert sum == total

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)#Explicit wait define
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))#Explicit wait implimented
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
TotalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
DiscountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(TotalAmount)
print(DiscountAmount)
assert TotalAmount > DiscountAmount
time.sleep(2)
