from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    # Открыть страницу https://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser.get(link)

    # Считать значение для переменной x.
    x_text = (browser.find_element(By.ID, "input_value")).text
    x = int(x_text)

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Проскроллить страницу вниз.
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    # Ввести ответ в текстовое поле.
    answer.send_keys(y)

    # Выбрать checkbox "I'm the robot".
    browser.find_element(By.ID, "robotCheckbox").click()

    # Переключить radiobutton "Robots rule!".
    browser.find_element(By.ID, "robotsRule").click()

    # Нажать на кнопку "Submit".
    browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

