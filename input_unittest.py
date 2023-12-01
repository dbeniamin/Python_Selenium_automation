import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_input_field(self):
        input_page = self.driver.find_element(By.LINK_TEXT, "Inputs")
        input_page.click()
        input_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        # define a value to be sent in the input field
        test_value = 1234567
        input_field.send_keys(test_value)
        # add the below time.sleep to the code to see the test value being sent in the field
        time.sleep(2)

        # find the value of the input field and assert it
        input_value = input_field.get_attribute("value")
        self.assertEqual(str(test_value), input_value)

        # test the arrow up or arrow down keys based on preference
        # for arrow up add =>  +1 , for arrow down subtract => -1
        input_field.send_keys(Keys.ARROW_UP)
        # add the below time.sleep to the code to see arrow interaction in the field
        time.sleep(2)
        updated_value = input_field.get_attribute("value")
        self.assertEqual(str(test_value + 1), updated_value)


if __name__ == "__main__":
    unittest.main()
