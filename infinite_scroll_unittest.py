import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestInfiniteScroll(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_infinite_scroll(self):
        infinite_scroll_page = self.driver.find_element(By.LINK_TEXT, "Infinite Scroll")
        infinite_scroll_page.click()

        # make a nested function in order to call it multiple times
        # allows the user to scroll as many times as wanted during test
        def scroll_down(elem, num):
            for _ in range(num):
                time.sleep(.01)
                elem.send_keys(Keys.PAGE_DOWN)

        # wait time between each scroll down - can be modified, counted in seconds
        scroll_pause_time = 0.3
        body = self.driver.find_element(By.XPATH, "/html/body")

        # get the initial scroll value
        initial_scroll_value = body.get_attribute("scrollHeight")

        prev_height = initial_scroll_value
        # range to be able to tell how many scrolls would be performed
        for i in range(10):
            scroll_down(body, 1)
            time.sleep(scroll_pause_time)

            current_height = body.get_attribute("scrollHeight")
            # Check if scrollable space got larger
            if current_height == prev_height:
                break
            prev_height = current_height

        # get a final value and print for comparison reasons
        final_scroll_value = body.get_attribute("scrollHeight")
        print(f"Initial Value : {initial_scroll_value} and Final Value : {final_scroll_value}")


if __name__ == "__main__":
    unittest.main()
