import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pageObjects.loginPage import Login
from utilities.readProperties import readconfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = readconfig.getApplicationURL()
    useremail = readconfig.getUserMail()
    password = readconfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**********************Test001 Login************************************")
        self.logger.info("**********************Validating home page************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**********************Test001 passed************************************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.logger.error("**********************Test001 failed ************************************")
            assert False

    def test_login(self,setup):
        self.logger.info("**********************Validating login ************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********************Login test passed************************************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.error("**********************Login failed ************************************")
            assert False
        self.driver.close()




