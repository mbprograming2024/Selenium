from selenium import webdriver
from selenium.webdriver.common.by import By
import time

signup_xpath='//*[@id="email" and @placeholder="Email id for Sign Up"]'
entering_arrow_xpath='//*[@id="enterimg"]'

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")

time.sleep(2)
email_input_box = driver.find_element(By.XPATH,signup_xpath)
email_input_box.send_keys("mayurmayurpbaviskar@gmail.com")
time.sleep(2)
arrow_btn = driver.find_element(By.XPATH,entering_arrow_xpath)
arrow_btn.click()



