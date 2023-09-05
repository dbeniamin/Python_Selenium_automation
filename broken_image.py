import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
 
URL = "https://the-internet.herokuapp.com/broken_images"
broken_image_count = 0
# defining broken image count to have a starting value
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

driver.get(URL)
 
image_list = driver.find_elements(By.TAG_NAME, "img") #almost all images have the tag name img - easy to find 
print('Total number of images on '+ URL + ' are ' + str(len(image_list))) # getting a total number of html elements with img tag
 
for img in image_list:
    try:
        response = requests.get(img.get_attribute('src'), stream=True)
        if (response.status_code != 200):                              # getting a response for each loaded element
            print(img.get_attribute('outerHTML') + " is broken.")
            broken_image_count = (broken_image_count + 1)
 
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other Exception")
 
driver.quit()
 
print('The page ' + URL + ' has ' + str(broken_image_count) + ' broken images')  #printing results for that specific page