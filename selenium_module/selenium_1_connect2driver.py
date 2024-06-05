import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By # класс, кот позволяет выбирать способ поиска элемента на странице
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
time.sleep(1)


# driver.get('http://fortesters.easysmarthub.ru/form1/')
# time.sleep(5)
# input_one = driver.find_element(By.NAME, 'name')
# input_one.send_keys('Katrin')
# btn = driver.find_element(By.NAME, 'button')
# btn.click()
# time.sleep(5)
# driver.quit()



# driver.get('https://www.google.com/')
# time.sleep(5)


# input_one = driver.find_element(By.ID, 'APjFqb')
# input_one.send_keys('Katrin')
# time.sleep(5)
# btn = driver.find_element(By.NAME, 'btnK')
# btn.click()
# time.sleep(5)
# driver.quit()

# driver.get('https://www.google.com/')
# time.sleep(5)


# input_one = driver.find_element(By.CLASS_NAME, 'gLFyf')
# input_one.send_keys('Katrin')
# time.sleep(5)
# btn = driver.find_element(By.NAME, 'btnK')
# btn.click()
# time.sleep(5)
# driver.quit()

# input_one = driver.find_element(By.CSS_SELECTOR, '')
# input_one.send_keys('Katrin')
# time.sleep(5)
# btn = driver.find_element(By.NAME, 'btnK')
# btn.click()
# time.sleep(5)
# driver.quit()

# driver.get('https://suninjuly.github.io/cats.html')
# time.sleep(5)
# input_one = driver.find_element(By.ID, 'bullet')
# input_one.send_keys('Katrin')
# time.sleep(5)
# btn = driver.find_element(By.NAME, 'btnK')
# btn.click()
# time.sleep(5)
# driver.quit()

# driver = webdriver.Chrome()
# time.sleep(5)

# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_01/')
#     time.sleep(5)
#     input_one = driver.find_element(By.ID, 'inputField')
#     input_one.send_keys('Katrin')
#     time.sleep(3)
#     btn = driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)')
#     # btn = driver.find_element(By.CSS_SELECTOR, 'buttons.btn:nth-child(3)') # если есть родительский класс у кнопки
#     btn.click()
#     time.sleep(3)
# finally:
#     driver.quit()

# try: # считаем количество кнопок и выводим в терминал, выводим да, если кнопок действительно 8
#     driver.get('https://erikdark.github.io/Qa_autotest_01/')
#     time.sleep(1)
#     # input_one = driver.find_elements(By.CSS_SELECTOR, 'button')
#     input_one = driver.find_elements(By.CSS_SELECTOR, '.btn')
#     print(input_one)
#     print(len(input_one))
#     if len(input_one) == 8:
#         print('da')
#     else:
#         print('no')
#     time.sleep(3)
#     # btn = driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)')
#     # # btn = driver.find_element(By.CSS_SELECTOR, 'buttons.btn:nth-child(3)') # если есть родительский класс у кнопки
#     # btn.click()
#     #time.sleep(3)
    
# finally:
#     driver.quit()




# try: 
#     driver.get('https://erikdark.github.io/Qa_autotest_02/')
#     data = ['89211449044', 'peterburg@gmail.com','Katrin','kjh8908D-']
#     input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
#     for i in range(len(input_one)):
#         input_one[i].send_keys(data[i])
#         time.sleep(1)
#     btn = driver.find_element(By.ID, 'submitBtn')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)
#     # btn = driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)')
#     # # btn = driver.find_element(By.CSS_SELECTOR, 'buttons.btn:nth-child(3)') # если есть родительский класс у кнопки
#     # btn.click()
#     #time.sleep(3)
    
# finally:
#     driver.quit()    



# try: # поиск элемента по тексту в ссылке тег а - это ссылка
#     search_in_href = 'https://easysmarthub.ru/blog/'
#     driver.get(search_in_href)
#     search_data = 'Что такое базы данных?'
#     found = driver.find_element(By.LINK_TEXT, search_data)
#     print('found ', search_data, '', found)
    
