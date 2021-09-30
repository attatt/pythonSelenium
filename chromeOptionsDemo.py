from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # ability to add Chrome options (to control browser)
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
# More example: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver", options=chrome_options)  # initializing webdriver, with options

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
