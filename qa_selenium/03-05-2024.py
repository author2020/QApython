# Задача с условным ветвлением на проверку времени года
# Вам надо проверить, при вводе месяца(не важно строкой или цифрой май - 05/5)
# Какое это время года.

# winter = ['январь', 'февраль','декабрь', '12', '1', '2', '01', '02']
# spring = ['март', 'апрель','май', '03', '3', '04', '4', '05', '5']
# summer = ['июнь', 'июль','август', '06', '6', '07', '7', '08', '8']
# autumn = ['сентябрь', 'октябрь','ноябрь', '09', '9', '10', '11']

# month = input("Введите название или номер месяца ")

# if month in winter:
#     print("winter")
# elif month in spring:
#     print("spring")
# elif month in summer:
#     print("summer")
# elif month in autumn:
#     print("autumn")            
# else:
#     print("Введите общепринятый формат месяца")

# from datetime import datetime

# month = int(input("Введите номер месяца "))

# print(month)

# Написать программу для выдачи кредита.
# Условия выдачи зависят от сумма дохода и кредитного рейтинга заемщика.

# 5000  - минималка (только целые числа)
# >=7 - кредитный рейтинг

# Пользователь вводит ежемесячный доход
# Вводит кредитный рейтинг

# *Ваш доход выше 5000 $
# *Ваш кредитный рейтинг хороший
# *Вам одобрен кредит
# *Ваш кредитный рейтинг ниже 7
# *Вам не одобрен кредит
# *Ваш доход ниже 5000$


# m_income = int(input("Введите ежемесячный доход: "))
# rating = int(input("Введите рейтинг: "))

# if rating < 7 and m_income < 5000:
#     print("Ваш кредитный рейтинг ниже 7. Ваш доход ниже 5000$. Вам не одобрен кредит")   
# elif m_income < 5000:
#     print("Ваш доход ниже 5000$. Вам не одобрен кредит")
# elif rating < 7:
#     print("Ваш кредитный рейтинг ниже 7. Вам не одобрен кредит")          
# else:
#     print("Ваш доход выше 5000 $. Ваш кредитный рейтинг хороший. Вам одобрен кредит")

# Написать программу которая должна оценить сразу несколько автомобилей, 
# чтобы пользователь мог ввести информацию о нескольких автомобилях (использовать for)
# Стоимость автомобиля зависит от его данных:
# Марка, год выпуска, пробег, состояние(новый/бу)
# Коэффициенты произвольные.
# Базовая стоимость авто = 10000

autos = []
price = []
BASE_PRICE = 10000
expensive =['bmw', 'audi']

print(autos)
N = int(input('Введите количество автомобилей, которые будет оценены: '))
for j in range(N):
    auto = [input('Введите через enter характеристики авто для оценки стоимости: Марка, год выпуска, пробег: ') for i in range(4)]
    auto[1] = int(auto[1])
    auto[2] = int(auto[2])
    if auto[2] > 0:
        auto[3] = 'old'
    else:
        auto[3] = 'new'
    autos.append(auto)
    print(autos[j])
    priced = BASE_PRICE
    if  auto[1] < 1990 or auto[2] > 200000:
        if auto[0] in expensive:
            priced = BASE_PRICE * 0.3
        else:
            priced = BASE_PRICE * 0.2
    elif auto[1] < 2000 or auto[2] > 100000:
        if auto[0] in expensive:
            priced = BASE_PRICE * 0.7
        else:
            priced = BASE_PRICE * 0.6        
    elif auto[1] < 2021 or auto[2] > 0:
        if auto[0] in expensive:
            priced = BASE_PRICE * 0.9
        else:
            priced = BASE_PRICE * 0.8
    price.append(priced)
    print(price[j])
