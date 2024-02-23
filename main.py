from selenium import webdriver

#to keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# # options.headless = True
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
#
# driver.get("https://www.google.com")





