from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver =webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
ele=driver.find_element(By.ID,"msdd")
ele.click()

options = driver.find_elements(By.XPATH,"//multi-select//li/a")


list2=['Turkish','Ukrainian','Urdu','Vietnamese']
for i in options:
    if i.text in list2:
        i.click()

input()