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
    horizontal_slider = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Horizontal Slider")
    ))
    horizontal_slider.click()
    time.sleep(1)
    
    slider_handle = driver.find_element(By.CSS_SELECTOR, "div.sliderContainer input[type='range']")
# defining actions to be performed as action chains driver
    actions = ActionChains(driver)
# Drag the slider handle xxx pixels to the right
    actions.drag_and_drop_by_offset(slider_handle, 50, 0) # x offset and y offset arguments for drag and drop
    actions.perform()

    slider_value = driver.find_element(By.CSS_SELECTOR, "#range").text
    time.sleep(1)

finally:
    driver.quit()
