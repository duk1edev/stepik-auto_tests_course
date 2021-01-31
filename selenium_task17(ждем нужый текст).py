import math

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), "100")
)
btn_book = browser.find_element_by_id('book')
btn_book.click()

btn_solve = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView();", btn_solve)

x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))
btn_solve.click()
#
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text
