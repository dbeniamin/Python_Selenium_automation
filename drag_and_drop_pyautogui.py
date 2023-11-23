from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
### driver.maximize_window()   - can work in full screen mode but it will look a bit off center when drag and dropping the items ###
driver.implicitly_wait(10)

# set the win size to keep the same aspect and not be related to any machine you run this on
# set size is measured in pixels
driver.set_window_size(1200, 600)

# use only to check if the win size was correctly set
win_size = driver.get_window_size()

source = driver.find_element(By.CSS_SELECTOR, "#column-a")
target = driver.find_element(By.CSS_SELECTOR, "#column-b")
# get the size of the element to be dragged
# not actually required but is a personal preference to make it more fancy and make sure the drag / drop action starts from the middle of the element
element_size = source.size

# get the location of elements in pixels
source_location = source.location
target_location = target.location

# required to get because the location of elements does not take in consideration the address bar, bookmark bar ie"the browser is controled by automated etc..." and the specific window size
inner_width = driver.execute_script("return window.innerWidth;")
inner_height = driver.execute_script("return window.innerHeight;")

# get the offset and middle of the element to be dragged and the target
offset_width = win_size['width'] - inner_width + element_size['width'] / 2
offset_height = win_size['height'] - inner_height + element_size['height'] / 2

# ### Print Statememts used for Debbug ###
# print(f"actual size is {win_size} ,ineer size is {inner_width}, {inner_height}")
# print(source_location, target_location)
# print(element_size, f"the offsets are {offset_width} and {offset_height}")

# use pyautoguy to perform the actions 
# make the actual start location by adding element .location value with the offests that are calculated for Chrome
pyautogui.moveTo(source_location['x'] + offset_width, source_location['y'] + offset_height)
pyautogui.mouseDown()

# adjust duration for a faster or slower animation for drag and drop based on preference
pyautogui.moveTo(target_location['x'] + offset_width, target_location['y'] + offset_height, duration=3)
pyautogui.mouseUp()

# ###  Assertion to check in case you dont wanna look and just run the test ###
# ###  Find the moved item, get the new location  ###
# ###  Assert that initial location and location after move are not the same => Drag and Drop action is a success  ###
# source_moved = driver.find_element(By.XPATH, '//div[@class="column"]/header[text()="A"]')
# source_newlocation = source_moved.location
# assert source_location != source_newlocation

# add a sleep time to enjoy the fruits of the work
time.sleep(1)

driver.quit()
