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
    add_remove = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Add/Remove Elements')
    ))
    add_remove.click()

    time.sleep(2)
# the button needed does not have a class or id , xpath location required, @inspect 'required text' = >given text at inspect<
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()  # click-ing the button found 
    time.sleep(2)
# inspect newlly added button to find class => easyer to locate by class / id    
    driver.find_element(By.CLASS_NAME, "added-manually").click()
    time.sleep(2)
      
   
finally:
    driver.quit()