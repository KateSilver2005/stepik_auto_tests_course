from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    # Открыть страницу https://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    number1 = browser.find_element(By.ID, "num1")
    value_number1 = number1.text
    number2 = browser.find_element(By.ID, "num2")
    value_number2 = number2.text
    sum = str(int(value_number1) + int(value_number2))
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(sum)
    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()