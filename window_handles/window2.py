from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
url="https://demo.automationtesting.in/Register.html"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
switch_to_element=driver.find_element(By.XPATH,'//ul/li/a[text()="SwitchTo"]')
action.move_to_element(switch_to_element)
action.key_down(Keys.ARROW_DOWN).perform()
action.key_down(Keys.ARROW_DOWN).perform()
# action.key_down()
action.key_down(Keys.ENTER).perform()

input("Enter to Close Browser")