
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

validateText = "Option3"
confirmValidateText = "Other Text"

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()

#  switching from html content to the alert
alert = driver.switch_to.alert  #create an object to handle the alert
alertText = alert.text

print(alertText)
assert validateText in alertText
alert.accept()

# second popup
driver.find_element_by_css_selector("#name").send_keys(confirmValidateText)
driver.find_element_by_id("confirmbtn").click()

#  switching from html content to the alert (for the other alert popup)
confirm = driver.switch_to.alert  #create an object to handle the alert
confirmText = confirm.text

print(confirmText)
assert confirmValidateText in confirmText
confirm.dismiss()