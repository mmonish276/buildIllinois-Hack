from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the Chromedriver
DRIVER_PATH = 'C:\\Users\\adamo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

service = Service(DRIVER_PATH)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get('https://eatsmart.housing.illinois.edu/NetNutrition/46')

# It's a good practice to close the browser when done
driver.quit()