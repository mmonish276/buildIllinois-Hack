from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set the path to the Chromedriver
DRIVER_PATH = 'C:\\Users\\adamo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

service = Service(DRIVER_PATH)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get('https://eatsmart.housing.illinois.edu/NetNutrition/46')

time.sleep(3)
element = driver.find_element(by = By.LINK_TEXT, value = 'Illinois Street Dining Center (ISR)')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)

time.sleep(3)
element = driver.find_element(by = By.LINK_TEXT, value = 'Fusion 48')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)

time.sleep(3)
element = driver.find_element(by = By.XPATH, value = '//*[@id="cbo_nn_menuDataList"]/div/div[1]/section/div/div/div[1]/a')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)

time.sleep(5)

# It's a good practice to close the browser when done
driver.quit()