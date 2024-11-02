# import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate a Chrome options object
options = webdriver.ChromeOptions()

# Set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# Initialize an instance of the Chrome driver (browser) in headless mode
driver = webdriver.Chrome(options=options)

try:
    # Visit your target site
    driver.get("https://eatsmart.housing.illinois.edu/NetNutrition/46")

    # Wait for the dining hall link to be present
    dining_hall_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-primary"))
    )

    # Extract the href attribute
    product_data = {
        "dining_hall": dining_hall_element.get_attribute("href"),
    }

    # Print the extracted data
    print(product_data)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release the resources allocated by Selenium and shut down the browser
    driver.quit()
