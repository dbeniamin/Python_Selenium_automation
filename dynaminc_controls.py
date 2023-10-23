from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dynamic_controls')
driver.maximize_window()
# introducing wait since the time to wait for elements is not the same
wait = WebDriverWait(driver, 30)
time.sleep(2)

# finding the remove button 
driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button").click()

# waiting for the message to load so it can be checked with assertion 
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#message")))

# checking the message matched the action
assert driver.find_element(By.CSS_SELECTOR, "#message").text == "It's gone!"
time.sleep(1)

# same course of action is writen bellow
# find element -> click element -> wait for the status to update -> check the message
driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#message")))
assert driver.find_element(By.CSS_SELECTOR, "#message").text == "It's back!"
time.sleep(1)

driver.close()
