from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestCheckBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_check_boxes(self):
        # find the link text to the specific page
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        # find and define first checkbox
        check_box_1 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
        # click the first checkbox
        check_box_1.click()
        # get the specific attribute for the checkbox
        box1_attribute = check_box_1.get_attribute("checked")
        # assert to test the code
        self.assertIsNotNone(box1_attribute, "The first box did not changed its status !!")
        # time.sleep(4)
        # test the 2-nd checkbox
        # the 2nd box is checked by default
        check_box_2 = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
        check_box_2.click()
        box2_attribute = check_box_2.text
        self.assertEqual(box2_attribute, "", "The 2nd box did not change its status !!")


""" you cant pass the .get_attribute("some string") to be used for box2 because """
""" if the attribute of box2 is not present it will return None """
""" if the attribute is pressent but has an empty value it will still return None """
""" so extract the text, user assertEqual and pass an empty string as condition """
