from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))
dead_links=[]
for link in links:
    url=link.get_attribute('href')
    # print(url)
    # print(f"{url}:::{response.status_code}")
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)  # Use HEAD request for efficiency
        if response.status_code != 200:
            print(f"Dead link found: {url} (Status Code: {response.status_code})")
            dead_links.append((url, response.status_code))
        else:
            print(f"Valid link: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error with link: {url} ({e})")
        dead_links.append((url, str(e)))
print(f"Number of Broken Link{len(dead_links)}")

