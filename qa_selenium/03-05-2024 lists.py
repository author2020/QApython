x = [2, 0, 3, 12, 'foo', 15, 100, 18, 18, 18]
print(x)
x.reverse()
print(x)
print(x.reverse()) # метод НЕ ВОЗВРАЩАЕТ перевернутый список, поэтому получаем None
print(x.count(18)) # считает количество вхождений в список