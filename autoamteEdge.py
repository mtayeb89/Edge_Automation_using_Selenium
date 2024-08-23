from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Intitialize the WebDriver
driver=webdriver.Edge()

# open a website
driver.get("https://www.google.com")

# Find the search box element using the updated method
searchbox=driver.find_element(By.NAME,"q")

# Type something into the search box
searchbox.send_keys("mp3 Quran")

# Simulate hitting the enter key
searchbox.send_keys(Keys.RETURN)

# Wait for a few seconds to see the result (optional)
driver.implicitly_wait(3)


# Keep the browser open to interact with it manually
input("Press Enter to close the browser...")

driver.quit()
