import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCkpFields:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.ok_fields = 0  # Инициализация счетчика совпадений
        self.wrong_field = 0  # Инициализация счетчика несовпадений
        yield  # Передать управление тесту
        self.browser.quit()  # Закрыть браузер после выполнения теста

    @pytest.mark.parametrize("uid", [
        "9a96a2c7-3c0d-477f-f2a6-da3bf538f4f4",
        "dd61b41d-5b91-a9a0-9e50-4f025a87553b",
        "dd61b41d-5b91-a9a0-9e50-4f025a87553b"
    ])
    def test_new_fields_ckp(self, uid):
        url = 'https://nirtest-portal.cspfmba.ru'
        url_ckp = 'https://nirtest-portal.cspfmba.ru/cabinet/ckp/'
        loginForm = "loginForm"
        passwordForm = "passwordForm"
        username = "omg\\ealekseeva"
        password = 'KateSilver1@@'
        link = url_ckp + uid
        self.browser.get(url)
        self.browser.maximize_window()

        # Логин
        login = self.wait.until(EC.visibility_of_element_located((By.ID, loginForm)))
        login.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, passwordForm)))
        password_field.send_keys(password)
        enter = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'w-100')))
        enter.click()
        self.wait.until(EC.url_changes(url))  # Ожидание изменения URL после входа

        # Ожидание загрузки страницы и переход по ссылке
        self.browser.get(link)
        ias = self.browser.window_handles[0]

        # field_1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(2)")))
        # field_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(4)")))
        # field_3 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(6)")))
        # field_4 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(8)")))
        # field_5 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(10)")))
        # field_6 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(12)")))
        # fields = [field_1, field_2, field_3, field_4, field_5, field_6]
        # count = 0
        # for field in fields:
        #     if field.find_elements(By.XPATH, "./*"):
        #         count += 1

        # Получение полей
        fields = []
        for i in range(1, 7):  # Предполагается, что поля находятся в четных позициях
            field = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f".col-8.content div:nth-child({i * 2})")))
            fields.append(field)

        count = sum(1 for field in fields if field.find_elements(By.XPATH, "./*"))
        print(f"Количество пунктов в ИАС: {count}")

        # Переход на ЦКП-РФ
        url_ckp_rf = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.col-6:nth-child(5) div.marker.text-justify a'))).text
        self.browser.execute_script(f"window.open('{url_ckp_rf}', '_blank');")

        # Переключение на новую вкладку
        ckp_rf = self.browser.window_handles[1]
        self.browser.switch_to.window(ckp_rf)

        # Получение полей на ЦКП-РФ
        fields_ckp = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sale-detail-params")))
        field_ckp = fields_ckp.find_elements(By.XPATH, "./*")  # Ищем всех дочерних элементов
        field_ckp_count = len(field_ckp)
        print(f"Количество пунктов на ЦКП-РФ: {field_ckp_count}")

        # Сравнение результатов
        assert count == field_ckp_count, f'В ЦКП - {link} не все поля заполнены. Ожидалось {field_ckp_count}, получено {count}.'
        self.ok_fields += 1
        print("ok")

        # Закрытие вкладки и возврат на предыдущую
        self.browser.close()
        self.browser.switch_to.window(ias)
        self.wait.until(EC.visibility_of_element_located((By.ID, "topMenuUser"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".d-flex:nth-child(6)"))).click()
        exit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        exit.click()
        print(f"Проверен uid - {uid}")


class TestUsuFields:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.ok_fields = 0  # Инициализация счетчика совпадений
        self.wrong_field = 0  # Инициализация счетчика несовпадений
        yield  # Передать управление тесту
        self.browser.quit()  # Закрыть браузер после выполнения теста

    @pytest.mark.parametrize("uid", [
        'ca344476-de21-ce19-3974-14fd42a9d131',
        '47c9a94f-814c-1d1e-23cb-4fe7eb9d05fd',
        '6158f57a-f5e3-6c6d-0877-5216a310a796',
        '4844688d-fa47-3d25-aeda-9810b09585d3',
    ])
    def test_new_fields_usu(self, uid):
        url = 'https://nirtest-portal.cspfmba.ru'
        url_usu = 'https://nirtest-portal.cspfmba.ru/cabinet/usu/'
        loginForm = "loginForm"
        passwordForm = "passwordForm"
        username = "omg\\ealekseeva"
        password = 'KateSilver1@@'
        link = url_usu + uid
        self.browser.get(url)
        self.browser.maximize_window()

        # Логин
        login = self.wait.until(EC.visibility_of_element_located((By.ID, loginForm)))
        login.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, passwordForm)))
        password_field.send_keys(password)
        enter = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'w-100')))
        enter.click()
        self.wait.until(EC.url_changes(url))  # Ожидание изменения URL после входа

        # Ожидание загрузки страницы и переход по ссылке
        self.browser.get(link)
        ias = self.browser.window_handles[0]

        # field_1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(2)")))
        # field_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(4)")))
        # field_3 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(6)")))
        # field_4 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(8)")))
        # field_5 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(10)")))
        # field_6 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(12)")))
        # fields = [field_1, field_2, field_3, field_4, field_5, field_6]
        # count = 0
        # for field in fields:
        #     if field.find_elements(By.XPATH, "./*"):
        #         count += 1

        # Получение полей
        fields = []
        for i in range(1, 7):  # Предполагается, что поля находятся в четных позициях
            field = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f".col-8.content div:nth-child({i * 2})")))
            fields.append(field)

        count = sum(1 for field in fields if field.find_elements(By.XPATH, "./*"))
        print(f"Количество пунктов в ИАС: {count}")

        # Переход на ЦКП-РФ
        usu_rf = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ms-2 .ms-1')))
        url_usu_rf = usu_rf.get_attribute('href')
        self.browser.execute_script(f"window.open('{url_usu_rf}', '_blank');")

        # Переключение на новую вкладку
        usu_rf = self.browser.window_handles[1]
        self.browser.switch_to.window(usu_rf)

        # Получение полей на ЦКП-РФ
        fields_usu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sale-detail-params")))
        field_usu = fields_usu.find_elements(By.XPATH, "./*")  # Ищем всех дочерних элементов
        field_usu_count = len(field_usu)
        print(f"Количество пунктов на ЦКП-РФ: {field_usu_count}")

        # Сравнение результатов
        assert count == field_usu_count, f'В ЦКП - {link} не все поля заполнены. Ожидалось {field_usu_count}, получено {count}.'
        self.ok_fields += 1
        print("ok")

        # Закрытие вкладки и возврат на предыдущую
        self.browser.close()
        self.browser.switch_to.window(ias)
        self.wait.until(EC.visibility_of_element_located((By.ID, "topMenuUser"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".d-flex:nth-child(6)"))).click()
        exit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        exit.click()
        print(f"Проверен uid - {uid}")
