from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Пройти капчу для робота и получить число-ответ
    x_text = browser.find_element(By.ID, "input_value").text
    x = int(x_text)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(1)
    print(browser.switch_to.alert.text)
browser.quit()