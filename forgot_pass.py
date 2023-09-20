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
    forgot_pass = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Forgot Password')   #locating the text link to be accessed
    ))
    forgot_pass.click()    
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("testing@seleniumlearning")
 # the send_keys("email address") refers to the email that is used for testing purposes
    time.sleep(1)
    driver.find_element(By.ID, "form_submit").click()
    time.sleep(1)
    
 # assert driver.find_element(By.ID, "message").text == "Your e-mail's been sent!"
 # an assertion can be added to check if the site returns a message at the end of forgot password process.
   
finally:
    driver.quit()