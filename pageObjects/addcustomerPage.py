import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AddCustomer():
    lnkCustomer_menu_xpath = "(//a[@href='#'])[7]"
    lnkCustomer_menuitem_linktext = "/Admin/Customer/List"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpth = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMale_xpath = "//input[@id='Gender_Male']"
    rdFemale_xpath = "//input[@id='Gender_Female']"
    txtDateOfBirth_xpath = "//input[@id='DateOfBirth']"
    txtCompany_id = "Company"
    chkTaxexempt_id = "IsTaxExempt"
    txtNewsletter_xpath = "(//div[@role='listbox'])[1]"
    txtCustomerRole_xpath = "(//div[@role='listbox'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstForumModerator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstGest_xpath = "//li[contains(text(),'Guests')]"
    istRegistered_xpath = "//li[contains(text(),'Registered')]"
    drpvendor_id = "VendorId"
    chkActive_id = "Active"
    txtAdminComment_id = "AdminComment"
    btnSave_name = "save0"

    def __init__(self,driver):
        self.driver = driver

    def ClickonCustomer_menu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).Click()

    def ClickonCustomer_menuitem(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkCustomer_menuitem_linktext).click()

    def ClickonAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpth).send_keys(password)

    def setFirstname(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lname)

    def setmale(self):
        self.driver.find_element(By.XPATH, self.rdMale_xpath).click()

    def setFemale(self):
        self.driver.find_element(By.XPATH, self..rdFemale_xpath).click()

    def setDateofbirth(self,dob):
        self.driver.find_element(By.XPATH, self.txtDateOfBirth_xpath).send_keys(dob)

    def setCompany(self,companyname):
        self.driver.find_element(By.ID, self.txtCompany_id).send_keys(companyname)

    def settaxexempt(self):
        self.driver.find_element(By.ID, self.chkTaxexempt_id).click()

    def setnewsletter(self,newsletter):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).send_keys(newsletter)

    def setROle(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
        time.sleep(2)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role== "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstForumModerator_xpath)
        elif role== "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.lstGest_xpath)











