from selenium import webdriver
import time


browser = webdriver.Chrome()
time.sleep(3)

# browser.execute_script("document.title='Script executing';")
# time.sleep(3)
#
# browser.execute_script("alert('Robots at work');")
# time.sleep(3)

browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(3)


