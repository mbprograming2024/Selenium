from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")

# print(driver.title)

# assert driver.title=='Drag and Drop' 

action=ActionChains(driver)

interation_element = driver.find_element(By.XPATH,'//ul/li/a[contains(text(),"Interactions")]')


action.move_to_element(interation_element)
action.key_down(Keys.ARROW_DOWN).perform()
time.sleep(20)
static_element = driver.find_element(By.XPATH,"//*[contains(text(),'Static')]")
time.sleep(20)
action.move_to_element(static_element).perform()
static_element.click()
# action.key_down(Keys.ENTER).perform()
# time.sleep(20)
source = driver.find_element(By.ID,'angular')
target = driver.find_element(By.CLASS_NAME,'dragged')
source2 = driver.find_element(By.ID,'mongo')
action.drag_and_drop(source,target).perform()
action.drag_and_drop(source2,target).perform()

input("success")