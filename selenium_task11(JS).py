# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script('document.title="Script executing";')
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id('input_value').text

    input_element = browser.find_element_by_id('answer').send_keys(calc(x))

    btn = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView();", btn)
    # browser.execute_script("window.scrollBy(0, 350);")

    radiobutton = browser.find_element_by_id('robotsRule').click()

    checkbox = browser.find_element_by_id('robotCheckbox').click()

    btn.click()


finally:
    time.sleep(10)
    browser.quit()
