from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # Принять confirm
    browser.switch_to.alert.accept()
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()