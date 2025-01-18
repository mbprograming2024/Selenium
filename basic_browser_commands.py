# from selenium import webdriver

# driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# print("title = ",driver.title)

# print("current_url = ",driver.current_url)
# print("current_window_handle = ",driver.current_window_handle)


#######################################################################################################
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
driver.get("https://www.selenium.dev/selenium/web/index.html")
print(driver.title)
driver.back()
print("after pressing backword")
print(driver.title)
driver.forward()
print("after pressing forword")
print(driver.title)

driver.refresh() 


