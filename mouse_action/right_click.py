from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")


driver.implicitly_wait(5)
element = driver.find_element(By.XPATH,"//p/span[text()='right click me']")
action = ActionChains(driver)
action.context_click(element).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(10)
action.send_keys(Keys.ENTER).perform()
time.sleep(10)
text=driver.switch_to.alert.text
print(f"alert text is : {text}")
driver.switch_to.alert.accept()

input("right click is down ")