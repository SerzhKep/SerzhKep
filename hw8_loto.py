#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Card:

    def __init__(self, name):
        self._name = name
        self._number_of_values = 15
        self._matrix = []
        for row in range(0, 3):
            self._matrix.append([None for column in range(0, 9)])

        six_numbers_in_row = True

        while six_numbers_in_row:
            self._clear()
            for column in range(0, 6):
                place_for_none = random.randint(0, 2)

                for row in range(0, 3):
                    if row != place_for_none:
                        self._matrix[row][column] = 0

        six_numbers_in_row = False
        for row in self._matrix:
            if row.count(0) == 6:
                six_numbers_in_row = True
                break

        for column in range(6, 9):
            six_numbers_in_row = True
            while six_numbers_in_row:
                place_for_0 = random.randint(0, 2)
                if self._matrix[place_for_0].count(0) < 5:
                    six_numbers_in_row = False
                    self._matrix[place_for_0][column] = 0

        for column in range(0, 9):
            new_position = random.randint(0, 8)
            for row in range(0, 3):
                buf = self._matrix[row][column]
                self._matrix[row][column] = self._matrix[row][new_position]
                self._matrix[row][new_position] = buf

        for row in range(0, 3):
            for column in range(0, 9):
                if self._matrix[row][column] == 0:
                    duplicate_detected = True
                    while duplicate_detected:
                        new_value = column * 10 + random.randint(1, 10)
                        if not [self._matrix[0][column], self._matrix[1][column],
                                self._matrix[2][column]].count(new_value):
                            duplicate_detected = False
                            self._matrix[row][column] = new_value

    def _clear(self):
        # Очистка карточки.
        for row in range(0, 3):
            for column in range(0, 9):
                self._matrix[row][column] = None

    @property
    def is_empty(self):
        return not self._number_of_values

    def output(self):
        title = ' ' + self._name + ' '
        if len(title) <= 24:
            print(title.center(26, '-'))
        else:
            print('-' * 26)
        for y in self._matrix:
            string = ''
            for x in y:
                if not x:
                    string += '   '
                elif x == -1:
                    string += ' - '
                else:
                    string += '{:>2} '.format(str(x))
            print(string)
        print('-' * 26)

    def find(self, value):
        for row in self._matrix:
            if row.count(value):
                return True
        return False

    def cross_out(self, value):
        for row in range(0, 3):
            for column in range(0, 9):
                if self._matrix[row][column] == value:
                    self._matrix[row][column] = -1
                    self._number_of_values -= 1
                    return value
        return None

class PouchOfBarrels:
    def __init__(self):
        self._array = list(range(1, 91))

    @property
    def left(self):
        return len(self._array)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._array):
            return self._array.pop(random.randint(0, len(self._array) - 1))
        raise StopIteration

last_comp_move = True

mistake_chance = 0.5

player_card = Card('Ваша карточка')
comp_card = Card('Карточка компьютера')

barrels = PouchOfBarrels()

print('Игра начинается'.upper())

player_loss = False
draw_flag = False

for new_barrel in barrels:
    print('\nНовый бочонок: {} (осталось {})'.format(new_barrel, barrels.left))
    player_card.output()
    comp_card.output()
    if input('Зачеркнуть цифру? (y/n) ') == 'y':
        if player_card.cross_out(new_barrel):
            print('Число {} вычеркнуто из вашей карточки.'.format(new_barrel))
            if player_card.is_empty and not last_comp_move:
                break
        else:
            print('Будьте внимательнее! Числа {} нет в вашей карточке.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                break
    else:
        if player_card.find(new_barrel):
            print('Будьте внимательнее! В вашей карточке есть число {}.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                break

    if mistake_chance and random.uniform(0, 99) < mistake_chance:
            print('Компьютер ошибается! В его карточке {} {}'.format(
                'есть число' if comp_card.find(new_barrel) else 'нет числа', new_barrel))
            if player_loss:
                draw_flag = True
            break
    else:
            if comp_card.cross_out(new_barrel):
                print('Компьютер вычёркивает число {} из своей карточки.'.format(new_barrel))

    if player_card.is_empty and comp_card.is_empty:
            draw_flag = True
            break
    if comp_card.is_empty:
            break
    if comp_card.is_empty:
            player_loss = True
            break
    if player_loss:
            break

if draw_flag:
    print('Игра окончена. Ничья!')
elif player_loss:
    print('Игра окончена. Вы проиграли!')
else:
    print('Игра окончена. Поздравляем, вы выиграли!')





























