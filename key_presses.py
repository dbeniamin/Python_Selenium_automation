from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # using as to rename de imported blocks
from selenium.webdriver.common.action_chains import ActionChains # importing actions (for sending keys without an web element)
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
action = webdriver.ActionChains(driver)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    key_presses_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Key Presses')
    ))
    key_presses_link.click()
    ActionChains(driver)\
        .send_keys(Keys.RETURN)\
        .perform()
    time.sleep(1)
    ActionChains(driver)\
        .send_keys(Keys.SPACE)\
        .perform()
    time.sleep(1)                  # delay between action keys pressed
    ActionChains(driver)\
        .send_keys(Keys.TAB)\
        .perform()
    time.sleep(2)
 
   
finally:
    driver.quit()