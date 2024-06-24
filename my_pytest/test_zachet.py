# pytest my_pytest\test_zachet_task1.py -v

# __________________________________task 1 Проверить валидацию формы регистрации
# Критерии:
# Имя имеет только буквы и символ - все остальное не должно проходить;
# email имеет корректный формат;
# Пароль содержит не менее 8 символов, включая одну заглавную букву, одну строчную букву и одну цифру.
# Пароль и его подтверждение совпадают

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

rf_data_0 = ['-Katrin-', 'peterburg@gmail.com','Password123','Password123'] # валидный набор данных для формы регистрации
process_message_0 = 'Регистрация успешна!'

rf_data_1 = ['Katrin_1', 'peterburg@gmail.com','Password123','Password123'] # невалидное имя
process_message_1 = 'Имя может содержать только буквы и знак "-"'

rf_data_2 = ['-Katrin-', 'peterburg.gmail.com','Password123','Password123'] # невалидный email
# process_message_2 = 'Введите корректный email'
process_message_2_1 = 'Адрес электронной почты должен содержать символ "@". В адресе "peterburg.gmail.com" отсутствует символ "@"'
process_message_2_2 =''

rf_data_3 = ['-Katrin-', 'peterburg@gmail.com','Password','Password'] # невалидный пароль
process_message_3 = 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'

rf_data_4 = ['-Katrin-', 'peterburg@gmail.com','Password123','Password321'] # Пароли не совпадают
process_message_4 = 'Пароли не совпадают'

rf_data_5 = ['', 'peterburg@gmail.com','Password123','Password123'] # пустое имя
process_message_0 = 'Регистрация успешна!'


def test_successful_reg_valid_data(driver: WebDriver): # тест корректности обработки валидных данных
    driver.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
    data = rf_data_0
    input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
    for i in range(len(input_one)):
        input_one[i].send_keys(data[i])
    driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert message == process_message_0

def test_unsuccessful_reg_invalid_name(driver: WebDriver): # тест корректности обработки невалидного имени и валидных данных других required полей
    driver.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
    data = rf_data_1
    input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
    for i in range(len(input_one)):
        input_one[i].send_keys(data[i])
    driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert message == process_message_1

def test_unsuccessful_reg_invalid_email(driver: WebDriver): # тест корректности обработки невалидного email
    driver.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
    driver.find_element(By.ID,'name').send_keys('erik')
    email_field = driver.find_element(By.ID,'email')
    email_field.clear()
    email_field.send_keys('eri@')
    driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
    valid_mes1 = email_field.get_property('validationMessage') # Введите часть адреса после символа "@". Адрес "eri@" неполный.
    print(f'Valid message {valid_mes1}')
    email_field.clear()
    email_field.send_keys('peterburg@gmail.com')
    valid_mes2 = email_field.get_property('validationMessage')
    print(f'Valid message {valid_mes2}')
    if valid_mes1 == process_message_2_1:
        assert valid_mes2 == process_message_2_2


def test_unsuccessful_reg_invalid_password(driver: WebDriver): # тест корректности обработки невалидного пароля и валидных данных других required полей
    driver.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
    data = rf_data_3
    input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
    for i in range(len(input_one)):
        input_one[i].send_keys(data[i])
    driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert message == process_message_3 


def test_unsuccessful_reg_passwords_unmatch(driver: WebDriver): # тест корректности обработки несовпадения паролей и валидных данных других required полей
    driver.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
    data = rf_data_4
    input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
    for i in range(len(input_one)):
        input_one[i].send_keys(data[i])
    driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert message == process_message_4

