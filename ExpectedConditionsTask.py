from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    x_variable = browser.find_element_by_id("input_value").text
    result = str(math.log(abs(12*math.sin(int(x_variable)))))

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(result)

    submit_button = browser.find_element_by_id("solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
