# Если в модалке одна кнопка ОК
alert = browser.switch_to.alert  # переключиться на окно с alert
alert.accept() # принять его с помощью команды accept()

# получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

# Если в модалке у пользователя есть выбор согласиться с сообщением или отказаться от него
# Оно называется confirm (Отмена или ОК). Для переключения на окно confirm используется та же команда, что и в случае с alert:

confirm = browser.switch_to.alert
confirm.accept()
# Для confirm-окон можно использовать следующий метод для отказа:
confirm.dismiss()

# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()