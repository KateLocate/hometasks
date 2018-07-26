# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих атрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть атрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл также через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name, health, damage, armor):
        self._name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _real_damage(self, defender):
        return self.damage // defender.armor

    def _attack(self, defender):
        defender.health -= self._real_damage(defender)
        print('Игроку {} нанесен урон: {}, оставшиеся HP: {}'.format(defender._name, self._real_damage(defender),
                                                                     defender.health))


class Player(Person):

    def __init__(self, name, health, damage, armor, equipment=['map', 'sword']):
        super().__init__(name, health, damage, armor)
        self.equipment = equipment


class Enemy(Person):

    def __init__(self, name, health, damage, armor, anger_level=0):
        super().__init__(name, health, damage, armor)
        self.anger_level = anger_level

    def _real_damage(self, defender):
        if self.anger_level > 4:
            return (self.damage // defender.armor) * 2
        else:
            return self.damage // defender.armor


class Battle:

    def start(self, player, enemy):
        import random
        choice = [player, enemy]
        who_attack = random.choice(choice)
        while player.health > 0 and enemy.health > 0:
            if who_attack == player:
                player._attack(enemy)
                who_attack = enemy
                enemy.anger_level += 1
            else:
                if enemy.anger_level > 5:
                    enemy.anger_level = 0
                enemy._attack(player)
                who_attack = player

    def end(self, player, enemy):
        if player.health > 0:
            print('Игрок {} победил! Оставшиеся HP: {}.'.format(player._name, player.health))
        else:
            print('{} победил! Оставшиеся HP: {}.'.format(enemy._name, enemy.health))


p = Player('Bob', 100, 12, 1.5)
e = Enemy('Creature', 80, 12, 1.2)

battle = Battle()
battle.start(p, e)
battle.end(p, e)

