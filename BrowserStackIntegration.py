import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'name': 'Scrive Sign Test',
 'build': 'ScriveBrowserStackTest'
}
driver = webdriver.Remote(
    command_executor='https://anusharamachandr_wrncGb:enXD8k7qPbAx5Z4Bc4Lc@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.maximize_window()
driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
time.sleep(3)
nametext = driver.find_element_by_xpath("//h1[normalize-space()='About you']")
driver.execute_script("arguments[0].scrollIntoView();",nametext)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='name']").send_keys('Anusha Ramachandra')
time.sleep(3)
driver.find_element_by_xpath("//a[@class='button button-block action']//div[@class='label']").click()
driver.implicitly_wait(3)
element = driver.find_element_by_xpath("//div[@class='section sign above-overlay']")
time.sleep(3)
driver.find_element_by_xpath("//a[@class='button button-block sign-button action']//div[@class='label']").click()
time.sleep(3)
element = driver.find_element_by_xpath("//span[normalize-space()='Document signed!']").text
print(element)
assert element == "Document signed!"
time.sleep(3)
try:
    WebDriverWait(driver, 5).until(EC.title_contains("Scrive"))
    # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
except TimeoutException:
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
print(driver.title)
driver.close()
driver.quit()