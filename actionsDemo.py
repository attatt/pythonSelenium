from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

action.context_click(driver.find_element_by_id("double-click")).perform()  # right click
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()

driver.close()