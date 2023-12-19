from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import requests


### Test will pass if there are no broken images on the tester URL
### This specific test is FAILING and printing the broken images in the report.

class BrokenImages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.set_window_size(1250, 850)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_broken_images(self):
        self.driver.find_element(By.LINK_TEXT, "Broken Images").click()
        image_list = self.driver.find_elements(By.TAG_NAME, "img")
        # set broken image count value to 0, easy to increment during the test
        self.broken_image_count = 0
        # get the number of broken images from len of image_list
        print(' Total number of images on are ' + str(len(image_list)))

        for img in image_list:
            try:
                # use 'src' attribute that is mandatory for any media file.
                # 'src' - > refers to the URL of the media file, can be used for videos also
                response = requests.get(img.get_attribute('src'), stream=True)

                # use status response code 200 -> indicates that the request has succeeded
                if response.status_code != 200:
                    # getting the outerHTML
                    # outerHTML -> attribute of the Element DOM that gets the serialized HTML describing the element
                    print(img.get_attribute('outerHTML') + " is broken.")
                    self.broken_image_count += 1
            except requests.exceptions.MissingSchema:
                # MissingSchema - occurs when the complete URL is not provide
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                # InvalidSchema - no connection adapters were found. Has 3 main reasons to occur
                # 1. -> passing a value that is not a string in the request.get()
                # 2. -> forgetting the protocol scheme in the URL i.e. HTTP:// or HTTPS://
                # 3. -> URL contains invalid characters.
                print("Encountered InvalidSchema Exception")
            except Exception as e:
                # IF errors returned by site are not invalid/missing schema print them
                print(f"Encountered Some other Exception: {str(e)}")

        self.assertEqual(self.broken_image_count, 0, f'The page has {self.broken_image_count} broken images')


if __name__ == "__main__":
    unittest.main()
