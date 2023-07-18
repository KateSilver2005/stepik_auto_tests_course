from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(attribute):
  return str(math.log(abs(12*math.sin(int(attribute)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    img = browser.find_element(By.ID, 'treasure')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    attribute = img.get_attribute("valuex")
    # Посчитать математическую функцию от x (сама функция остаётся неизменной)
    answer = calc(attribute)
    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer").send_keys(answer)
    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule").click()
    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, ".container button.btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
