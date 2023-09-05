from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # using as to rename de imported blocks
import time 

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    basic_auth = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Basic Auth')   #locating the link text to be accessed
    ))
    basic_auth.click()
    # (the driver.get stated here can be skipped if the test does not require
    #  to identify and click the element that is redirecting to the pop up authencication page.)
        
    time.sleep(1)
    # passing the user / pass in case of popup window that is not a HTML code and cannot be inspected.
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
    #the user / app are passed in the url as shown above.
    
    time.sleep(1)
   
finally:
    driver.quit()