#     # btn = driver.find_element(By.ID, 'submitBtn')
#     # time.sleep(1)
#     found.click()
#     time.sleep(3)
#     search_in_href = string(found) # так не работает found  Что такое базы данных?  
#     # <selenium.webdriver.remote.webelement.WebElement (session="d0259678ecb9c83cbd243e4150688f9a", element="f.9E802E3656F1221BD1F87A3B1AB88686.d.7D3BCF140C5117A66E2F45D0BDC6349D.e.27")>
#     driver.get(search_in_href)
#     search_data = 'Эрик Спичак'
#     found = driver.find_element(By.LINK_TEXT, search_data)
#     print('found 2', search_data)
#     time.sleep(5)
#     found.click()
#     time.sleep(5)
    
# finally:
#     driver.quit()    


# try: 
#     driver.get('https://erikdark.github.io/Qa_autotest_02/')
#     data = ['89211449044', 'peterburg@gmail.com','Katrin','kjh8908D-']
#     input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
#     for i in range(len(input_one)): # for i in input: еще можно так
#         #i.send_keys('Text') - еще можно так

#         input_one[i].send_keys(data[i])
#         time.sleep(1)
#     btn = driver.find_element(By.ID, 'submitBtn')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)
#     # btn = driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)')
#     # # btn = driver.find_element(By.CSS_SELECTOR, 'buttons.btn:nth-child(3)') # если есть родительский класс у кнопки
#     # btn.click()
#     #time.sleep(3)
    
# finally:
#     driver.quit()    

# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     data = ['Katrin', 'Vasileva','peterburg@gmail.com', '+79211449044','Address kjh8908D-']
#     input_one = driver.find_elements(By.CSS_SELECTOR, 'input')
#     for i in range(len(input_one)): # for i in input: еще можно так
#         #i.send_keys('Text') - еще можно так
#         input_one[i].send_keys(data[i])
#         # time.sleep(1)
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)

#     cong = driver.find_element(By.TAG_NAME, 'h2')
#     print(cong) # <selenium.webdriver.remote.webelement.WebElement (session="fd6620a88f8c96602427b3a9315e5deb", element="f.32527E71C562AD3287544861FBCDC0B5.d.DAECB14261DA917A9AE663F789833577.e.17")>
#     print(type(cong)) # <class 'selenium.webdriver.remote.webelement.WebElement'>
#     cong_text = cong.text 
#     print(cong_text) #Поздравляю, вы прошли первый уровень.
#     print(type(cong_text)) #<class 'str'>
#     assert'Поздравляю, вы прошли первый уровень.' == cong_text


# finally:
#     time.sleep(3)
#     driver.quit()    


# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     data = ['Katrin', 'Vasileva','peterburg@gmail.com', '+79211449044','Address kjh8908D-']
#     input_one = driver.find_elements(By.CSS_SELECTOR, 'input:required')
#     for i in range(len(input_one)): # for i in input: еще можно так
#         #i.send_keys('Text') - еще можно так
#         input_one[i].send_keys(data[i])
#         # time.sleep(1)
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)
#     # driver.close() 


#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     input_one = driver.find_element(By.CSS_SELECTOR, '#address')
#     input_one.send_keys('My Address')
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)



#     input_one = driver.find_element(By.ID, 'phone')
#     input_one.send_keys('+7989787867')
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)


# finally:
#     time.sleep(2)
#     driver.quit()    


# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_04/')
#     data = ['Ka', 'Va','peterburg@gmail.com', '9211449044','Address kjh8908D-'] # проблема была с полем телефон
#     input_one = driver.find_elements(By.CSS_SELECTOR, 'input:required')
#     for i in range(len(input_one)): # for i in input: еще можно так
#         #i.send_keys('Text') - еще можно так
#         input_one[i].send_keys(data[i])
#         # time.sleep(1)
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)
#     # driver.close() 


#     driver.get('https://erikdark.github.io/Qa_autotest_04/')
#     input_one = driver.find_element(By.CSS_SELECTOR, '#address')
#     input_one.send_keys('My Address')
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)



#     input_one = driver.find_element(By.ID, 'phone')
#     input_one.send_keys('+7989787867')
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     time.sleep(1)
#     btn.click()
#     time.sleep(3)


# finally:
#     time.sleep(2)
#     driver.quit()    

