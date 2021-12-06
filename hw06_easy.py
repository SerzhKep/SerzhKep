from os import makedirs, removedirs, listdir, path
import sys
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
  a = float(input("a = "))
  b = float(input("b = "))
  c = avg(a, b)
  print("Среднее геометрическое = {:.2f}".format(c))
except(SyntaxError):
  print('Error!')

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir(name_dir):
    try:
        makedirs(name_dir)
    except FileExistsError:
        print('{} - уже есть'.format(name_dir))

def delet_dir(name_dir):
    try:
        removedirs(name_dir)
    except FileNotFoundError:
        print('{} - такой папки нет'.format(name_dir))

def start_def():

    #Не знаю как продолжить(


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    dir =listdir()
    for index, element in enumerate(dir, start = 1):
        if path.isdir(element):
            print('{}. {}'.format(index, element))
if __name__ == 'go':
    list_dir()
# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
