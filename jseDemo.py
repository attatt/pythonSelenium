# JS DOM can access any elements on web page, just like how Selenium does
# selenium has a method to execute javascript code in it

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))  # will return the value (in this case what we entered), even if no value was set in the html

print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # executes JS executor

shopButton = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();", shopButton)  # clicks the element using JS executor by firing an html event

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")