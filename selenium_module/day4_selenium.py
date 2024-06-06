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


#_________________________________________не решили задачу - как скомбинировать не знаю синтаксис
import time
from selenium import webdriver #импортирую сам вебдрайвер
from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome() #иницилизирую драйвер браузера

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')

    if 
    a1 = WebDriverWait(driver,5).until((EC.text_to_be_present_in_element((By.ID,"price1"), '550')))
    print(a1)
    print(type(a1)) 
    a2 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#buyButton1'))) 
    print(a2)
    print(type(a2)) 
    
    # .click() 
    # lada_price.click() 
    # код ожидает N секунд пока элемент станет видимым
    # my_price = lada_price.text
    # print(my_price)
    # btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.CSS_SELECTOR,'#buyButton1')).click()
    # btn = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID,'buyButton1'))).click() # код ожидает 1 секунд пока элемент станет доступным для нажатия
    message = driver.find_element(By.ID,'message1')
    assert 'Вы успешно купили автомобиль!' in message.text
       
       
finally:
    time.sleep(5)
    driver.quit()