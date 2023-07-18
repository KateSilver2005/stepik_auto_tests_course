# Проверка  чекбоксов и радиокнопок, что одна из них активна по уолчанию
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    #Находим радиокнопку
    people_radio = browser.find_element(By.ID, "peopleRule")
    #получаем значение атрибута checked
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    #проверяем что он активен - нажат по умолчанию и в принт вернется знаечение "true"
    #если проверка не увенчается успехом, в AssertionError запишеться наименование ошибки "Robot radio is not selected by default"
    assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is not None, "Robot radio is not selected by default"
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

