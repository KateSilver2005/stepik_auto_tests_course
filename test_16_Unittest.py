import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем класс с тестами, который должен наследоваться от unittest.TestCase
class TestForm (unittest.TestCase):
    def test_registration1(self):
        # try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Заполняем обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class > input.first")
        input_first_name.send_keys("Kate")
        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class > input.second")
        input_last_name.send_keys("Alexeeva")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class > input.third")
        input_email.send_keys("sade_2005@llist.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assertEquals проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals (welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает")
            # finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test_registration2(self):
        # try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Заполняем обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class > input.first")
        input_first_name.send_keys("Kate")
        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class > input.second")
        input_last_name.send_keys("Alexeeva")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class > input.third")
        input_email.send_keys("sade_2005@llist.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assertEquals проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals (welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает")
        # finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
if __name__ == "__main__":
    unittest.main()