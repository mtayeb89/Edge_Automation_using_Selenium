# Edge_Automation_using_Selenium
This script demonstrates how to automate Microsoft Edge using Selenium in Python.
# Microsoft Edge Automation Script using Selenium
# Overview

This script demonstrates how to automate Microsoft Edge using Selenium in Python. The script opens Microsoft Edge, navigates to Google, performs a search, and then keeps the browser open for manual inspection.

# Requirements

    Python 3.x
    Selenium package (pip install selenium)
    Microsoft Edge WebDriver compatible with your version of Edge. You can download it from here.

# How It Works
# Code Explanation:
    Imports:
        webdriver from selenium: To control the browser.
        By from selenium.webdriver.common.by: To locate elements on the web page.
        Keys from selenium.webdriver.common.keys: To simulate keyboard actions like hitting the Enter key.

    Initialize the WebDriver:
        driver = webdriver.Edge(): This initializes the Edge WebDriver. Ensure the msedgedriver executable is in your system's PATH or provide its path explicitly.

    Open a Website:
        driver.get("https://www.google.com"): Opens the Google homepage.

    Find the Search Box:
        search_box = driver.find_element(By.NAME, "q"): Finds the search box element on Google’s homepage using the name attribute.

    Perform a Search:
        search_box.send_keys("OpenAI"): Types "OpenAI" into the search box.
        search_box.send_keys(Keys.RETURN): Simulates pressing the Enter key to start the search.

    Wait for Results:
        driver.implicitly_wait(5): Waits for 5 seconds to allow the search results to load.

    Keep Browser Open:
        input("Press Enter to close the browser..."): Pauses the script, keeping the browser open until the user presses Enter.

    Close the Browser Window:
        driver.close(): Closes the current browser window. Note that this does not quit the WebDriver session if other windows are open.

# Running the Script

    Ensure you have all the requirements installed.
    Run the script using Python: python your_script_name.py
    Interact with the browser manually if needed, and close it by pressing Enter.

# Notes

    The driver.quit() command, which closes all windows and ends the WebDriver session, was intentionally omitted to allow manual browser interaction.
    Use driver.close() to close only the current window if you need to keep the session active.
