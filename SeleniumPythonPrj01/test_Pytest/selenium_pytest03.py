# == import files and libraries == #
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

# Create a Pytest fixture and leverage what can be set up and tear down...
@pytest.fixture()
def chrome_browser():
    # instance for CHROME Browser...
    service = ChromeService(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service)
    # chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #chromeBrowser = webdriver.Chrome()
    # additional further actions...
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.close()
    chrome_browser.quit()

# Parameterization in Pytest...
@pytest.mark.parametrize('username, password',[
    ('test','test'),
    ('wrong_usr1', 'wrong_pwd1'),
    ('wrong_usr2', 'wrong_pwd2'),
    ('test', 'test'),
])

# make this as a class with "test" as a starting class name so Pytest is able to recognize it as a set to be run
def test_googles_search(chrome_browser, username, password):
    # run another  test using browser
    chrome_browser.get('https://trytestingthis.netlify.app')
    time.sleep(10)
    chrome_browser.find_element(By.ID, "uname").send_keys(username)
    chrome_browser.find_element(By.ID, "pwd").send_keys(password)
    time.sleep(2)
    chrome_browser.find_element(By.XPATH, "//input[@value = 'Login']").click()
    # additional further actions...
    assert "Successful" in chrome_browser.page_source
    time.sleep(5)
    # display a confirmation of test result...
    print("Test Chrome run DONE!")