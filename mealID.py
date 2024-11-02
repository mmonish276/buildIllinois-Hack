from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta


elementCount = 0
scrollHeight = 300
visible_elements = []
todayDate = datetime.now()
today = datetime.now().strftime("%A, %B%e, %Y")
print(today)

def element_exists(driver, by, value):
    try:
        elements = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located(by, value)
        )
        if(elements != None):
            return True
    except:
        return False
      # Returns True if the element exists, otherwise False





# Set the path to the Chromedriver
DRIVER_PATH = 'C:\\Users\\adamo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

service = Service(DRIVER_PATH)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get('https://eatsmart.housing.illinois.edu/NetNutrition/46')


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

driver.execute_script(f"window.scrollTo(0, {scrollHeight});")


while True:
    try:
        # Wait for the date header to appear
        element = WebDriverWait(driver, 0.5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, f"//*[contains(text(), '{today}')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)


        # Get the date header and the corresponding "Lunch" element
        lunch = driver.find_element(By.XPATH, f"//header[contains(text(), '{today}')]/following::a[contains(text(), 'Lunch')]")
        
        # Process the found element (increment count or log info)
        elementCount += 1  
        print(f"Found 'Lunch' for {today}")

        # Move to the next day
        todayDate += timedelta(days = 1)
        today = todayDate.strftime("%A, %B%e, %Y")  # Update 'today' variable for next loop
        
    except:
        # Scroll down and try again if the element isn't found yet
        scrollHeight += 400
        driver.execute_script(f"window.scrollTo(0, {scrollHeight});")
        
        if scrollHeight > 6200:
            print(f"No more 'Lunch' elements found for {today}. Stopping.")
            break  # Exit if max scroll is reached
        

print(elementCount)
print(len(visible_elements))

# It's a good practice to close the browser when done
driver.quit()



