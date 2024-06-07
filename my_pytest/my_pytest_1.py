# https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery
# C:\Users\AuroraPC\Desktop\QA_Python\QA_Python\practika> pytest pytest_example\test_first_element.py::test_sum
# так я запускаю тест на конкретный модуль в файле test_first_element.py


# PS C:\Users\AuroraPC\Desktop\QA_Python\QA_Python\practika> pytest pytest_example\test_first_element.py

# PS C:\Users\AttekPC\Documents\GitHub\QApython> pytest my_pytest\my_pytest.py
# Так я запускаю все тесты в файле

# Для запуска теста в терминал пишем pytest и теперь подробнее:
# Если мы не передаем никакого аргумента в команду, а тупо написали pytest в таком случае, тест раннер запустит поиск по всей текущей директории.
# как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов.

# Будет искать только файлы в которых есть в начале или в конце test_*.py *_test.py

# Все функции начинаются test которые находятся вне классов
# Все тесте название которых начинается  с test внутри классов, имя которых начинается с Test(без метода __Init__ внутри класса) 

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchAttributeException



# def test_exeption1():
#     try:
#         driver = webdriver.Chrome
#         driver.get('http://selenium1py.pythonanywhere.com/ru/')
#         with pytest.raises(NoSuchAttributeException):
#             driver.find_element(By.CSS_SELECTOR, '#button.btn')
#             pytest.fail('Не должно быть кнопки')

#     finally:
#         driver.quit()


# запускать надо с включенным венвом так - (venv) PS C:\Users\AttekPC\Documents\GitHub\QApython> pytest my_pytest\my_pytest_1.py
# pytest my_pytest\my_pytest_1.py

# import pytest


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# def test_exection1(): # Успешная регистрация - то есть все поля заполнены кнопка нажимается текст появляется
#     try:
#         driver = webdriver.Chrome()
#         driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
#         with pytest.raises(NoSuchElementException): # все элементы на странице есть, поэтому тут не нужно выкидывать это исключение - просто надо было делаь через assert
#             data = ['Katrin', 'peterburg@gmail.com','kjh8908D-']
#             input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
#             for i in range(len(input_one)):
#                 input_one[i].send_keys(data[i])
#             btn = driver.find_element(By.ID,'button').click()
#             message = driver.find_element(By.ID,'success-message')
#             assert 'Вы успешно зарегистрированы!' in message.text
#             pytest.fail('Все поля должны быть заполнены')
   
#     finally:
#         driver.quit()

# def test_exection2(): # Регистрация с ошибкой (неверный email)
#     try:
#         driver = webdriver.Chrome()
#         driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
#         with pytest.raises(NoSuchElementException):
#             data = ['Katrin', '','kjh8908D-']
#             input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
#             for i in range(len(input_one)):
#                 input_one[i].send_keys(data[i])
#             btn = driver.find_element(By.ID,'button').click()
#             message = driver.find_element(By.ID,'success-message')
#             assert message.text == 'Пожалуйста, заполните все поля.', 'Не прошел'
#             pytest.fail('Все поля должны быть заполнены')
    
#     finally:
#         driver.quit()

# pytest my_pytest\my_pytest_1.py


# Мое решение (ERIC) с использованием ХРЕН ПОЙМИ ЧЕГО ПОД НАЗВАНИЕМ ФИКСТУРЫ
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit




def test_successful_reg(driver):
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
    in1 = driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Erik')
    in1 = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('Erik@mail.ru')
    in1 = driver.find_element(By.CSS_SELECTOR,'#password').send_keys('Erik123')
    btn = driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#success-message').text
    assert message == 'Вы успешно зарегистрированы!', 'Не нашел текст или ты рукожоп...'


def test_successful_reg1(driver):
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
    in1 = driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Erik')
    in1 = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('@mail.ru')
    in1 = driver.find_element(By.CSS_SELECTOR,'#password').send_keys('Erik123')
    btn = driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#success-message').text
    assert message == 'Вы успешно зарегистрированы!', 'почта не прошла'

# ПОЛУЧИЛИ ВОТ ЧТО
# =================================================================================================== test session starts ===================================================================================================
# platform win32 -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
# rootdir: C:\Users\AttekPC\Documents\GitHub\QApython
# collected 2 items

# my_pytest\my_pytest_1.py
# DevTools listening on ws://127.0.0.1:54107/devtools/browser/7b60e246-ba1d-44d7-b2d7-8bb1e2e7cdff
# .
# DevTools listening on ws://127.0.0.1:54125/devtools/browser/7f8c4488-22ec-442b-91b2-9bc4fd00a15c
# F                                                                                                                                                                                          [100%]

# ======================================================================================================== FAILURES ========================================================================================================= 
# __________________________________________________________________________________________________ test_successful_reg1 ___________________________________________________________________________________________________ 

# driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="5848b2c0a8127c50836b05e5c50b345c")>

#     def test_successful_reg1(driver):
#         driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
#         in1 = driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Erik')
#         in1 = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('@mail.ru')
#         in1 = driver.find_element(By.CSS_SELECTOR,'#password').send_keys('Erik123')
#         btn = driver.find_element(By.CSS_SELECTOR,'button').click()
#         message = driver.find_element(By.CSS_SELECTOR,'#success-message').text
# >       assert message == 'Вы успешно зарегистрированы!', 'почта не прошла'
# E       AssertionError: почта не прошла
# E       assert '' == 'Вы успешно зарегистрированы!'
# E
# E         - Вы успешно зарегистрированы!

# my_pytest\my_pytest_1.py:118: AssertionError
# ================================================================================================= short test summary info ================================================================================================= 
# FAILED my_pytest/my_pytest_1.py::test_successful_reg1 - AssertionError: почта не прошла
# =============================================================================================== 1 failed, 1 passed in 6.01s =============================================================================================== 
# (venv) PS C:\Users\AttekPC\Documents\GitHub\QApython> 

# pytest my_pytest\my_pytest_1.py