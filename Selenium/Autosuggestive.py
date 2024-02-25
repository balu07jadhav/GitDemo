import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind") #locate dropdown
time.sleep(3)
options=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") #Store all option in variable
for option in options: # for loop for select single option
    if option.text == "India":
        option.click()
        break
#print(driver.find_element(By.ID, "autosuggest").text) It now working
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
#assert
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(5)
