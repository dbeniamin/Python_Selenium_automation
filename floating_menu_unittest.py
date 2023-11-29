from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest


class TestFloatMenu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 750)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_floating_menu(self):
        floating_page = self.driver.find_element(By.LINK_TEXT, "Floating Menu")
        floating_page.click()
        body = self.driver.find_element(By. XPATH, '/html/body')
        # use the END key to instantly scroll at the bottom of the page
        body.send_keys(Keys.END)
        # if there are multiple elements on the float menu they can be tested:
        # by changing the [1] to the number of the element you want to test
        # in this case 1 = Home, 2 = News, 3 = Contact, 4 = About
        floating_element = self.driver.find_element(By. XPATH, '//*[@id="menu"]/ul/li[1]/a')
        # make a try bloc to raise assertion that the tested element is still present even after the scroll down
        # use the no such element to catch the exception
        try:
            assert floating_element.is_displayed()
        except NoSuchElementException:
            raise AssertionError(f"{floating_element} is not present on the page")


if __name__ == "__main__":
    unittest.main()
