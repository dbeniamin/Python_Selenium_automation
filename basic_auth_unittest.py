import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestBasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.set_window_size(1250, 850)

    def tearDown(self):
        self.driver.quit()

    def test_basic_auth(self):
        self.driver.find_element(By.LINK_TEXT, 'Basic Auth').click()
        self.driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
        successful_authentication = "Congratulations! You must have the proper credentials."
        self.assertTrue(successful_authentication in self.driver.page_source,
                        f"Expected message '{successful_authentication}' not found on the page.")


if __name__ == '__main__':
    unittest.main()
