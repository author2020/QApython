# ________________________Замена Time.sleep() - Implicit_wait Который заложен в Selenium Waits


# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By, который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# import re


# driver = webdriver.Chrome() #иницилизирую драйвер браузера

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_14/')
   
#     btn = driver.find_element(By.ID,'verify').click()
#     message = driver.find_element(By.ID,'verify_message')
#     assert 'Verification successful!' in message.text
   

# finally:
#     time.sleep(5)
#     driver.quit()

# _______________________В selenium wedbriver есть способ организации ожидания выполнения кода. 
# Который позволяет задать ожидание при инициализации драйвера, другими словами мы можем применить его ко всем тестам. 
# Ожидание называется неявным (implicit wait) так как его не надо явно указывать каждый раз когда мы выполняем поиск элементов, 
# оно автоматически будет применяться при вызове каждой последующей команды. 
# На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде чем выбросит исключение NoSuchElementEx

# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# import re

# driver = webdriver.Chrome() #иницилизирую драйвер браузера
# driver.implicitly_wait(5) #задали неявное ожидание при инициализации драйвера = 5 секунд - работает ДЛЯ ВСЕХ ЭЛЕМЕНТОВ НА СТРАНИЦЕ

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_14/')
       
#     btn = driver.find_element(By.ID,'verify').click()
#     message = driver.find_element(By.ID,'verify_message')
#     assert 'Verification successful!' in message.text
       
# finally:
#     time.sleep(5)
#     driver.quit()

# _______________________ Возможные ошибки:
# Если элемент не был найден за отведенное время, то мы получим NoSuchElementException
# Если элемент был найден, но при последующем обращении к элементу DOM изменился, то мы получим StaleElementReferenceException. 
# Пример(Мы нашли кнопку на сайте, и через 2 секунды решили кликнуть по ней, Но кнопка за это время была скрыта скриптом, 
# в таком случае метод применять бесполезно (click) так как кнопка ‘Устарела’ в понимании DOM и весит в состоянии (stale) а значит мы увидим исключение.
# Если элемент был найден в момент поиска но сам элемент невидим(имеет нулевые размеры например) 
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNoVisibleException


# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# import re

# driver = webdriver.Chrome() #иницилизирую драйвер браузера
# driver.implicitly_wait(5) #задали неявное ожидание при инициализации драйвера = 5 секунд - работает ДЛЯ ВСЕХ ЭЛЕМЕНТОВ НА СТРАНИЦЕ

# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_15/')
       
#     btn = driver.find_element(By.ID,'verify').click()
#     message = driver.find_element(By.ID,'verify_message')
#     assert 'Verification successful!' in message.text

# finally:
#     time.sleep(5)
#     driver.quit()

# получили     assert 'Verification successful!' in message.text
# AssertionError
# При выполнении кода у нас вылетает ошибка поиска сообщения, потому что кнопка есть и он ее сразу нашел, кликнул, а то что кнопка не активна его не интересует.
# Чтобы этого избежать нам нужны.
# Явные ожидания (Explicit Wait)

#___________________________________________________ Явные ожидания (Explicit Wait) https://www.selenium.dev/documentation/webdriver/waits/
#В WebDriver есть явные ожидания которые позволяют задать специально ожидание для конкретного элемента. 
# Для этого используется expected_conditions
# и webdriverwait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#____________________________________ Решение с WebDriverWait - это самый лучший вариант для работы и собеседования

# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re

# driver = webdriver.Chrome() #иницилизирую драйвер браузера

# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_15/')
#     btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click() # код ожидает 5 секунд пока элемент станет доступным для нажатия
#     message = driver.find_element(By.ID,'verify_message')
#     assert 'Verification successful!' in message.text
       
       
# finally:
#     time.sleep(5)
#     driver.quit()

# WebDriverWait - это класс из библиотеки Selenium, предназначенный для явного ожидания выполнения определенного запроса
# driver - переменная которая содержит экземпляр webdriver  
# 5 - значение в секундах, которое определяет максимальное время ожидания выполнения условия
# Документация по методу https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# Задание:Требуется написать скрипт, который будет находить нам 1 машину дожидаться пока цена будет 550$  и как только цена будет 550 нажимать кнопку купить
# в результате должна зеленая надпись, что вы 
# Вы успешно купили автомобиль!


#_________________________________________не решили задачу - как скомбинировать не знаю синтаксис https://docs.google.com/document/d/1kwJLHZy7o1QU2fDyjal6-epM2wQusAXrpkvSdFma51Q/edit
# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re

# driver = webdriver.Chrome() #иницилизирую драйвер браузера

# try:
#     driver.get('https://erikdark.github.io/QA_autotest_16/')

    
#     # a1 = WebDriverWait(driver,5).until((EC.text_to_be_present_in_element((By.ID,"price1"), '550')))
#     # print(a1)
#     # print(type(a1)) 
#     # a2 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))) 
#     # print(a2)
#     # print(type(a2)) 
#     if WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))): # and WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))):
#     # if WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))):
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))).click() 
#     # .click() 
#     # lada_price.click() 
#     # код ожидает N секунд пока элемент станет видимым
#     # my_price = lada_price.text
#     # print(my_price)
#     # btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.CSS_SELECTOR,'#buyButton1')).click()
#     # btn = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID,'buyButton1'))).click() # код ожидает 1 секунд пока элемент станет доступным для нажатия
#     message = driver.find_element(By.ID,'message1')
#     assert 'Вы успешно купили автомобиль!' in message.text

       
       
# finally:
#     time.sleep(5)
#     driver.quit()

#________________________________________ДЗ_не решила задачи - как скомбинировать не знаю синтаксис https://docs.google.com/document/d/1kwJLHZy7o1QU2fDyjal6-epM2wQusAXrpkvSdFma51Q/edit
# ДЗ:
# https://erikdark.github.io/QA_autotest_16/
# https://erikdark.github.io/Qa_autotests_17/
# Задача: написать код, который будет при запуске 10 раз из 10 выдавать нужный результат за исключением физической невозможности дать верный ответ.
# Для 2 и 3 машины
# 800
# 19000
# https://docs.google.com/document/d/1GFF7sSzvk3zV0Vq5QSwjEhzA3i28C_hFK1aQCjAuGf0/edit
# Пример вакансии на которую не стоит тратить время


# _____________________________________________________Вернемся к нему с локаторами
# https://erikdark.github.io/QA_autotest_16/


# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()
# try:
#     driver.get('https://erikdark.github.io/QA_autotest_16/')
#     wait = WebDriverWait(driver,10)
#     price_element = wait.until(EC.presence_of_element_located((By.ID,'price1')))
#     while True:
#         current_price = int(price_element.text)
#         if current_price == 550:
#             buy_btn = driver.find_element(By.CSS_SELECTOR,'[id="buyButton1"]').click()
#             message_element = driver.find_element(By.CSS_SELECTOR,'[id="message1"]')
#             if 'Вы успешно купили автомобиль!' in message_element.text:
#                print('Успех')
#             else:
#                 print('Не успех')
#             break
#         time.sleep(1)
# finally:
#     driver.quit()




# __________________________________EC.presence_of_element_located((By.ID,'price1'))
# presence_of_element_located, требует чтобы ему был передан кортеж, содержащий метод поиска (By.ID в нашем случае) и строка идентификатора элемента. 
# Это связано с тем, что SELENIUM ожидает, что мы передадим ему метод поиска и строку для поиска а не результат поиска элемента.
# Когда мы используем find_element , он возвращает сам элемент, не подходит для функций ожидания, которые работают с локаторами.
# С переменными будет выглядеть вот так

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotest_16/')
#     price_locator = (By.ID,'price1')
#     btn = (By.ID,'buyButton1')
#     msg = (By.ID,'message1')
#     wait = WebDriverWait(driver,10)
#     price_element = wait.until(EC.presence_of_element_located(price_locator))
#     while True:
#         current_price = int(price_element.text)


#         if current_price == 550:
#             buy_btn = driver.find_element(*btn).click()
#             message_element = driver.find_element(*msg)
#             if 'Вы успешно купили автомобиль!' in message_element.text:
#                print('Успех')
#             else:
#                 print('Не успех')
#             break
#         time.sleep(1)
# finally:
   
#     driver.quit()

