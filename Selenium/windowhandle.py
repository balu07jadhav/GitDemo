from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
openedwindows = driver.window_handles #get the list of opened windows
driver.switch_to.window(openedwindows[1])#switch to 2nd window
print(driver.find_element(By.XPATH, "//h3").text)
driver.close()#It close current window
driver.switch_to.window(openedwindows[0]) #switch to 1st window
assert "Opening a new window" == driver.find_element(By.XPATH, "//h3").text