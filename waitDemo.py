import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/attilacseh/selenium/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.implicitly_wait(5)
# wait for up to 5 seconds if object is not displayed. if object is loaded before that, no longer wait. max wait is x seconds
# global
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)


# driver.quit()


# implicit wait
# explicit wait
# pause for a few seconds using Time