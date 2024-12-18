from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    field_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field_input)
    field_input.send_keys(y)

    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()