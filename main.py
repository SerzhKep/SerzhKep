__author__ = 'Грязнов Сергей Андреевич'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст'))
age2 = age - 18
print(name, 'на',age2,'лет больше 18' )


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a = int(input('Введите значение переменной №1: '))
b = int(input('Введите значение переменной №2: '))
print(a)
print(b)
a,b = b,a
print(a)
print(b)
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))
d = b ** 2 - 4 * a * c
print('Дискриминант d =', d)
if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / 2 * a
    print(x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)