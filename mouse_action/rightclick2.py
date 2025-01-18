from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click_menu_list_xpath = '//p/span[contains(text(),"right click me")]'

element = driver.find_element(By.XPATH,right_click_menu_list_xpath)

action = ActionChains(driver)
action.context_click(element).perform()

menu_options = driver.find_elements(By.XPATH,"//*[@class='context-menu-list context-menu-root']/li")

for option in menu_options:
        print(option.text)

input("done")

# context-menu-one btn btn-neutral context-menu-active