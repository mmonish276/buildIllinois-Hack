from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate a Chrome options object
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Run in headless mode

# Initialize an instance of the Chrome driver (browser)
driver = webdriver.Chrome(options=options)

try:
    # Visit your target site
    driver.get("https://eatsmart.housing.illinois.edu/NetNutrition/46")
    
    # Print the page title for debugging
    print("Page title:", driver.title)

    # Wait for the dining hall link to be present
    dining_hall_elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "text-primary"))
    )

    # Extract the names and links of the dining halls
    product_data = []
    for element in dining_hall_elements:
        title = element.get_attribute("title")  # Get the title attribute
        product_data.append({"dining_hall_name": title})

    # Print the extracted data
    for data in product_data:
        print(data)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release the resources allocated by Selenium and shut down the browser
    driver.quit()
