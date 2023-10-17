from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/entry_ad')
# maximize the window so its more visible
driver.maximize_window()
time.sleep(3)
# find the add close button and define it as a variable
close_ad = driver.find_element(By.XPATH, "//p[normalize-space()='Close']")

action = ActionChains(driver)
# close the add using the defined variable
action.click(close_ad).perform()
# find the ad restart button and define it as variable
restart_ad = driver.find_element(By.CSS_SELECTOR, "#restart-ad")
# restart the ad
action.click(restart_ad).perform()
time.sleep(2)

driver.quit()
