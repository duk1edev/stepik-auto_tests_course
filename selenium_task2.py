import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = 'http://suninjuly.github.io/simple_form_find_task.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID,'submit_bfdfdfutton')
    button.click()
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()

