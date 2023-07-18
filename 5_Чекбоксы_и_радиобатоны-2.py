from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу https://suninjuly.github.io/math.html
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group #input_value")
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer").send_keys(y)
    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()
    # Нажать на кнопку Submit
    Submit = browser.find_element(By.CSS_SELECTOR, ".container button.btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

