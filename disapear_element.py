from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # using as to rename de imported blocks
import time 
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    disappear_element = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Disappearing Elements')
    ))
    disappear_element.click()

    time.sleep(1)
    if driver.find_element(By.XPATH, "//a[contains(text(), 'Gallery')]"):
        print("Element 'Gallery' was found")
            #  check new page
        driver.find_element(By.XPATH, "//a[@href='/gallery/']").click()
        driver.implicitly_wait(3)
        if driver.find_element(By.XPATH, "//h1[contains(text(), 'Not Found')]"):
            print("New page opened")
    driver.refresh()
except NoSuchElementException:
        print("Element 'Gallery' not found")
        driver.refresh()

finally:
    driver.quit()