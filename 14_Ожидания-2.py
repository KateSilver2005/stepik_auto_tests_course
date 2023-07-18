# CHAPTER 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# Мы видим, что WebDriver смог найти кнопку с id="verify" и кликнуть по ней, но тест упал на поиске элемента
# "verify_message" с итоговым сообщением:
#
# no such element: Unable to locate element: {"method":"id","selector":"verify_message"}
# Это произошло из-за того, что WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной.
# На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки,
# но неактивная кнопка в момент загрузки — обычное дело для реального сайта.

# CHAPTER 2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

# element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
# Обратите внимание, что в объекте WebDriverWait используется функция until, в которую передается правило ожидания,
# элемент, а также значение, по которому мы будем искать элемент. В модуле expected_conditions есть много других правил,
# которые позволяют реализовать необходимые ожидания:
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# Описание каждого правила можно найти на сайте
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions