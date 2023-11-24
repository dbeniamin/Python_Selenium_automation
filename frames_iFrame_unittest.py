from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time 


class TestFramesiFrame(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()

    def test_frames_iFrame(self):

        self.driver.find_element(By.LINK_TEXT, "Frames").click()
        self.driver.find_element(By.LINK_TEXT, "iFrame").click()

        iframe = self.driver.find_element(By.TAG_NAME, "iframe")
            # switch to the iFrame after page loades
        self.driver.switch_to.frame(iframe)
      
            # find the element within the iframe using the text
        edit_box = self.driver.find_element(By.XPATH, "//*[text()='Your content goes here.']")
        
        edit_box.send_keys(Keys.CONTROL,'a')
        edit_box.send_keys(Keys.BACKSPACE)
        time.sleep(1)
            # find the updated element 
            ### using the same method but with empty string does not work  ###
        updated_edit_box = self.driver.find_element(By.XPATH, '//*[@id="tinymce"]')
            ### send the test text ###
        updated_edit_box.send_keys("This is an Automated Test !!")
        updated_edit_box.send_keys(Keys.CONTROL,'a')
        updated_edit_box.send_keys(Keys.CONTROL,'b')
        updated_edit_box.click()

        # time.sleep(1)

if __name__ == "__main__":
    unittest.main()