# try:
#     driver.get('https://erikdark.github.io/Qa_autotests_05/')
#     time.sleep(2)
#     #data = ['Ka', 'Va','peterburg@gmail.com', '9211449044','Address kjh8908D-'] # проблема была с полем телефон
#     input_one = driver.find_element(By.CSS_SELECTOR, '#challenge')
#     print(input_one.text) #What is 93 + 39?
#     text1 = input_one.text #What is 93 + 39?
#     # for i in filter(str.isdigit, text1):
#     #     print(i) # 8 6 7
#     text2 = re.findall(r'(\d+)', text1)
#     print(text2)
#     print(type(text2))
#     numbers_list = [int(item) for item in text2]
#     print(numbers_list)
#     print(sum(numbers_list))

#     driver.find_element(By.CSS_SELECTOR, '#notRobot').click()
#     driver.find_element(By.CSS_SELECTOR, '#cool').click()
#     driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
#     text = driver.find_element(By.CSS_SELECTOR,'#message').text
#     assert 'Поздравляю, Elon Musk!' == text

# finally:
#     time.sleep(2)
#     driver.quit()    

# try:
#     driver.get('https://erikdark.github.io/Qa_autotests_06/')
#     time.sleep(1)

#     nums = driver.find_element(By.CSS_SELECTOR, '#challenge') # строка в которой есть атрибуты
#     a = nums.get_attribute('data-a') # получаем значение указанного атрибута - все то, что находится внутри тега: data-a='80' - получаем сразу строку 80
#     b = nums.get_attribute('data-b')
#     numbers_list = [] # список строк
#     numbers_list.append(a)
#     numbers_list.append(b)
#     print(numbers_list)

#     int_list = [int(i) for i in numbers_list] # список чисел
#     print(int_list)

#     answer = sum(int_list)
#     print(sum(int_list)) # сумма чисел из списка
#     driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(answer))
#     driver.find_element(By.CSS_SELECTOR, '#notRobot').click()
#     driver.find_element(By.CSS_SELECTOR, '#cool').click()
#     driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
#     text = driver.find_element(By.CSS_SELECTOR,'#message').text
#     print(text)
#     assert'Поздравляю, Илон Маск!' == text

# finally:
#     time.sleep(1)
#     driver.quit()    


# try: # тут код котика изменили и он больше не работает
#     driver.get('https://erikdark.github.io/Qa_autotest_07/')
#     time.sleep(1)

#     num1_webel_obj = driver.find_element(By.CSS_SELECTOR, '#challenge') # строка в которой есть атрибут
#     print(num1_webel_obj) # <selenium.webdriver.remote.webelement.WebElement (session="800f93a980de9bce86d278ae5fe7252b", element="f.C7CF2649A6C1446422ADD91BD7C5DE89.d.0DB8811D3929663E421B163F1D79EEEB.e.5")>
#     num1_str = num1_webel_obj.text # получаем значение указанного атрибута 
#     num1_to_num = re.findall(r'(\d+)', num1_str)
#     num1_to_num = [int(item) for item in num1_to_num]
#     print(num1_to_num)
#     print(type(num1_to_num))
#     # num1_int = int(num1_to_num)
#     # print(type(num1_to_num))
#     # a = nums.get_attribute('data-a') # получаем значение указанного атрибута - все то, что находится внутри тега: data-a='80' - получаем сразу строку 80
#     # b = nums.get_attribute('data-b')
#     # numbers_list = [] # список строк
#     # numbers_list.append(a)
#     # numbers_list.append(b)
#     # print(numbers_list)

#     # int_list = [int(i) for i in numbers_list] # список чисел
#     # print(int_list)

#     nums = driver.find_element(By.CSS_SELECTOR, '#numberImage') # строка в которой есть атрибут
#     text_stroka = nums.get_attribute('data-b') # получаем значение указанного атрибута - все то, что находится внутри тега: data-b='80' - получаем сразу строку 80
#     print('text_stroka',text_stroka)
#     text2 = re.findall(r'(\d+)', text_stroka)
#     print(text2)
#     print(type(text2))
#     # numbers_list = [int(item) for item in text2]
#     # print(numbers_list)
    
