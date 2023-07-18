from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book").click()
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit) #принудительно скроллим страницу до нужного элемента
    submit.click()


finally:
    #переключаемся на окно alert, берем оттуда текст и выводим его на экран консоли
    alert = browser.switch_to.alert
    print(browser.switch_to.alert.text)
    time.sleep(5)
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()

