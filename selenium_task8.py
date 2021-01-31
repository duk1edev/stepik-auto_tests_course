from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_elements_by_id('input_value')
    x = int(x_element[0].text)
    y = calc(x)

    # send to input
    input_element = browser.find_element_by_id('answer').send_keys(y)

    # find checkbox robot
    robot_checkbox = browser.find_element_by_id('robotCheckbox').click()

    # find radio robot
    robot_radio = browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_class_name('btn').click()



finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
