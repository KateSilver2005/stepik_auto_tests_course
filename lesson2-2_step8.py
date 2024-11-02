from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group input[name='firstname']")
    input1.send_keys("Kate")

    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group input[name='lastname']")
    input2.send_keys("Alekseeva")

    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group input[name='email']")
    input3.send_keys("error_mail")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    send_file = browser.find_element(By.CSS_SELECTOR, "[type='file']#file")
    send_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()