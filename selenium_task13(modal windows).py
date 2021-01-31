import os
import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(link)

    form_action = browser.find_element_by_class_name('btn-primary').click()

    # accept allert
    alert = browser.switch_to.alert.accept()
    time.sleep(1)

    # next page
    num = browser.find_element_by_id('input_value').text
    res = calc(num)

    browser.find_element_by_id('answer').send_keys(res)
    browser.find_element_by_tag_name('button[type="submit"]').click()


finally:
    time.sleep(10)
    browser.quit()
