from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("attila")


# customized CSS syntax: tagname[attribute='value']   (tagname is optional)
driver.find_element_by_css_selector("input[name='name']").send_keys("attila - by css")
# Regex: [attribute*='value']
driver.find_element_by_name("email").send_keys("cseh - by name")

driver.find_element_by_id("exampleCheck1").click()

# Select class provides the methods to handle options in a dropdown. Only works if the dropdown uses the 'select' html tag
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value("Male")  # won't work for our dropdwon, as the options do not have value attributes

driver.find_element_by_xpath("//input[@type='submit']").click()
# regex: //*[contains(@class,'alert-success')]

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message


driver.quit()

# driver.close()