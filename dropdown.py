from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # using as to rename de imported blocks
from selenium.webdriver.support.ui import Select
import time 

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    drop_down = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Dropdown')
    ))
    drop_down.click()

    time.sleep(1)

    drop = driver.find_element(By.ID, "dropdown")

    drop.click() # - using this line will click and open the drop down and show the available options
    # the code can run with or without the above line 
    time.sleep(1)
 # select the element with index 1
    Select(drop).select_by_index(1)

    time.sleep(1)
 # select the element with index 2
    Select(drop).select_by_index(2)

    time.sleep(1)
 # Note - index 0 is "Please select an option"       
   
finally:
    driver.quit()