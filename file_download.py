from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
  # use to wait for the full page to load - set max time to wait as argument for the implicitly wait
driver.implicitly_wait(10)
  # use xpath to find element
  # use value attribute from xpath to target the position of file to be downloaded ie: [the postion of the file ]
  # only usable if the downloadable items are all in the same class
  # for other cases you might need to locate each element separatelly
driver.find_element (By.XPATH, '//*[@id="content"]/div/a[19]').click()
  # use time sleep to see the file downloaded before closing the page
  # the site does not have a confirmation message for download so you need to wait
time.sleep(5)

driver.quit
