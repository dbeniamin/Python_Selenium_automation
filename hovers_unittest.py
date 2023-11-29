from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest


class TestHovers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_hovers(self):
        hovers_page = self.driver.find_element(By.LINK_TEXT, "Hovers")
        hovers_page.click()
        action = webdriver.ActionChains(self.driver)
        # same class items with hover attribute can be found using Xpath and value as index of the element
        hover_element = self.driver.find_element(By.XPATH, '// *[ @ id = "content"] / div / div[1] / img')
        action.move_to_element(hover_element).perform()
        detail_hover = self.driver.find_element(By.LINK_TEXT, "View profile")
        # make a try bloc to raise assertion -> link appears under element when hovering in this case
        # use the no such element to catch the exception
        try:
            assert detail_hover.is_displayed()
        except NoSuchElementException:
            raise AssertionError(f"{detail_hover} is not present on the page")


if __name__ == "__main__":
    unittest.main()
