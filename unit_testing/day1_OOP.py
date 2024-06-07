# ______________________________________________Unittest - эту библиотеку используют программисты
# Тест-раннеры сами находят тестовые методы в указанных при запуске файлах. Для этого надо следовать общепринятым правилам.
# Общее правило для всех тестовых фреймворков название каждого метода должно начинаться со слова “test_” Дальше может идти любой текст, который являетсяу уникальным названием для вашего теста:

import unittest #https://docs.python.org/3/library/unittest.html


class TestAbs(unittest.TestCase): #Создать класс, который должен наследоваться от класса unittest.TestCase
    def test_abs1(self):
        self.assertEqual(abs(-42),-42,'should be abs')
    def test_abs2(self):
        self.assertEqual(abs(-42),42,'should be abs')


if __name__ == "__main__": 
    unittest.main()

