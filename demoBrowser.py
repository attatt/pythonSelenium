from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")

driver.get("https://google.com")

print(driver.title)

driver.quit()