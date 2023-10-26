from selenium import webdriver
from selenium.webdriver.common.by import By

# even if the elements are in the same parent class they have diffrent attributes that allow the user to find out witch element is the one that will get shifted

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/shifting_content/menu")
# driver.maximize_window()

try:
    driver.implicitly_wait(10)

    # Find the element you want to check
    element = driver.find_element(By.CSS_SELECTOR, ".shift")

    # get the location x , y of the element you want
    first_x = element.location['x']
    first_y = element.location['y']

    # refresh the page
    driver.refresh()

    # wait for all elements to load - max time can be adjusted
    driver.implicitly_wait(10)
    

    # define a variable with new locations of the same element
    reloaded_element = driver.find_element(By.CSS_SELECTOR, ".shift")

    # get location of the variable newlly defined.
    second_x = reloaded_element.location['x']
    second_y = reloaded_element.location['y']

    # compare and print initial location versul target location.
    if (first_x, first_y) != (second_x, second_y):
        print("The element has shifted from its initial position.")
        print(f"Initial coordinates: ({first_x}, {first_y})")
        print(f"Coordinates after refresh: ({second_x}, {second_y})")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()
