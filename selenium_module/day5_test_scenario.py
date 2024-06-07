# Тестовые сценарии.

def test_abs1():
    assert abs(-42) == 42, 'Should be absolute value of a number'

if __name__ == "__main__":
    test_abs1()
    print('All tests passed!')

# if __name__ == “__main__” - служит для подтверждения того, что данный скрипт был запущен напрямую, 
# а не вызван внутри другого файла в качестве модуля. Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно.

# _____________________________________________________________ООП
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         pass


# class Dog(Animal):
#     def speak(self):
#         return f'{self.name} says: ГАВ ГАВ ГАВ'
   
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says: МЯУ ГДЕ ЕДА "
   
# dog = Dog('Гром')
# cat = Cat('Йота')
# print(dog.speak())
# print(cat.speak())

# _______________________________________________

class Person:
    def __init__(self,name,age):
        self.name = name #self.name - атрибут name
        self.age = age #self.age - атрибут age


    def greet(self):
        print(f'Привет, я {self.name} и мне {self.age} лет')


person1 = Person('Erik',28)
person1.greet()


person2 = Person('Mary',30)
person2.greet()