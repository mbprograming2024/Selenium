from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")


links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
dead_links=[]
for link in links:
    url=link.get_attribute("href")
    if url:
        # print(url)
        response = requests.head(url,allow_redirects=True,timeout=5)
        # print(f"{url}={response.status_code}")
        if response.status_code != 200:
            print(f"valid {url}")
        else:
            dead_links.append(url)
        # except:
print(f"number of dead links : {dead_links}")
input("check all links successfully")

