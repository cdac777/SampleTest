# == import files and libraries == #
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Create a Pytest fixture and leverage what can be set up and tear down...
@pytest.fixture()
def chrome_browser():
    # instance for CHROME Browser...
    chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #chromeBrowser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.close()
    chrome_browser.quit()

# make this as a class with "test" as a starting class name so Pytest is able to recognize it as a set to be run
def test_googles_search(chrome_browser):
    # run a test using browser
    chrome_browser.get('https://www.google.ca')
    # find the Search box...
    google_search_box = chrome_browser.find_element(By.ID, "APjFqb")
    # insert a text...
    google_search_box.send_keys("Automation")
    # click the Google Search button...
    chrome_browser.find_element(By.NAME, "btnK").click()
    # additional further actions...
    time.sleep(10)
    # display a confirmation of test result...
    print("Test Chrome PASSED!")