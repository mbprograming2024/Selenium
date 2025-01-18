from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")

element = driver.find_element(By.XPATH,'//*[@id="Skills"]')

dropdown=Select(element)
dropdown.select_by_index(5)

all_options= dropdown.options
for c in all_options:
    print(c.text)
input()