import time
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

try: # считаем количество кнопок и выводим в терминал, выводим да, если кнопок действительно 8
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(1)
    # input_one = driver.find_elements(By.CSS_SELECTOR, 'button')
    input_one = driver.find_elements(By.CSS_SELECTOR, '.btn')
    print(input_one)
    print(len(input_one))
    if len(input_one) == 8:
        print('da')
    else:
        print('no')
    time.sleep(3)
    # btn = driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)')
    # # btn = driver.find_element(By.CSS_SELECTOR, 'buttons.btn:nth-child(3)') # если есть родительский класс у кнопки
    # btn.click()
    #time.sleep(3)
    
finally:
    driver.quit()