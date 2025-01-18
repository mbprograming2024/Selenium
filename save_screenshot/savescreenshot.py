from selenium import webdriver

url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
driver.save_screenshot("/home/mayurbaviskar/Study/mbprograming/selenium/save_screenshot/pic.png")

# driver.s
input("Success")