#     answer = map(sum, zip(num1_to_num,numbers_list))
#     # answer = sum(numbers_list)
#     print(answer)
#     answer = int(answer)
#     print(list(answer))
#     # int_list = [int(i) for i in numbers_list] # список чисел
#     # print(int_list)
#     # print(sum(int_list)) # сумма чисел из списка
#     driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(answer))
#     # driver.find_element(By.CSS_SELECTOR, '#notRobot').click()
#     # driver.find_element(By.CSS_SELECTOR, '#cool').click()
#     driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
#     # text = driver.find_element(By.CSS_SELECTOR,'#message').text
#     # print(text)
#     # assert'Поздравляю, Илон Маск!' == text

# finally:
#     time.sleep(3)
#     driver.quit()    

# _________день 3 с selenium https://docs.google.com/document/d/1kwJLHZy7o1QU2fDyjal6-epM2wQusAXrpkvSdFma51Q/edit

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_08/')
#     time.sleep(2)
#     driver.find_element(By.TAG_NAME,'select').click()
#     driver.find_element(By.CSS_SELECTOR,'option:nth-child(2)').click()
   
# finally:
#     time.sleep(5)
#     driver.quit()

# _____________________________________________________А так мы обращаемся ко 2 селекту
# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_08/')
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,'.container-main select option:nth-child(2)').click()

# finally:
#     time.sleep(5)
#     driver.quit()

# ______________________________________________________________Пример с Select - open list - в нем выбрали оптион 5
# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_08/')
#     time.sleep(2)
#     select = Select(driver.find_element(By.TAG_NAME,'select'))
#     select.select_by_value('5')
   
# finally:
#     time.sleep(5)
#     driver.quit()

# ______________________________________________Подробно - open list - в нем выбрали оптион 2 и в выпадающем тоже выбрали оптион 2
# import time #импортирую сам вебдрайвер
# from selenium import webdriver #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re #иницилизирую драйвер браузера
# driver = webdriver.Chrome()
# try:
#     driver.get('https://erikdark.github.io/QA_autotests_08/')
#     time.sleep(2)
#     #подробно каждый шаг
#     first_select_container = driver.find_element(By.CSS_SELECTOR,'.container')
#     first_select_container.find_element(By.CSS_SELECTOR,'select').click()
#     first_select_container.find_element(By.CSS_SELECTOR,'option:nth-child(2)').click()
#     #или каждый шаг прописан в 1 запрос
#     driver.find_element(By.CSS_SELECTOR,'.container-main select option:nth-child(2)').click()
# finally:
#     time.sleep(5)
#     driver.quit()


    #______________________________________ Или через [value=””]
    # first_select_container = driver.find_element(By.CSS_SELECTOR,'.container')
    # first_select_container.find_element(By.CSS_SELECTOR,'select').click()
    # first_select_container.find_element(By.CSS_SELECTOR,'[value="2"]').click()


#  ще два метода из класса Select
# select_by_visible_text(‘text) - ищет по тексту внутри (только если текст виден на странице)
# select_by_index(index) - ищет по индексу
# select.select_by_index(1)

#_____________________________________________________________Задача 05.06.2024

# import time
# from selenium import webdriver #импортирую сам вебдрайвер
# from selenium.webdriver.common.by import By #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.support.ui import Select
# import re
# driver = webdriver.Chrome() #иницилизирую драйвер браузера

#_____________________________________________________________Задача 05.06.2024
# try:
#     driver.get('https://erikdark.github.io/QA_autotests_09/')
#     time.sleep(1)

#     nums = driver.find_element(By.CSS_SELECTOR, '#challenge') # строка в которой есть атрибут = <div id="challenge">What is 73 + 36?</div>
#     text_stroka = nums.text # получаем значение указанного атрибута - все то, что находится внутри тега: data-b='80' - получаем сразу строку 80
#     print('text_stroka',text_stroka) # text_stroka What is 61 + 33?
#     text2 = re.findall(r'(\d+)', text_stroka) # ['61', '33']
#     print(text2) # ['61', '33']
#     print(type(text2)) # <class 'list'>
#     numbers_list = [int(item) for item in text2] # перевели каждую строку списка в число [61, 33]
#     print(numbers_list)

#     sum_1 = sum(numbers_list) # получили сумму списка из списка целых чисел - 94
#     print(sum_1)
#     #подробно каждый шаг
#     first_select_container = driver.find_element(By.CSS_SELECTOR,'.container')
  
