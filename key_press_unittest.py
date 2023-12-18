from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
### import time
# -> use time.sleep if you want to see the results or the action itself and for debug reasons don't keep it on
# not recommended to use since it's a hard value and the driver will wait that specific amount even if everything
# loaded and the desired elements are located.


class TestKeyPress(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_key_pressing(self):
        self.driver.find_element(By.LINK_TEXT, "Key Presses").click()
        # you can choose any key to send on the page ( not only special keys ).
        # make sure you adjust the assertion values for the keys you chose.
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        action_status_message = self.driver.find_element(By.ID, 'result')
        # use any keys you want to send to the field, the page can take input from keys without focusing on the field
        # itself, by doing so you can speed it up and remove the find field and click field steps
        self.assertEqual("You entered: SPACE", action_status_message.text)
        ### time.sleep(2)

        # sending regular keys does not require the use of Keys class
        # regular keys can be sent using string argument for send_keys
        ActionChains(self.driver).send_keys("b").perform()
        self.assertEqual("You entered: B", action_status_message.text)

        ### time.sleep(2)


if __name__ == "__main__":
    unittest.main()
