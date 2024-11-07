from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

def get_link(link):
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class > input.first")
    input_first_name.send_keys("Kate")
    input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class > input.second")
    input_last_name.send_keys("Alexeeva")
    input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class > input.third")
    input_email.send_keys("sade_2005@llist.ru")
    input_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class > input.first")
    input_phone.send_keys("911")
    input_address = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class > input.second")
    input_address.send_keys("USA")
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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text

class test_class_registration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        get_link(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        get_link(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()