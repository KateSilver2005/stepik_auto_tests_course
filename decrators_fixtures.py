# https://pythonworld.ru/osnovy/dekoratory.html
# Классические фикстуры  (lesson3-4_step2) - setup_method, terdown_method
#
# Фикстуры, возвращающие значение (lesson3-4_step3)
# @pytest.fixture
# def browser():
# ...
# def test_guest_should_see_login_link(self, browser):
# ...
#
# Финализаторы — закрываем браузер (lesson3-4_step4) - yield
# @pytest.fixture
# def browser():
#     ....
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     browser.quit()
# Область видимости scope (lesson3-4_step5) - scope (“function”, “class”, “module”, “session”)
# @pytest.fixture(scope="class")
#
# Автоиспользование фикстур (lesson3-4_step6) - autouse=True -
# который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова
#
#


# 0
def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

stand_alone_function()
#
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
# 1
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()

# 2
# stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function()

# 3
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Оставь меня в покое")
#
# another_stand_alone_function()

# 4
# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper
#
# def ingredients(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper

# def sandwich(food="--ветчина--"):
#     print(food)
#
# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()

# 5
# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print(food)
#
# sandwich()

# 6
# @ingredients
# @bread
# def sandwich(food="--ветчина--"):
#     print(food)
#
# sandwich()

# 7
# Передача декоратором аргументов в функцию
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# # передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
# print_full_name("Vasya", "Pupkin")

# 8
# Декорирование методов
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie -= 3
#         return method_to_decorate(self, lie)
#     return wrapper
#
# class Lucy:
#     def __init__(self):
#         self.age = 32
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
# l = Lucy()
# l.sayYourAge(-3)

# 9
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Передали ли мне что-нибудь?:")
#         print(args)
#         print(kwargs)
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")
#
# function_with_no_argument()
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
# function_with_arguments(1, 2, 3)
# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#     print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))
#
# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
# class Mary(object):
#     def __init__(self):
#         self.age = 31
#     @a_decorator_passing_arbitrary_arguments
#     def sayYourAge(self, lie=-3): # Теперь мы можем указать значение по умолчанию
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
# m = Mary()
# m.sayYourAge()

# 10
# Декораторы с аргументами
# def decorator_maker():
#     print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
#     def my_decorator(func):
#         print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
#         def wrapped():
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
#                    "Я возвращаю результат работы декорируемой функции.")
#             return func()
#         print("Я возвращаю обёрнутую функцию.")
#         return wrapped
#     print("Я возвращаю декоратор.")
#     return my_decorator
#
# # Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
# new_decorator = decorator_maker()
#
# # Теперь декорируем функцию
# def decorated_function():
#     print("Я - декорируемая функция.")
#
#
# @decorator_maker()
# def decorated_function():
#     print("Я - декорируемая функция.")
#
# decorated_function()
#
# 11
# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print("Я создаю декораторы! И я получил следующие аргументы:",
#            decorator_arg1, decorator_arg2)
#     def my_decorator(func):
#         print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
#                decorator_arg1, decorator_arg2)
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "И я имею доступ ко всем аргументам\n"
#                    "\t- и декоратора: {0} {1}\n"
#                    "\t- и функции: {2} {3}\n"
#                    "Теперь я могу передать нужные аргументы дальше"
#                    .format(decorator_arg1, decorator_arg2,
#                            function_arg1, function_arg2))
#             return func(function_arg1, function_arg2)
#         return wrapped
#     return my_decorator
#
# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
#            " {1}".format(function_arg1, function_arg2))
#
# decorated_function_with_arguments("Раджеш", "Говард")
#
# 12
# def benchmark(func):
#     """
#     Декоратор, выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print(func.__name__, time.clock() - t)
#         return res
#     return wrapper
#
# def logging(func):
#     """
#     Декоратор, логирующий работу кода.
#     (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
#     """
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(func.__name__, args, kwargs)
#         return res
#     return wrapper
#
# def counter(func):
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
#         return res
#     wrapper.count = 0
#     return wrapper
#
# @benchmark
# @logging
# @counter
# def reverse_string(string):
#     return ''.join(reversed(string))
#
# print(reverse_string("А роза упала на лапу Азора"))
# print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,"
# "maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag,"
# "a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
# "a jar, sore hats, a peon, a canal: Panama!"))

