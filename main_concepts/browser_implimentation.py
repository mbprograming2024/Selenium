from selenium import webdriver

url="http://practice.automationtesting.in/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()


