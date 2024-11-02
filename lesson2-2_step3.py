from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = num1_element.text
    num2 = num2_element.text
    summ = int(num1) + int(num2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summ))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()