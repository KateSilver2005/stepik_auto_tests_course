from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()