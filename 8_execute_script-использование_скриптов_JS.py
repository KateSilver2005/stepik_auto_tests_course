# from selenium import webdriver
# browser = webdriver.Chrome()
# import time
# try:
#     browser.execute_script("document.title='Script executing';")
#     browser.execute_script("alert('Robots at work');")
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(2)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()