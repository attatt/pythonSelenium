from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("http://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

parentWindow = driver.window_handles[0]
childWindow = driver.window_handles[1]

print(childWindow)
driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()


driver.switch_to.window(parentWindow)
assert driver.find_element_by_tag_name("h3").text == "Opening a new window"