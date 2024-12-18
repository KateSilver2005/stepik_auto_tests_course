# Область видимости scope
# Допустимые значения: “function”, “class”, “module”, “session”.
# один раз для тестового метода
# один раз для класса (если в файле два класса, фикстура будет работать на два класса - два раза открывать браузер)
# один раз для модуля - один файл с тестами
# один раз для всех тестов, запущенных в данной сессии - весь прогон тестов (в нем может быть несколько файлов)
#
# в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере.
# Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера
# для каждого теста (function), чтобы повысить стабильность тестов

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")