# Пояснение к звездочке в коде выше (*)  используется для распаковки кортежа в аргументы функции. В данном случае, мы используем * только при работе с find_element для until в купе с EC * для распаковки не требуется, потому что она уже ожидает правильной передачи.


#______________________________________Функции из EC в Selenium (Expectedconditions)

# presence_of_element_located - ожидает появления элемента на странице. Не требует чтобы элемент был видимым.
# element = wait.until(EC.presence_of_element_located((By.ID,’element_id)))
# visibility_of_element_located - ожидает что элемент станет видимым
# element_to_be_clickable  -Ожидает что элемент станет кликабельным
# text_to_be_present_in_element - ожидает появления определенного текста внутри элемента.
# wait.until(EC.text_to_be_present_in_element(By.ID,’element_id),’Expected Text’))
# frame_to_be_available_and_switch_to_it - ожидает появление фрейма и переключения на него.
# alert_is_present ожидает появление js уведомлений.



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

# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html


# _________________________________________________________________Pytest и фикстуры
# Что такое с чем их едят

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit


# Фикстуры в Pytest - это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.


# https://en.wikipedia.org/wiki/Test_fixture#Software



# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit



# ________________________Выше фикстура по инициализации веб-драйвера и закрытия.


# ___________________________________________Пример фикстуры для логина и пароля


# @pytest.fixture
# def login_driver(driver):
#     driver.get('https://blabla/login')


#     userame = driver.find_element(By.CLASS_NAME,'login').send_keys('root')
#     userame = driver.find_element(By.CLASS_NAME,'login').send_keys('root')
#     btn....
#     yield driver




# def test_dashbord(login_driver):
#     assert ....


# ________________________________________Разница между фикстурми и обычными функциями в pytest

# Цели и использование:
# Обычные функции: в тестах выполняют конкретные задачи и вызываются напрямую внутри тестов. Они не обладают автоматическим управлением жизненным циклом.
# Фикстуры - Позволяют разделить логику настройки и очистки для тестов, делая код тестов более читаемым. Фикстуры могут быть автоматически вызваны тестовой функцией и они могу быть переиспользованы в нескольких тестах.



# ________________________________________________Автоматическое управление жизненным циклом:

# Фикстуры pytest управляют жизненным циклом. Например код до оператора yield выполняется до теста, а код после yield после теста.
# Обычные функции не имеют встроенного механизма управления жизненным циклом. вы должны будете вручную вызывать их и управлять очисткой.


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit


# http://selenium1py.pythonanywhere.com/ru/


# Тест-сьюты - это набор тестов, которые сгруппированы вместе для выполнения. В контексте pytest, тест-сьюты позволяют объединить связные тесты для удобного запуска и организации.

# Вы можете использовать для группировки, директории, модули, классы и метки.

# Вариант с файлами
# tests/ 
# ├── test_login.py 
# ├── test_dashboard.py 
# └── test_profile.py


# _________________________________________Вариант с маркерами
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest


# @pytest.mark.login
# def test_valid_login(driver):
#     driver.get('https///')
#     #.....(тест на логин валидный)
# @pytest.mark.login
# def test_invalid_login(driver):
#     driver.get('https///')
#     #.....(тест на логин  инвалидный)
# @pytest.mark.dashboard
# def test_dashboard(driver):
#     driver.get('https///')
#     #.....(тест на дашборд)

# pytest -m (название маркера)
# Вариант с классами
# link = 'http://selenium1py.pythonanywhere.com/ru/'


# class TestMainPage1():
#     def setup_method(self):
#         print('run browser')
#         self.driver = webdriver.Chrome()


#     def teardown_method(self):
#         print('quit browser')
#         self.driver.quit()


#     def test_guest_see_link(self):
#         self.driver.get(link)
#         self.driver.find_element(By.CSS_SELECTOR,'#login_link')


#     def test_g_l_m(self):
#         self.get(link)
#         self.driver.find_element(By.CSS_SELECTOR,'.basket-mini .btn-group > a')


# В каких случая стоит прибегать к маркерам
# Мы можем делать выборку.
# Например у нас есть ряд тестов, который мы выполняем на каждый коммит разработчика.
# (smoke)

# Также берем делим дальше наши тесты и вешаем маркер регрессионных тестов(regression) которые нужно запускать на момент релиза.

