from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
new_url='https://intellipaat.com/blog/tutorial/selenium-tutorial/selenium-cheat-sheet/'
driver.execute_script(f"window.open('{new_url}','_blank')")

input("Done")













# new_url="https://intellipaat.com/blog/tutorial/selenium-tutorial/selenium-cheat-sheet/"
# driver.execute_script(f"window.open('{new_url}','_blank');")
# input("Done")