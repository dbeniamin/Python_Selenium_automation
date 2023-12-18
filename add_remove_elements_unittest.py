from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
### import time
# use time.sleep if you want to see the results or the actions
# remove or comment time.sleep after you saw the test running as desired


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_add_remove_elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        # use a for loop to click multiple times on the same element
        # inside the for loop find the element and pass the .click() on the same line
        for _ in range(10):
            self.driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
        # same loop situation after the elements have been added

        ### time.sleep(2)

        for n in range(8):
            self.driver.find_element(By.CLASS_NAME, "added-manually").click()
        ### time.sleep(2)

        # getting the len of remaining elements
        # use driver.find_elements, so it will generate a list and len() can be extracted
        # if you user driver.find_element -> you will have a len() error
        remaining_elements = len(self.driver.find_elements(By.CLASS_NAME, "added-manually"))
        # assertion to check the len against the actual difference from the loops
        self.assertEqual(remaining_elements, 2, )


if __name__ == "__main__":
    unittest.main()
