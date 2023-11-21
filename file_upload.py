from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
driver.implicitly_wait(10)

upload_file = driver.find_element (By.CSS_SELECTOR, '#file-upload')
# for some reasons you cant upload files that are on the root user location - no idea why 
# the path from windows will be "C:\folder name\ etc" you need to add "\" after C: for the code to work because path is not absolute C:
# the file name and location has to be specific for your machine
upload_file.send_keys("C:\\your folder name\another folder name\file name.png")
driver.implicitly_wait(10)
# add a sleep sequence to see the file sent to the upload field
time.sleep(3)
# find the submit button and pass the .click() action
driver.find_element(By.CSS_SELECTOR, "#file-submit").click()
driver.implicitly_wait(10)
# creeate a result element so you can pass an assertion
# can be passed without creating the variable but i prefer to use it like this for visibility
result = driver.find_element(By.CSS_SELECTOR, "#uploaded-files")
# assertion to check if the succesfull upload action has the selected file name
# test using the .text method to match the strings
assert result.text == "file name.png"
time.sleep(2)
driver.quit

### drag and drop for the other element is still broken so testing the other element is imposible ####