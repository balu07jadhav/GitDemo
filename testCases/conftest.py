import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        service_obj = Service("C:/Driver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        print("Launching chrome...........")
    elif browser == "firefox":
        service_obj = Service("C:/Driver/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        print("Launching Firefox...........")
    else:
        service_obj = Service("C:/Driver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        print("Launching chrome...........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#html reports code
#def pytest_configure(config):
##    config.metadata['Project Name'] = 'LMS'
 #   config.metadata['Module name'] = 'Login'
 #   config.metadata['Tester'] = 'Balu Jadhav'

#It is hook for delete/modify environment info to html reports
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
##    metadata.pop("JAVA_HOME", 'None')
 #   metadata.pop("Plugins", 'None')