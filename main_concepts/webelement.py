from selenium import webdriver
from selenium.webdriver.common.by import By
 

url="http://practice.automationtesting.in/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

def navigation_menu(ele):
    element = "//li/a[text()='"+ele+"']"
    menu_element=driver.find_element(By.XPATH,element)
    menu_element.click()

def Login_to_automation_testing(username1,password1):
    username = '//input[@id="username"]'
    passwd   = '//*[@id="password"]'
    loginbtn = '//*[@name="login"]'
    username_box = driver.find_element(By.XPATH,username)
    username_box.send_keys(username1)
    passwd_box = driver.find_element(By.XPATH,passwd)
    passwd_box.send_keys(password1)
    login_btn = driver.find_element(By.XPATH,loginbtn)
    print(login_btn.is_displayed())
    print(login_btn.is_enabled())
    login_btn.click()



navigation_menu('My Account')
Login_to_automation_testing("mayur","baviskar")

input()
