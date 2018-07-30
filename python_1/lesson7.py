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
 7 87     - 14    11
      16 49    55 88    77
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

    def __init__(self, message):
        self.message = message

    def _generate_line(self, card_values):

        spaces = ['  '] * 4
        sample = random.sample(card_values, k=5)
        for member in sample:
            card_values.remove(member)
        line = sample + spaces
        random.shuffle(line)
        return line

    def generate_card(self):

        all_card_values = [i for i in range(1, 91)]
        numbers = random.sample(all_card_values, k=15)

        line1 = self._generate_line(numbers) + ['\n']
        line2 = self._generate_line(numbers) + ['\n']
        line3 = self._generate_line(numbers) + ['\n']
        card = line1 + line2 + line3

        return card

    def print_card(self, card, message):

        print(' ----- {} -----\n '.format(message), end='')
        for i in card:
            if len(str(i)) == 1:
                print(' ' + str(i), end=' ')
            else:
                print(i, end=' ')
        print('----------------------------')

    def delete_value(self, card, value):

        index = card.index(value)
        card.remove(value)
        card.insert(index, ' -')

    def test(self, card):
        x = True
        for value in card:
            if value != '  ' and value != ' -' and value != '\n':
                x = False
        return x



def generate_number(numbers):
    value = random.choice(numbers)
    numbers.remove(value)
    rest_numbers = len(numbers)
    print('{}(Осталось {} бочонков)'.format(value, rest_numbers))
    return value


class Loto:

    def start(self):

        player_message = 'Ваша карта'
        computer_message = 'Карта компьютера'

        p_c = Card(player_message)
        player_card = p_c.generate_card()

        c_c = Card(computer_message)
        computer_card = c_c.generate_card()

        values = [i for i in range(1, 91)]
        while len(values) > 0:
            n = generate_number(values)
            p_c.print_card(player_card, player_message)
            c_c.print_card(computer_card, computer_message)
            choice = 0
            while choice != 'y' and choice != 'n':
                choice = input('Зачеркнуть цифру? (y/n)\n')
            if n in computer_card:
                c_c.delete_value(computer_card, n)
            if choice == 'y' and n in player_card:
                p_c.delete_value(player_card, n)
            elif choice == 'y' and n not in player_card:
                print('Вы проиграли!')
                break
            elif choice == 'n' and n not in player_card:
                pass
            elif choice == 'n' and n in player_card:
                print('Вы проиграли!')
                break

            if p_c.test(player_card) is True and c_c.test(computer_card) is True:
                print('Победила дружба!:)')
                break
            elif p_c.test(player_card) is True:
                print('Вы заполнили всю карту! Поздравляем с победой!:)')
                break
            elif c_c.test(computer_card) is True:
                print('Победил компьютер!:(')
                break

game = Loto()
game.start()
