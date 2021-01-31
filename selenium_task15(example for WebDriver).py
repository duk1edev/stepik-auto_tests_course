import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.find_element_by_id("button")

# browser.implicitly_wait(5)
# time.sleep(2)
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")

assert "successful" in message.text