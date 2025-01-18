from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# date = "18-January-2025"
expected_year= '2002'
expected_month= 'March'
expected_date= '09'
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

url='https://demo.automationtesting.in/Register.html'
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
Widgets_xpath  = driver.find_element(By.XPATH,"//ul/li/a[text()='Widgets']")
datepicker_xpath = '//*[@id="datepicker1"]'
datepicker_next_btn_xpath = '//*[@data-handler="next"]'
datepicker_back_btn_xpath = '//*[@data-handler="prev"]'

action=ActionChains(driver)
action.move_to_element(Widgets_xpath).perform()
action.key_down(Keys.ARROW_DOWN).perform()
time.sleep(5)
action.key_down(Keys.ARROW_DOWN).perform()
time.sleep(5)
action.key_down(Keys.ARROW_DOWN).perform()
time.sleep(5)
print("click on datepicker")
action.click().perform()


print("Now start select date")
time.sleep(20)
ele     = driver.find_element(By.XPATH,datepicker_xpath)
ele.click()
month   = driver.find_element(By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(1)')
year    = driver.find_element(By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(2)')

while True:
    if year.text == expected_year:
        current_month_index = months.index(month.text)
        expected_month_index = months.index(expected_month)
        print("current_month_index=",current_month_index)
        print("expected_month_index=",expected_month_index)
        time.sleep(5)
        while True:
            driver.find_element(By.XPATH,'//*[@title="Next"]').click()
            try:
                month = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#ui-datepicker-div > div > div > span:nth-of-type(1)"))
                )
                if month.text == expected_month:
                    date = WebDriverWait(driver,30).until(
                       EC.presence_of_element_located((By.XPATH,'//*[@class="ui-datepicker-calendar"]//tr/td/a'))
                    )
                    date_xpath = '//*[@class="ui-datepicker-calendar"]//tr/td/a[text()='+expected_date+']'
                    driver.find_element(By.XPATH,date_xpath).click()  
                    break
            except Exception as e:
                print(f"Error: {e}")
        break    
    elif year.text < expected_year:
        print(f"{year.text} is less than {expected_year}")
        while True:
            driver.find_element(By.XPATH,datepicker_next_btn_xpath).click()
            try:
                month = WebDriverWait(driver,20).until (
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(1)'))
                    )
                year = WebDriverWait(driver,20).until (
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(2)'))
                    )
                if year.text == expected_year and month.text == expected_month:
                    date = WebDriverWait(driver,30).until(
                       EC.presence_of_element_located((By.XPATH,'//*[@class="ui-datepicker-calendar"]//tr/td/a'))
                    )
                    # print("date is ",date.text)
                    date_xpath = '//*[@class="ui-datepicker-calendar"]//tr/td/a[text()='+expected_date+']'
                    print("date_xpath=",date_xpath)
                    driver.find_element(By.XPATH,date_xpath).click()                     
                    break
            except  Exception as e:
                print(f"error {e}")
        break
    elif year.text > expected_year:
        print(f"{year.text} is greater than {expected_year}")
        while True:
            driver.find_element(By.XPATH,'//*[@title="Prev"]').click()
            try:
                month = WebDriverWait(driver,20).until (
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(1)'))
                    )
                year = WebDriverWait(driver,20).until (
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#ui-datepicker-div > div > div > span:nth-of-type(2)'))
                    )
                if year.text == expected_year and month.text == expected_month:
                    date = WebDriverWait(driver,30).until(
                       EC.presence_of_element_located((By.XPATH,'//*[@class="ui-datepicker-calendar"]//tr/td/a'))
                    )
                    date_xpath = '//*[@class="ui-datepicker-calendar"]//tr/td/a[text()='+expected_date+']'
                    driver.find_element(By.XPATH,date_xpath).click()  
                    break
            except  Exception as e:
                print(f"error {e}")
        break
input("Testing Success")