# == import files and libraries == #
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# import the login page class so it can be used in this set of test run...
from POM_files.pages.login_page_main_cls import LoginPage

# Create a Pytest fixture and leverage what can be set up and tear down...
@pytest.fixture()
def driver():
    # instance for CHROME Browser...
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # additional further actions...
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

# Parameterization in Pytest...
@pytest.mark.parametrize('username, password',[
    ('test','test'),
    ('wrong_usr1', 'wrong_pwd1'),
    ('wrong_usr2', 'wrong_pwd2'),
    ('test', 'test'),
])

# make this as a class with "test" as a starting class name so Pytest is able to recognize it as a set to be run
def test_googles_search(driver, username, password):
    # use and call the class function parameters (from the class source file) to use all of its methods...
    login_page = LoginPage(driver)
    time.sleep(5)
    login_page.login_actions('https://trytestingthis.netlify.app', username, password)
    time.sleep(5)
    # display a confirmation of test result...
    print("Test Chrome (login page) DONE!")