from random import randint
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n:m]
print(fibonacci(3,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    length = len(origin_list)
    for i in range(length):
        for j in range(0, length-i-1):
            if origin_list[j] > origin_list[j+1]:
                temp = origin_list[j]
                origin_list[j] = origin_list[j+1]
                origin_list[j+1] = temp
my_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(my_list)
print(my_list)



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def this_filter(function, spisok):
    filtered_spisok = []
    for i in range(len(spisok)):
        if filter(spisok[i]) == True:
            filtered_spisok.append(spisok[i])
    return filtered_spisok

def modife_list(L, fun):
    for i, j in enumerate(L):
        L[i] = fun(j)
L = [1, 2, 3, 'stroka']
modife_list(L, this_filter)
print(L)
# Я пытался сделать но где-то повернул не туда и полностью запутался)







# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
       abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False
print(parallelogram([2, 3], [4, 5], [6, 7], [8, 9]))
# Что-то не пойму, тут сравнение уже написанно, нужно вызвать функцию?