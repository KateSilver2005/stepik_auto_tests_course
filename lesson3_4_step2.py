# Мы видим, что в первом тест-сьюте браузер запустился один раз, а во втором — два раза.
#
# Лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее.
# К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают,
# если они запускаются каждый в собственном браузере.

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite 1 ..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite 1 ..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        elf.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test 2..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")