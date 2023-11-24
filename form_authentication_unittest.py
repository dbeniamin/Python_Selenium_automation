from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time 


class TestFormAuthentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1000, 750)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_form_authentication_login(self):
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login > button").click()
        login_message = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h4')

        self.assertEqual(login_message.text, "Welcome to the Secure Area. When you are done click logout below.")
       
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()

