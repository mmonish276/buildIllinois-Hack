from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException

# Set the path to the Chromedriver
DRIVER_PATH = 'C:\\Users\\adamo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get('https://eatsmart.housing.illinois.edu/NetNutrition/46')

# Variables
macrosFull = []

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

# Initial Navigation
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

# Loop to gather data
for i in range(27):
    for k in range(2):
        refresh()
        links = currBlocks[i].find_elements(By.CLASS_NAME, 'cbo_nn_menuLink')
        driver.execute_script("arguments[0].scrollIntoView();", links[k])
        driver.execute_script("arguments[0].click();", links[k])

        try:
            dropdowns = WebDriverWait(driver, 2).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'js-collapse-icon.pl-2.fa.fa-caret-right'))
            )
            for dropdown in dropdowns:
                driver.execute_script("arguments[0].scrollIntoView();", dropdown)
                driver.execute_script("arguments[0].click();", dropdown)
                time.sleep(1)
        except:
            pass

        items = WebDriverWait(driver, 1).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'cbo_nn_itemHover'))
        )

        for item in items:
            driver.execute_script("arguments[0].scrollIntoView();", item)
            driver.execute_script("arguments[0].click();", item)
            time.sleep(0.5)

            try:
                table = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="nutritionLabel"]/div/div/table'))
                )

                # Re-fetch `macrosFull` every time to avoid stale elements
                headers = table.find_elements(By.CLASS_NAME, 'cbo_nn_LabelBorderedSubHeader')
                headers.append(driver.find_element(By.CLASS_NAME, 'cbo_nn_LabelHeader'))
                headers.append(driver.find_element(By.CLASS_NAME, 'cbo_nn_LabelBottomBorderLabel'))

                for header in headers:
                    try:
                        print(header.text)
                    except StaleElementReferenceException:
                        # Retry fetching text if stale
                        print("Stale element, retrying fetch...")
                        header = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.CLASS_NAME, header.get_attribute("class")))
                        )
                        print(header.text)

            except StaleElementReferenceException:
                print("Table elements became stale. Skipping this item.")

            close = WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located((By.ID, 'btn_nn_nutrition_close'))
            )
            driver.execute_script("arguments[0].scrollIntoView();", close)
            driver.execute_script("arguments[0].click();", close)
            time.sleep(1)
        
        back = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.ID, 'btn_Back*Menu Item Details'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", back)
        driver.execute_script("arguments[0].click();", back)

driver.quit()
