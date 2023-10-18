from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
time.sleep(2)

# can be used to acction the other buttons on the page
js_alert = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
action = ActionChains(driver)
js_alert.click()
time.sleep(1)

# switching to opened pop-up that is js alert
alert = driver.switch_to.alert

# accepting the alert
alert.accept()
time.sleep(1)
result = driver.find_element(By.CSS_SELECTOR, "#result")
expected_result = "You successfully clicked an alert"

# compare the text of the result element with the expected_result
# if they don't match, the test will fail and display the actual and expected results in the error message.
# modify the string that is defining the expected_result and test again
assert result.text == expected_result, f"Actual result: {result.text}, Expected result: {expected_result}"
time.sleep(3)

driver.quit()