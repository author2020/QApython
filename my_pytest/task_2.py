# Task 2. Задача для страницы логин
# Проверить что все 5 человек успешно проходят валидацию формы
# Затем создать нового пользователя и сразу проверить его на валидацию
# Затем создать разом 3 пользователей и снова проверить всех 3 на валидацию 
# Проверять в левой колонке создавать в правой

# pytest my_pytest\task2.py -v


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/QA_DIPLOM/login.html')
elements = driver.find_elements(By.TAG_NAME, 'td')
table_els = []
for e in elements:
    table_els.append(e.text)
print(type(table_els))
print(table_els)

users =[]
passwords = []

for i in range(len(table_els)):
    if i % 2 == 0:
        users.append(table_els[i])
        print(table_els[i])
        print(users)
    else:
        passwords.append(table_els[i])


print(type(users))
print(type(passwords))
print(users)
print(passwords)

D = dict(zip(users,passwords))
print(D)
print(len(D))

for k, v in D.items(): 
    print(k, v)



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

def test_successful_reg_valid_data(driver: WebDriver): # Проверить что все 5 человек успешно проходят валидацию формы
    for k, v in D.items():
        driver.get('https://erikdark.github.io/QA_DIPLOM/login.html')
        input_login = driver.find_element(By.CSS_SELECTOR, '#login')
        input_pass = driver.find_element(By.CSS_SELECTOR, '#password')
        input_login.send_keys(k)
        input_pass.send_keys(v)
        driver.find_element(By.CSS_SELECTOR,'button').click()
        message = driver.find_element(By.CSS_SELECTOR,'#loginMessage').text
        assert message == 'Вход успешен!'


def test_create_new_user(driver: WebDriver): #создать нового пользователя и сразу проверить его на валидацию
    driver.get('https://erikdark.github.io/QA_DIPLOM/login.html')
    driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys('user6')
    driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
    first_select_button = driver.find_element(By.CSS_SELECTOR,'button')
    first_select_button.find_element(By.CSS_SELECTOR,'option:last-child').click()
    message = driver.find_element(By.CSS_SELECTOR,'#loginMessage').text
    assert message == 'Пользователь добавлен!'


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit


# def test_successful_authorization(driver: WebDriver): # тест, что все 5 человек успешно проходят валидацию формы
#     driver.get('https://erikdark.github.io/QA_DIPLOM/login.html')
#     elements = driver.find_elements(By.TAG_NAME, 'td')
#     for e in elements:
#         print(e.text)




    # input_one = driver.find_elements(By.CSS_SELECTOR, 'td')
    # for i in range(len(input_one)):
    #     input_one[i].send_keys(data[i])
    # driver.find_element(By.CSS_SELECTOR,'button').click()
    # message = driver.find_element(By.CSS_SELECTOR,'#message').text
    # assert message == process_message_0

