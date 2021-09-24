from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") # accepts frame id, frame name, or index value
driver.find_element_by_css_selector("#tinymce").click()
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am automating")


driver.switch_to.default_content()
assert driver.find_element_by_tag_name("h3").text