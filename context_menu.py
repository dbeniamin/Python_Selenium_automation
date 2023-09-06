from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # using as to rename de imported blocks
from selenium.webdriver.common.action_chains import ActionChains # importing actions (for sending keys without an web element)
import time 

driver = webdriver.Chrome()
action = webdriver.ActionChains(driver)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    context_menu = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Context Menu')
    ))
    context_menu.click()
 # finiding element based on ID 
    dot_box = driver.find_element(By.ID, "hot-spot")
 # moving the mouse over the box doing a right click ( context_click = right click )
    ActionChains(driver).move_to_element(dot_box).context_click().perform()
 # switching the the pop up that appeard - also reffered to as allert.
    alert = driver.switch_to.alert
 # defining the alert text variable
    s = alert.text
    print("Alert text: ")
    print(s)
 #accept alert
    alert.accept()

    time.sleep(1)

finally:
    driver.quit()