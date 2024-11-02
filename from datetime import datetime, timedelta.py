from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
# Set the path to the Chromedriver
DRIVER_PATH = 'C:\\Users\\adamo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
service = Service(DRIVER_PATH)
# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)
# Navigate to the URL
driver.get('https://eatsmart.housing.illinois.edu/NetNutrition/46')

#Variables





def refresh():
    global elements, rows, currBlocks, links
    elements = WebDriverWait(driver, 1).until(
    EC.visibility_of_all_elements_located((By.ID, 'menuPanel'))
)
    for element in elements:
        rows = element.find_elements(By.CLASS_NAME, 'MenuList')
        for row in rows:
            currBlocks = row.find_elements(By.CLASS_NAME, 'col-12')
            for block in currBlocks:
                links = block.find_elements(By.CLASS_NAME, 'cbo_nn_menuLink')
    
    

    










element = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.LINK_TEXT, 'Illinois Street Dining Center (ISR)'))
)
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)


element = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.LINK_TEXT, 'Fusion 48'))
)
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)

for i in range(27):
    for k in range(2):
        refresh()
        links = currBlocks[i].find_elements(By.CLASS_NAME, 'cbo_nn_menuLink')
        driver.execute_script("arguments[0].scrollIntoView();", links[k])
        driver.execute_script("arguments[0].click();", links[k])
        back = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.ID, 'btn_Back*Menu Item Details'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", back)
        driver.execute_script("arguments[0].click();", back)




                



driver.quit()


