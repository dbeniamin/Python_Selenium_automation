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
    checkboxes = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Checkboxes')
    ))
    checkboxes.click()

    time.sleep(1)

 # using XPath since there is no class. Standard syntax for XPath is -> XPath=//tagname[@attribute='value']
 #// : Select the current node.
 #Tagname: Tagname of the particular node.
 #@: Select attribute.
 #Attribute: Attribute the name of the node.
 #Value: Value of the attribute.

    driver.find_element(By.XPATH, ('//*[@id="checkboxes"]/input[1]')).click()
 # click the first checkbox
    time.sleep(1)

    driver.find_element(By.XPATH, ('//*[@id="checkboxes"]/input[2]')).click()
 # click the 2nd checkbox
    time.sleep(1)

    driver.find_element(By.XPATH, ('//*[@id="checkboxes"]/input[1]')).click()
 # click the first checkbox again
    time.sleep(1)

finally:
    driver.quit()