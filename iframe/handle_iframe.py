from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.w3schools.com/jsreF/tryit.asp?filename=tryjsref_iframe_contentdocument")
driver.maximize_window()
print(driver.title)

iframe = driver.find_element(By.XPATH,"//html/iframe[2]")
iframe_html = iframe.get_attribute("outerHTML")
print("Iframe HTML Source Code:")
print(iframe_html)

driver.switch_to.frame("iframeResult")

# Optionally, print the inner content of the iframe
inner_html = driver.execute_script("return document.body.outerHTML;")
print("Iframe Inner Content:")
print(inner_html)

# goto next inner iframe
driver.switch_to.frame("myframe")
innerhtml2=driver.execute_script("return document.body.outerHTML;")
print(f"iframe inner :{innerhtml2}")

ele = driver.find_element(By.TAG_NAME,"p")
print(ele.text)


# go back to parent iframe
driver.switch_to.parent_frame()
inner_html_back = driver.execute_script("return document.body.outerHTML;")
print(f"inner_html_back:{inner_html_back}")



# go back to main iframe
# driver.switch_to.default_content()
# inner_html_back = driver.execute_script("return document.body.outerHTML;")
# print(f"inner_html_back:{inner_html_back}")
input("done")