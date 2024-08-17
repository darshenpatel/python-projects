import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a URL
driver.get('https://google.com')

try:
    # Wait for the title to be available and print it
    WebDriverWait(driver, 20).until(EC.title_is("Google Domain"))
    print(driver.title)
finally:
    driver.quit()