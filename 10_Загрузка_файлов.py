from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name = 'firstname']").send_keys("Kate")
    last_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name = 'lastname']").send_keys("Alexeeva")
    email = browser.find_element(By.CSS_SELECTOR, ".form-group [name = 'email']").send_keys("sade_2005@list.ru")
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    upload = browser.find_element(By.CSS_SELECTOR, "[type='file']")

    # Находим и получаем путь к директории текущего исполняемого файла
    current_path = os.path.abspath(os.path.dirname(__file__))
    # в переменную ложим полный путь до файла
    file_path = os.path.join(current_path, 'new-file.txt')
    upload.send_keys(file_path)
    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # alert = browser.switch_to.alert
    # alert.accept()
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

