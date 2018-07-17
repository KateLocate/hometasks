# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'name': input('Player:'), 'health': 180, 'damage': 40, 'armor': 1.0}
enemy = {'name': input('Enemy:'), 'health': 100, 'damage': 20, 'armor': 6.2}


def attack(attacker, defender):
    defender['health'] = round(defender['health'] - attacker['damage'], 2)


def defend(attacker, defender):
    attacker['damage'] = round(attacker['damage'] / defender['armor'], 2)


def record_players_data(personal_dict):
    with open(personal_dict['name']+'.txt', 'w', encoding='utf-8') as file:
        for key, value in personal_dict.items():
            file.write(str(key)+' '+str(value)+'\n')


def read_players_data(person):
    with open(person+'.txt') as file:
        player = dict(map(lambda x: x.strip().split(), file))
    player['armor'] = float(player['armor'])
    player['damage'] = float(player['damage'])
    player['health'] = float(player['health'])
    return player


record_players_data(player)
record_players_data(enemy)

player1 = read_players_data(input('Player1:'))
player2 = read_players_data(input('Player2:'))

defend(player1, player2)
defend(player1, player1)

while player1['health'] >= 0 and player2['health'] >= 0:
    attack(player1, player2)
    attack(player2, player1)
if player1['health'] >= 0:
    print('{} wins! Rest HP = {}.'.format(player1['name'], player1['health']))
else:
    print('{} wins! Rest HP = {}.'.format(player2['name'], player2['health']))
