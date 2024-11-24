# == import files and libraries == #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

# == extra import files and libraries == #
# from selenium.webdriver import Keys

# instance for CHROME Browser...
chromeABrowser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# run a test using browser
chromeABrowser.get('https://www.google.ca')

# find the Search box...
googleSearchBox = chromeABrowser.find_element(By.ID, "APjFqb")
# insert a text...
googleSearchBox.send_keys("Automation")
# click the Google Search button...
waitChrome = WebDriverWait(chromeABrowser, 5)
elementChrome = waitChrome.until(ec.element_to_be_clickable((By.NAME,"btnK")))
chromeABrowser.find_element(By.NAME,"btnK").click()
# another way to test the search button (mirrors the action of hitting the enter button after typing what to search)
# >> googleSearchBox.send_keys(Keys.RETURN)

# additional further actions...
time.sleep(10)
chromeABrowser.close()
chromeABrowser.quit()
# display a confirmation of test result...
print("Test Chrome (A) PASSED!")

# another instance for CHROME Browser...
chromeBBrowser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# run another  test using browser
chromeBBrowser.get('https://trytestingthis.netlify.app')
# insert text(s)...
time.sleep(5)
chromeBBrowser.find_element(By.ID, "fname").send_keys("JOHN")
chromeBBrowser.find_element(By.ID, "lname").send_keys("DOE")
time.sleep(5)
chromeBBrowser.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()

# additional further actions...
time.sleep(5)
chromeBBrowser.close()
chromeBBrowser.quit()
# display a confirmation of test result...
print("Test Chrome (B) PASSED!")

# instance for EDGE Browser...
#   if __name__ == '__main__':
edgeBrowser = webdriver.Edge()
# run a test using browser
edgeBrowser.get('https://www.google.ca')

# find the Search box...
googleSearchBox = edgeBrowser.find_element(By.ID, "APjFqb")
# insert a text...
googleSearchBox.send_keys("Automation")
# click the Google Search button...
waitEdge = WebDriverWait(edgeBrowser, 5)
elementEdge = waitEdge.until(ec.element_to_be_clickable((By.NAME,"btnK")))
edgeBrowser.find_element(By.NAME,"btnK").click()
# another way to test the search button (mirrors the action of hitting the enter button after typing what to search)
# >> googleSearchBox.send_keys(Keys.RETURN)

# additional further actions...
time.sleep(5)
edgeBrowser.close()
edgeBrowser.quit()
# display a confirmation of test result...
print("Test Edge PASSED!")