from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest


class TestGeolocation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_geolocation(self):
        geolocation_page = self.driver.find_element(By.LINK_TEXT, "Geolocation")
        geolocation_page.click()
        self.driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()
        google_link = self.driver.find_element(By. XPATH, '//*[@id="map-link"]/a')
        # make a try bloc to raise assertion that the Google link  is present after getting the geolocation
        # use the no such element to catch the exception
        try:
            assert google_link.is_displayed()
        except NoSuchElementException:
            raise AssertionError(f"{google_link} is not present on the page")


if __name__ == "__main__":
    unittest.main()
