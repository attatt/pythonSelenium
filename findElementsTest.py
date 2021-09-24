import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").text)  # this won't bring the new text, because the DOM is already loaded, and wasn't updated
# instead use this:
print(driver.find_element_by_id("autosuggest").get_attribute('value'))

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