# Если нам нужно регистрировать наши метки их надо занести в файл в корневой папке проекта.

# pytest.ini

# и текст

# [pytest]
# markers = 
# 	smoke: …..
# 	regression: ……




# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# link = "http://selenium1py.pythonanywhere.com/"




# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()




# class TestMainPage1():


#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")


#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


#     @pytest.mark.xfail
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "button.favorite")

# Конфигурация тестов. 

# Когда у вас много тестов, вы в каждом файле описываете фикстуру. Это нудно. Мне не нравится.
# Вместо этого мы будем создавать файл  конфигураций в который помещаем часто употребляемы фикстуры и глобальные настройки. Файл должен лежать в вашем проекте с тестами. 


# создаем файл conftest.py 
# закидываем туда функции и фикстуры которые надо предоставлять для всех тестов

# ВАЖНО!

# Pytest автоматически находит и подгружает файлы conftest.py которые находятся в директории с тестами. 
# Ессли вы храните свои скрипты в одной директории, то смотрите чтобы не возникло ситуации когда вы запускаете тест из папки tests

# tests/
# |
# |-conftest.py
# |-subfolder
# 	|-conftest.py
# 	|-test_abs.py

# ____________________________________Так делать незя!


# selenium_Course/
# |
# |-section1
# |	|-conftest.py
# |	|-test_login.py
# 	|-test_pw.py
# |
# |-section2
# 	|-conftest.py
# 	|-test_main_page.py


# https://erikdark.github.io/Qa_autotests_reg_form_pop_up/

# login:  testuser
# password: password123

# __________________________________Ваша задача написать автотест (pytest)
# со следующим набором действий
# Открыть страницу
# Авторизоваться под логином и паролем(рабочими)
# Дождаться того что попап закроется
# Если логин или пароль отличаются получить сообщение
# Войти без пароля (получить сообщение)
# Войти без логина(получить сообщения)


# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def driver():
#    driver = webdriver.Chrome()
#    yield driver
#    driver.quit()

# @pytest.mark.login
# def test_login(driver):
#    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
#    open_modal_button = WebDriverWait(driver, 10).until(
#        EC.element_to_be_clickable((By.ID, 'openModalButton'))
#    )
#    open_modal_button.click()
#    modal = WebDriverWait(driver, 10).until(
#        EC.visibility_of_element_located((By.ID, 'loginModal'))
#    )
#    username_field = driver.find_element(By.ID, 'username')
#    password_field = driver.find_element(By.ID, 'password')
#    login_button = driver.find_element(By.CSS_SELECTOR, '#loginForm button[type="submit"]')

#    username_field.send_keys('testuser')
#    password_field.send_keys('password123')
#    login_button.click()




 
#    WebDriverWait(driver, 10).until(
#        EC.invisibility_of_element((By.ID, 'loginModal'))
#    )

#    modal_display = driver.execute_script("return document.getElementById('loginModal').style.display")
#    assert modal_display == 'none', 'Modal did not close after login'

# if __name__ == "__main__":
#    pytest.main()

# https://www.mozilla.org/ru/firefox/new/ - официальный браузер
# https://github.com/mozilla/geckodriver/releases - драйвер мозилы
# Скачиваем  драйвер под нашу винду 

# https://github.com/operasoftware/operachromiumdriver/releases для оперы
# https://github.com/yandex/YandexDriver - для яндекса


# ________________________________________________Пример как можно оформить conftest для запуска в нужном нам браузере не меняя постоянно conftest.py

# import pytest
# from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption('--browser_name',action='store', default=None, help='Choose browser: chrome or firefox')


# @pytest.fixture(scope='function')
# def driver(request):
#     driver_name = request.config.getoption('browser_name')
#     driver = None
#     if driver_name == 'Chrome':
#         driver = webdriver.Chrome()
#     elif ....

# pytest -s -v -- browser_name=Chrome test_example.py



# https://docs.pytest.org/en/latest/reference/plugin_list.html - тут все плагины для pytest

# У нас бывают ситуации когда наш тест может упасть, в связи с форм факторами. Для того проверить проблема это или реальный баг

# Мы ставим плагин 
# pip install pytest-rerunfailures

# И после его установки, когда хотим указать количество перезапусков для каждого упавшего теста, мы должны добавить в командную строку параметр --reruns n
# где n это количество перезапусков.

