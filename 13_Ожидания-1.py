from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

# Попробуйте сначала выполнить тест вручную, а затем запустить автотест. В первом случае, вы завершите тест успешно,
# во втором случае автотест упадет с сообщением NoSuchElementException для элемента c id="verify". Почему так происходит?
# Команды в Python выполняются синхронно, то есть, строго последовательно. Пока не завершится команда get, не начнется
# поиск кнопки. Пока кнопка не найдена, не будет сделан клик по кнопке и так далее.
# Но тест будет работать абсолютно стабильно, только если в данной веб-странице не используется JavaScript
# (что маловероятно для современного веба). Метод get дожидается информации от браузера о том, что страница загружена,
# и только после этого наш тест переходит к поиску кнопки. Если страница интерактивная, то браузер будет считать,
# что страница загружена, при этом продолжат выполняться загруженные браузером скрипты. Скрипт может управлять
# появлением кнопки на странице и показывать ее, например, с задержкой, чтобы кнопка красиво и медленно возникала
# на странице. В этом случае наш тест упадет с уже известной нам ошибкой NoSuchElementException, так как в момент
# выполнения команды button = browser.find_element(By.ID, "verify") элемент с id="verify" еще не отображается на
# странице. На данной странице пауза перед появлением кнопки установлена на 1 секунду, метод find_element() сделает
# только одну попытку найти элемент и в случае неудачи уронит наш тест.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(1)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# Теперь мы можем быть уверены, что при небольших задержках в работе сайта наши тесты продолжат работать стабильно.
# На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде,
# чем выбросить исключение NoSuchElementException.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/cats.html")
#
# button = browser.find_element(By.ID, "button")
# button.click()
# # message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text