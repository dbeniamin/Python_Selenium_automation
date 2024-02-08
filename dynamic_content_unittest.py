from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

""" same logic can be applyed to get the text modifications by using xpath '//*[@id="content"]/div[2]/div[2]' """
""" element_text = element.text , and you can extract the len(element.text) """
""" compare len values of the elements in order to see if they changed"""


class DynamicContent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_dynamic_content(self):
        self.driver.find_element(By.LINK_TEXT, "Dynamic Content").click()

        # define elements , find them and extract the attribute
        photo_1 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/img')
        photo_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/img')
        photo_3 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/img')
        photo_1_initial = photo_1.get_attribute("src")
        photo_2_initial = photo_2.get_attribute("src")
        photo_3_initial = photo_3.get_attribute("src")

        self.driver.refresh()

        # get the values of updated elements, the .get_attribute("src") can be passed while finding the element
        photo_1_refreshed = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[1]/div[1]/img'
        ).get_attribute("src")
        photo_2_refreshed = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[2]/div[1]/img'
        ).get_attribute("src")
        photo_3_refreshed = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[3]/div[1]/img'
        ).get_attribute("src")

        # compare initial and updated values
        self.assertEqual(photo_1_initial, photo_1_refreshed, "The content for Photo 1 remains the same")
        self.assertEqual(photo_2_initial, photo_2_refreshed, "The content for Photo 2 remains the same")
        self.assertEqual(photo_3_initial, photo_3_refreshed, "The content for Photo 3 remains the same")
