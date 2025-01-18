# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
# driver.maximize_window()
# element=driver.find_element(By.LINK_TEXT,"See an example alert")
# element.click()

# alert = driver.switch_to.alert
# text=alert.text
# print(text)
# alert.accept()
# input("enter any key to close browser")

# driver.execute_script
# element=driver.find_element(By.LINK_TEXT,"See a sample confirm")
# driver.execute_script("arguments[0].click()",element)

# confirm_box = driver.switch_to.alert
# print(confirm_box.text)
# # confirm_box.accept()

# from selenium.webdriver.support.ui import WebDriverWait


# element = driver.find_element(By.LINK_TEXT, "See a sample prompt")
# driver.execute_script("arguments[0].click();", element)

# wait = WebDriverWait(driver, timeout=2)
# alert = wait.until(lambda d : d.switch_to.alert)
# time.sleep(20)
# alert.send_keys("Selenium")
# time.sleep(20)
# text = alert.text
# alert.accept()
# assert text == "What is your tool of choice?"

# # input("enter any key to close browser")


############################################################################################################
# PRACTICE 2 
############################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = "https://demo.automationtesting.in/Alerts.html"

# driver = webdriver.Chrome()

# driver.get(url)
# driver.maximize_window()

# alert_popup_xpath = '//*[@class="btn btn-danger"]'
# element = driver.find_element(By.XPATH,alert_popup_xpath)
# driver.execute_script("arguments[0].click()",element)
# alert = driver.switch_to.alert
# text = alert.text
# alert.accept()                        
# print(text)
# assert  text == 'I am an alert box!'



# driver.find_element(By.XPATH,'//*[text()="Alert with OK & Cancel "]').click()
# driver.find_element(By.XPATH,'//*[@onclick="confirmbox()"]').click()
# alert = driver.switch_to.alert
# text= alert.text
# print(text)
# # alert.accept()
# alert.dismiss()
# input()

from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_confirm_popup():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//*[contains(text(),'Alert with Textbox')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(),'click the button to demonstrate the prompt box')]").click()
    alert2 = driver.switch_to.alert
    alert2.send_keys("mayur")
    text1=alert2.text
    alert2.accept()
    print(text1)
handle_confirm_popup()
input()



from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_confirm_popup():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()
    
    # Click on "Alert with Textbox"
    driver.find_element(By.XPATH, "//*[contains(text(),'Alert with Textbox')]").click()
    
    # Trigger the prompt alert
    driver.find_element(By.XPATH, "//*[contains(text(),'click the button to demonstrate the prompt box')]").click()
    
    # Switch to the alert
    alert2 = driver.switch_to.alert
    
    # Send text to the prompt alert
    alert2.send_keys("mayur")
    
    # Print the text from the alert
    text1 = alert2.text
    print("Alert Text:", text1)
    
    # Accept the alert
    alert2.accept()

#     # Close the browser
#     # driver.quit()
    input()

handle_confirm_popup()
