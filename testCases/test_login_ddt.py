import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pageObjects.loginPage import Login
from utilities.readProperties import readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = readconfig.getApplicationURL()
    path = "testdata/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("**********************Validating login ************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.row = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of row in excel",self.row)
        lst_status=[]
        for r in range(2, self.row+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

        self.lp.setUserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if self.exp=="Pass":
                self.logger.info("****** passed ****")
                self.lp.clickLogout()
                lst_status.append("Pass")
            elif self.exp == "Fail":
                self.logger.info("****** passed ****")
                self.lp.clickLogout()
                lst_status.append("Fail")

        elif act_title != exp_title:
            if self.exp=="Pass":
                self.logger.info("****** failed ****")
                self.lp.clickLogout()
                lst_status.append("Fail")
            elif self.exp == "Fail":
                self.logger.info("****** passed ****")
                self.lp.clickLogout()
                lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("*******Login DDT test passed*****")
            assert True

        else:
            self.logger.info("*******  Login DDt failed *******")
            assert False