#     first_select_container.find_element(By.CSS_SELECTOR,f'[value="{sum_1}"]').click()
#     # ______________________________другой вариант передать сумму чисел для выбора из выпадающего списка - в 2 строки
#     # select = Select(driver.find_element(By.TAG_NAME,'select'))
#     # select.select_by_value(str(sum_1))


#     # driver.find_element(By.CSS_SELECTOR,'#submitBtn').click()
#     # message = driver.find_element(By.CSS_SELECTOR,'#message').text
#     # assert 'You guessed it! Well done!' == message

#     first_select_container.find_element(By.CSS_SELECTOR,'#submitBtn').click()

#     cong = driver.find_element(By.CSS_SELECTOR, '#message')
#     print(cong) # <selenium.webdriver.remote.webelement.WebElement (session="fd6620a88f8c96602427b3a9315e5deb", element="f.32527E71C562AD3287544861FBCDC0B5.d.DAECB14261DA917A9AE663F789833577.e.17")>
#     print(type(cong)) # <class 'selenium.webdriver.remote.webelement.WebElement'>
#     cong_text = cong.text 
#     print(cong_text) #Поздравляю, вы прошли первый уровень.
#     print(type(cong_text)) #<class 'str'>
#     assert'You guessed it! Well done!' == cong_text 
#     # first_select_container.find_element(By.CSS_SELECTOR,'option:nth-child(2)').click()
#     # #или каждый шаг прописан в 1 запрос
#     # driver.find_element(By.CSS_SELECTOR,'.container-main select option:nth-child(2)').click()
# finally:
#     time.sleep(1)
#     driver.quit()


#________________Возможность запуска JavaScript внутри питона на SElenium
# try:
#     driver.get('https://erikdark.github.io/QA_autotests_10/')
#     time.sleep(1)
    
#     driver.execute_script("document.getElementById('hiddenButton').style.display='block';") # Есть скрытая кнопка и ее надо нажать 
#     driver.find_element(By.CSS_SELECTOR,'#hiddenButton').click()

# finally:
#     time.sleep(1)
#     driver.quit()

#____________________________________________________________ Скролл страницы через js
    # driver.execute_script(“window.scrollTo(0, document.body.scrollHeight)
#_______________________________________________________Получить значение скрытого элемента
    # driver.execute_script(“return document.getElementById(‘hiddenelement’).value;”)
#_______________________________________Выполнение сложных пользовательских действий
# driver.execute_script("""
#     var element = document.getElementById('someElement');
#     var event = new MouseEvent('mouseover', {
#         'view': window,
#         'bubbles': true,
#         'cancelable': true
#     });
#     element.dispatchEvent(event);
# """)


#____________________________________________________________ загрузка файлов
# Задача: Открыть форму и написать скрипт который загружает картинку и нажимает кнопку отправить

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_11/')
#     time.sleep(2)
    
#     # driver.execute_script("document.getElementById('imageInput')") # Есть скрытая кнопка и ее надо нажать 
#     driver.find_element(By.CSS_SELECTOR, '#imageInput').send_keys(r'C:\Users\AttekPC\Documents\GitHub\QApython\selenium_module\kat.jfif')
    
#     driver.find_element(By.CSS_SELECTOR,'Button').click() # другой вариант - driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

# finally:
#     time.sleep(1)
#     driver.quit()

#___________________________Тема всплывашки, модальные окна и системные сообщения
# Alert это не модальное окно, а значит пользователь не может взаимодействовать с интерфейсом пока не закроет его.
# alert = driver.switch_to.alert
# alert.accept()

# switch_to.alert 
# accept()

# alert.text - Чтобы получить текст из alert

# ______________модальное окно типа confirm Оно имеет 2 кнопки в отличии от alert отмена и ок
# confirm = driver.switch_to.alert
# confirm.accept() #нажимаем ок
# confirm.dismiss() #нажимаем отмена

# ____________prompt Имеет доп поле для заполнения для поле заполнения берем команду send_keys
# prompt = driver.switch_to.alert
# prompt.send_keys('anser')
# prompt.accept() #нажимаем ок
# prompt.dismiss() #нажимаем отмена



