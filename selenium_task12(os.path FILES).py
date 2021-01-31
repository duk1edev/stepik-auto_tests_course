import os
import time
from selenium import webdriver

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)

    browser.find_element_by_tag_name('input[name="firstname"]').send_keys('Haha')
    browser.find_element_by_tag_name('input[name="lastname"]').send_keys('Ohohoh')
    browser.find_element_by_tag_name('input[name="email"]').send_keys('Ohohoh@asdsad.ewr')

    file_path = os.path.abspath(os.path.abspath('task12.txt'))
    browser.find_element_by_id('file').send_keys(file_path)

    btn = browser.find_element_by_class_name('btn').click()


finally:
    time.sleep(10)
    browser.quit()
