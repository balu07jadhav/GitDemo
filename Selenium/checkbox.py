import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:/Driver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
select=Select(driver.find_element(By.XPATH, "//select[@name='dropdown-class-example']"))#select class for dropdown
select.select_by_index(2)
#driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()#xpath using index for checkbox
#Another way for checkbox select
lists=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(lists))#len used to display length of elements
for list in lists:
    if list.get_attribute("name")=="checkBoxOption2":
        list.click()
        assert list.is_selected() #this methos used to selected or not element
        print(list.get_attribute("value")) #this used to select attribute
        break


#same way can use for radio buuton, now here one more way
radiobutton=driver.find_elements(By.CSS_SELECTOR, " .radioButton")
radiobutton[1].click()
assert radiobutton[1].is_selected()

assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

driver.find_element(By.XPATH, "(//input[@class='btn-style class2'])[1]").click()
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()#if condition failed tc will execute

time.sleep(1)