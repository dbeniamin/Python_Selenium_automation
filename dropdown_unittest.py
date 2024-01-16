import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def test_dropdown(self):
        dropdown = self.driver.find_element(By.ID, "dropdown")
        # get all the options in the dropdown
        options = Select(dropdown).options
        # assert how many options you have in the dropdown i.e. 3
        self.assertEqual(len(options), 3)
        # select the first option based on the idex i.e. - index number can be adjusted
        Select(dropdown).select_by_index(0)
        # assert that the first option is selected
        self.assertEqual(Select(dropdown).first_selected_option.text, "Please select an option")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
