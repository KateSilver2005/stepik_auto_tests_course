# stepik_auto_tests_course
![Изображение](https://cdn.stepik.net/media/cache/images/courses/575/cover_3kqh9Iw/d1a44446e98638349c7416e78814f122.png "Логотип")
-[x] [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575 "программа курса")


## Создание виртуального пространства
### Шаги
1. Создать папку, где будут храниться наши виртуальные окружения, и перейдем в неё:
mkdir environments
cd environments
2. Создать виртуальное окружение:
`` python -m venv selenium_env ``
3. Запустим созданный для нас приложением venv файл activate.bat, чтобы активировать окружение:
`` selenium_env\Scripts\activate.bat ``

    >**Примечание.** *Если понадобится выйти из нашего окружения, достаточно выполнить команду deactivate*
---

## Активация виртуального пространства
### Шаги
1. Перейти в папку - `` cd C:\Users\ealekseeva\environments\selenium_env\Scripts ``
2. Активировать пространство - `` activate.bat ``
---
## Запуск скрипта из файла
### Шаги
1. Повторить шаги "активация виртуального пространства"
2. В пространстве ввести команду `` python C:\Users\ealekseeva\selenium_course\stepik_auto_tests_course\first_script.py ``
---
## Запуск скрипта в терминале
### Шаги
1. Запустить виртуальное пространство
2. Запуск интерпретатора - команда `` python ``
3. Пишем скрипт, Enter
    >**Примечание.** *Выход из интерпретатора - команда exit()*
---
## Фиксируем пакеты в requirements.txt 
### Шаги
1. Повторить шаги "активация виртуального пространства"
2. Выполнить команду ``pip freeze > requirements.txt``
   >**Примечание.** *Эта команда сохранит все версии пакетов в специальный файл requirements.txt.*
3. Как их оттуда достать?
   
   3.1. Создать новое виртуальное окружение

   3.2. Активировать окружение
4. После чего выполнить команду ``pip install -r requirements.txt``
---
## PyTest: правила запуска тестов
Когда мы выполняем команду pytest, тест-раннер собирает все тесты для запуска по определенным правилам:
1. Если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории 
2. Как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: 

   - ``найти все тесты в директории scripts/selenium_scripts``
   ``pytest scripts/selenium_scripts ``

   - ``найти и выполнить все тесты в файле``
   ``pytest test_user_interface.py ``

   - ``найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить``
   ``pytest scripts/drafts.py::test_register_new_user_parametrized  ``
3. Дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории

   - во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или \*\_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)

   - внутри всех этих файлов находит тестовые функции по следующему правилу:

     - все тесты, название которых начинается с test, которые находятся вне классов

     - все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)
---
## PyTest — отчёты
- ``pytest test_sample.py -v`` # (verbose, то есть подробный) в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения
- ``pytest test_sample.py --collect-only`` #собирает информацию тестового набора
- ``pytest test_sample.py -v`` #выводит вербозные сообщения
- ``pytest -q test_sample.py`` #опустить вывод имени файла
- ``python -m pytest -q test_sample.py`` #вызов pytest через python
- ``pytest --markers`` #показать доступные маркеры
- ``pytest -k "TestClass, а не test_one"`` #запускать только тесты с именами, которые соответствуют "строковому выражению"
- ``pytest test_server.py::TestClass::test_method`` #cnly run tests that match the node ID
- ``pytest -x`` #останавливаться после первой неудачи
- ``pytest --maxfail=2`` #останавливаться после двух неудач
- ``pytest --showlocals`` #показывать локальные переменные в трассировках
- ``pytest -l`` #(сокращение)
- ``pytest --tb=long`` #информативное форматирование трассировки по умолчанию
- ``pytest --tb=native`` #форматирование стандартной библиотеки Python
- ``pytest --tb=short`` #более короткий формат возвратов к трассировке
- ``pytest --tb=line`` #только одна строка для каждого сбоя
- ``pytest --tb=no`` #отсутствие вывода трассировки
- ``pytest -x --pdb`` #при первом сбое сброс в PDB, затем завершение сеанса тестирования
- ``pytest --durations=10`` #список 10 самых медленных длительностей теста.
- ``pytest --maxfail=2 -rf`` #выход после двух сбоев, сообщение о сбое.
- ``pytest -n 4`` #посылать тесты на несколько процессоров
- ``pytest -m slowest`` #запускать тесты с декоратором @pytest.mark.slowest или slowest = pytest.mark.slowest; @slowest
- ``pytest --traceconfig`` #выяснить, какие плагины pytest активны в вашем окружении.
- ``pytest --instafail`` #если установлен pytest-instafail, показывать ошибки и сбои мгновенно, а не ждать окончания набора тестов.