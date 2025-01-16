# driver url 
# chrome = https://googlechromelabs.github.io/chrome-for-testing/#stable



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service)
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#################################################################################################
# - - - - - - - - - - - - - - - - - - -  - - -  - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -
# initialize driver using local driver path

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# # Specify the path to chromedriver executable
# chromedriver_path = "/home/mayurbaviskar/Study/mbprograming/selenium/driver/chromedriver"  # Replace this with the actual path

# # Create the Service object
# service = Service(chromedriver_path)

# # Initialize the WebDriver with the service
# driver = webdriver.Chrome(service=service)

# # Open a URL
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")


##################################################################

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# # Automatically manage chromedriver and ensure it is available
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # Open a URL
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#######################################################################

# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

# # Automatically download and install GeckoDriver
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# # Open a URL
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")


####################################################################################

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options

# options = Options()
# options.add_argument("-profile")
# options.add_argument("/home/mayurbaviskar/snap/firefox/common/.mozilla/firefox/0nnqsujr.mayur22kar")

# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service, options=options)

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")


