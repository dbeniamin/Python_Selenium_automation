import selenium
from selenium.webdriver.common.by import By
import unittest


class TestStatusCodes(unittest.TestCase):
    # the setUp and tearDown functions will repeat during all test process
    def setUp(self):
        self.driver = selenium.webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 750)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_download_secure(self):
        self.driver.find_element(By.LINK_TEXT, "Redirect Link").click()
        self.driver.find_element(By.LINK_TEXT, "here").click()
        # is it possible to pass the click action directly to the link text but will make it hard to assert
        code_500 = self.driver.find_element(By.LINK_TEXT, "500")
        code_500.click()
        # locate the new element that contains the status message
        status_page = self.driver.find_element(By.XPATH,
                                               "//p[contains(text(),'This page returned a 500 status code.')]")
        # assert to see if the loaded page has the correct message
        assert 'This page returned a 500 status code.' in status_page.text
        # use the .back() to go back one page
        self.driver.back()

        code_404 = self.driver.find_element(By.LINK_TEXT, "404")
        code_404.click()
        status_page = self.driver.find_element(By.XPATH,
                                               "//p[contains(text(),'This page returned a 404 status code.')]")
        assert 'This page returned a 404 status code.' in status_page.text
        self.driver.back()

        code_301 = self.driver.find_element(By.LINK_TEXT, "301")
        code_301.click()
        status_page = self.driver.find_element(By.XPATH,
                                               "//p[contains(text(),'This page returned a 301 status code.')]")
        assert 'This page returned a 301 status code.' in status_page.text
        self.driver.back()

        code_200 = self.driver.find_element(By.LINK_TEXT, "200")
        code_200.click()
        status_page = self.driver.find_element(By.XPATH,
                                               "//p[contains(text(),'This page returned a 200 status code.')]")
        assert 'This page returned a 200 status code.' in status_page.text
        self.driver.back()


if __name__ == "__main__":
    unittest.main()
