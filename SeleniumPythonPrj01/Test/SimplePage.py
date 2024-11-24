# == import files and libraries == #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# instance for "driver"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# run a test using google browser
driver.get("https://www.google.ca/")
time.sleep(10)
driver.close()
driver.quit()
print("Test PASSED!")
