from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class Horizontal_Slider(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    def test_slider(self):
        slider = self.driver.find_element(By.XPATH, "//input[@type='range']")
        
        # Move the slider to the right 
        slider.send_keys(Keys.ARROW_RIGHT)
        slider.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)  # Wait for the animation to complete
        
        # Get the slider's value and convert it to a float
        slider_value = float(slider.get_attribute("value"))
        
        # Assert that the slider value is equal to how many times the right arrow was pressed times the increment in the page
        self.assertEqual(slider_value, 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
