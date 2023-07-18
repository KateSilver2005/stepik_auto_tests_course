from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 6 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#илиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиили
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# #Импортим сам модуль
# import random
# #Так как модуль для чисел, импортим еще один стандартный модуль
# import string
# # Создаем строку из букв англ. алфавита в нижнем регистре
# letters = string.ascii_lowercase
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     fields = browser.find_elements(By.TAG_NAME, "input")
#     for field in fields:
#         # В цикл добавляем генерацию случайного набора символов (диапазон произвольный)
#         random_word = ''.join(random.choice(letters) for _ in range(8))
#         #И заполняем наше поле этим словом
#         field.send_keys(random_word)
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#не забываем оставить пустую строку в конце файла

#илиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиилиили
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import random
# value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys(random.choice(value))
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 5 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# #
# # # не забываем оставить пустую строку в конце файла