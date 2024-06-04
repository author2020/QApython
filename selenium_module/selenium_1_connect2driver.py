import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By # класс, кот позволяет выбирать способ поиска элемента на странице


driver = webdriver.Chrome()
time.sleep(5)

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


try:
    driver.get('https://erikdark.github.io/Qa_autotest_07/')
    time.sleep(1)

    nums = driver.find_element(By.CSS_SELECTOR, '#numberImage') # строка в которой есть атрибуты
    text_stroka = nums.get_attribute('data-b') # получаем значение указанного атрибута - все то, что находится внутри тега: data-b='80' - получаем сразу строку 80
    text2 = re.findall(r'(\d+)', text_stroka)
    print(text2)
    print(type(text2))
    numbers_list = [int(item) for item in text2]
    print(numbers_list)
    answer = sum(numbers_list)
    print(answer)
    # int_list = [int(i) for i in numbers_list] # список чисел
    # print(int_list)
    # print(sum(int_list)) # сумма чисел из списка
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(answer))
    # driver.find_element(By.CSS_SELECTOR, '#notRobot').click()
    # driver.find_element(By.CSS_SELECTOR, '#cool').click()
    driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
    # text = driver.find_element(By.CSS_SELECTOR,'#message').text
    # print(text)
    # assert'Поздравляю, Илон Маск!' == text

finally:
    time.sleep(3)
    driver.quit()    