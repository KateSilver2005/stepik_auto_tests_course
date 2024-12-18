from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(1)
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# browser.execute_script("window.scrollBy(0, 100);")

button.click()
time.sleep(3)
