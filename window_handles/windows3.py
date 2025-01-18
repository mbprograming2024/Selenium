# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def open_and_handle_two_windows():
#     # Initialize the WebDriver
#     driver = webdriver.Chrome()

#     try:
#         # Open the first URL
#         driver.get("https://www.google.com/")
#         print(f"First Window Title: {driver.title}")

#         # Get the handle of the first window
#         first_window = driver.current_window_handle

#         # Open the second URL in a new window
#         driver.execute_script("window.open('https://www.facebook.com/login/', '_blank');")

#         # Wait for the new window to open
#         time.sleep(2)

#         # Get all window handles
#         all_windows = driver.window_handles

#         # Identify the second window handle
#         second_window = [window for window in all_windows if window != first_window][0]

#         # Switch to the second window
#         driver.switch_to.window(second_window)
#         print(f"Second Window Title: {driver.title}")

#         # Close the second window
#         driver.close()
#         print("Closed Second Window")

#         # Switch back to the first window
#         driver.switch_to.window(first_window)
#         print(f"Back to First Window Title: {driver.title}")

#         # Close the first window
#         driver.close()
#         print("Closed First Window")
#     finally:
#         # Quit the driver to clean up resources
#         # driver.quit()
#         input()

# # Call the function
# open_and_handle_two_windows()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def handle_multiple_windows_without_js():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the initial webpage
        driver.get("https://demo.automationtesting.in/Windows.html")
        driver.maximize_window()

        # Locate and click on a button or link that opens a new window
        driver.find_element(By.XPATH, "//a[contains(text(),'Open New Seperate Windows')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'click')]").click()

        # Wait for the new window to load
        time.sleep(2)

        # Get all window handles
        all_windows = driver.window_handles
        print(f"All Window Handles: {all_windows}")

        # Switch to the second window (index 1)
        driver.switch_to.window(all_windows[1])
        print(f"Switched to Second Window: {driver.current_url}")
        time.sleep(2)

        # Close the second window
        driver.close()
        print("Closed the Second Window")

        # Switch back to the first window (index 0)
        driver.switch_to.window(all_windows[0])
        print(f"Switched back to First Window: {driver.current_url}")
    finally:
        # Close the browser
        # driver.quit()
        input()

# Call the function
handle_multiple_windows_without_js()
