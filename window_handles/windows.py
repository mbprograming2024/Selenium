# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Windows.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a/button[contains(text(),'click')]").click()
# a=driver.title
# print("Title=",a)
# handle = driver.current_window_handle
# print(handle)
# handles = driver.window_handles
# print(handles)

# for x in handles:
#     if handle != x:
#         driver.switch_to.window(x)
#         b=driver.title
#         print("Title=",b)

# driver.switch_to.window(handle)
# c=driver.title
# print("Title=",c)
# # driver.switch_to.new_window('tab')
# # b=driver.title
# # print("Title=",b)
# # handles = driver.window_handles
# # print(handles)
# # driver.switch_to.window(1)
# # 
# input()