# Если прогон повторных запусков пройдет успешно, то и проон тестов пройдет успешно. Количество перезапусков отражается в отчетах.
# pytest -v --reruns 5 --browser_name=Chrome test.py


# Для тех кто будет работать с разными языковыми интерфейсами.
# Для вас Есть возможность передавать данные через параметр accept-language
# А также Класс Option и метод add_experimental_option

# from selenium.webdriver.chrome.option import Options

# options = Options()
# options.add_experimental_option(‘prefs’,{intl.accept_languages’: user_language})
# driver = webdriver.Chrome(options=options)



# _________________________________________________________Задача:
# Открыть сайт выше с разделом Предложения
# http://selenium1py.pythonanywhere.com/ru/

# То есть с главной перейти на раздел предложения
# В разделе предложения берем эти 4 книги и добавляем в корзину
# Затем идем в раздел посмотреть корзину
# И начинаем процесс оформления заказа
# Довести процесс оформления до конца

# Входные данные:
# login - admin123 321nimda
# pw - password123 321drowssap
# bd_name - bd_dovod dovod_db
# localhost - localhost tsohlacol
# нажать кнопку отправить

# https://erikdark.github.io/dovod_repo_QA_form/


# _____________________Решение


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# driver = webdriver.Firefox()
# driver.get('https://erikdark.github.io/dovod_repo_QA_form/')

# #найти элементы
# l_i = driver.find_element(By.ID,'login')
# p_i = driver.find_element(By.ID,'password')
# d_i = driver.find_element(By.ID,'database')
# h_i = driver.find_element(By.ID,'host')
# s_b = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')

# #заполнил форму
# l_i.send_keys('admin123')
# p_i.send_keys('password123')
# d_i.send_keys('bd_dovod')
# h_i.send_keys('localhost')

# #отправляю форму
# s_b.click()
# alert = driver.switch_to.alert
# alert.accept()

# #очищаю поля
# l_i.clear()
# p_i.clear()
# d_i.clear()
# h_i.clear()

# h_i.send_keys('tsohlacol')
# d_i.send_keys('dovod_db')
# p_i.send_keys('321drowssap')
# l_i.send_keys('321nimda')
# s_b.click() #отправляю форму

# ___________________________________________ кладем в корзину те книги, которые нужны [0,2,4,6,14,16]
# https://selenium1py.pythonanywhere.com/ru/offers/

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.get('https://selenium1py.pythonanywhere.com/ru/offers/')


# indexs_to_click = [0,2,4,6,14,16]


# for i in indexs_to_click:
#     try:
#         btn = driver.find_elements(By.CSS_SELECTOR,'button.btn.btn-primary.btn-block') # внимание - тут .find_elementS
#         btn[i].click()
#         print(f'[{i}] нннн куплен')
#     except:
#         print(f'[{i}] хрень какая-то  - кнопка не кликабельная или элемент не найден')

# # __________А так ищем через nth-child() -  второй вариант решения - кладем в корзину те книги, которые нужны [0,2,4,6,14,16]

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.get('https://selenium1py.pythonanywhere.com/ru/offers/')


# indexs_to_click = [2,4,7]


# for i in indexs_to_click:
#     try:
#         btn_css = f'.row .col-xs-6:nth-child({i+1}) button.btn.btn-primary.btn-block'
#         btn = driver.find_element(By.CSS_SELECTOR,btn_css)
#         btn.click() # ручками - успеть зайти в корзину и проверить до закрытия окна
#         print(f'[{i}] нннн куплен')
#     except:
#         print(f'[{i}] хрень какая-то')

# var charMap = { 'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': '𐐒', 'C': 'Ɔ', 'D': 'ᗡ', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ɹ', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': '‘', '.': '˙', "'": ',', '"': '„', '?': '¿', '!': '¡', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<', '&': '⅋', '_': '‾', '/': '\\', '\\': '/', ';': '؛', ':': '∴', '@': '@', '+': '±', '-': '⁻', '*': '⁎', '=': '≠', '^': 'v', '°': '°', '#': '#', '$': '$', '%': '%', '£': '£', '€': '€', '¥': '¥', '`': '´', '~': '~' };