# Задание: Открыть страницу, нажать на кнопку, согласится с конфирмом и решить промпт и нажать окей. и проверить текст внутри алерта если он совпадает с текстом Правильно! Ответ 50. То в консоли ничего не будет, если нет то увидите сообщение

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_12/')
#     time.sleep(2)
    
#     driver.find_element(By.CSS_SELECTOR,'#startTaskBtn').click() # другой вариант - driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
#     driver.switch_to.alert.accept() # Вы хотите решить задачу? нажимаем ок
#     time.sleep(1)
#     prompt = driver.switch_to.alert
#     prompt_text = prompt.text
#     print('prompt_text = ', prompt_text)
#     # nums = driver.find_element(By.CSS_SELECTOR, '#challenge') # строка в которой есть атрибут = <div id="challenge">What is 73 + 36?</div>
#     text2 = re.findall(r'(\d+)', prompt_text) # ['25, '25']
#     print(text2) # ['25', '25']
#     print(type(text2)) # <class 'list'>
#     numbers_list = [int(item) for item in text2] # перевели каждую строку списка в число [25, 25]
#     print(numbers_list)
#     sum_1 = sum(numbers_list) # получили сумму списка из списка целых чисел - 94
#     print(sum_1)
#     prompt.send_keys(f'{sum_1}')
#     time.sleep(2)
#     prompt.accept() #нажимаем ок
#     time.sleep(1)
#     # prompt.dismiss() #нажимаем отмена
#     alert = driver.switch_to.alert
#     assert 'Правильно! Ответ 50.' == alert.text
#     alert.accept()
#     time.sleep(1)

#     # driver.find_element(By.CSS_SELECTOR, '#imageInput').send_keys(r'C:\Users\AttekPC\Documents\GitHub\QApython\selenium_module\kat.jfif')
    


# finally:
#     time.sleep(1)
#     driver.quit()


# __________________________ Переход по вкладкам в webdriver switch_to.window(window_name)
# _______________Задание. Открыть страницу, нажать на кнопку переключится на новую вкладку там нажать на кнопку получить радоваться.

try:
    driver.get('https://erikdark.github.io/QA_autotests_13/')
    time.sleep(2)
    
    # new_window = driver.window_handles[1]
    # first_window = driver.window_handles[0]

    driver.find_element(By.CSS_SELECTOR,'#openNewPageBtn').click() # другой вариант - driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
    # new_window = driver.window_handles[1]
    time.sleep(2)
    win2 = driver.window_handles[1]
    driver.switch_to.window(win2)
    driver.find_element(By.CSS_SELECTOR,'#displayTextBtn').click()
    message = driver.find_element(By.CSS_SELECTOR,'#displayText')
    assert message == 'Я СДЕЛАЛ', 'Похоже ошибка'
    time.sleep(2)
    

    # driver.switch_to.alert.accept() # Вы хотите решить задачу? нажимаем ок
    # time.sleep(1)
    # prompt = driver.switch_to.alert
    # prompt_text = prompt.text
    # print('prompt_text = ', prompt_text)
    # # nums = driver.find_element(By.CSS_SELECTOR, '#challenge') # строка в которой есть атрибут = <div id="challenge">What is 73 + 36?</div>
    # text2 = re.findall(r'(\d+)', prompt_text) # ['25, '25']
    # print(text2) # ['25', '25']
    # print(type(text2)) # <class 'list'>
    # numbers_list = [int(item) for item in text2] # перевели каждую строку списка в число [25, 25]
    # print(numbers_list)
    # sum_1 = sum(numbers_list) # получили сумму списка из списка целых чисел - 94
    # print(sum_1)
    # prompt.send_keys(f'{sum_1}')
    # time.sleep(2)
    # prompt.accept() #нажимаем ок
    # time.sleep(1)
    # # prompt.dismiss() #нажимаем отмена
    # alert = driver.switch_to.alert
    # assert 'Правильно! Ответ 50.' == alert.text
    # alert.accept()
    # time.sleep(1)

    # # driver.find_element(By.CSS_SELECTOR, '#imageInput').send_keys(r'C:\Users\AttekPC\Documents\GitHub\QApython\selenium_module\kat.jfif')
    


finally:
    time.sleep(1)
    driver.quit()