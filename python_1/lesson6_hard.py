# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:

    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type


class ToyAnimal(Toy):

    def __init__(self, name, color, toy_type='animal'):
        super().__init__(name, color)
        self._toy_type = toy_type


class CartoonToy(Toy):

    def __init__(self, name, color, toy_type='cartoon character'):
        super().__init__(name, color)
        self._toy_type = toy_type


class ToyFactory:

    def materials_purchase(self):
        print('Закупаем ткани, искусственный мех, набивку, пуговицы и т.п.')

    def sewing(self):
        print('Кроим ткани и сшиваем изделие.')

    def coloring(self):
        print('Окрашиваем игрушку.')

    def creation(self, toy_type, name, color):
        if toy_type == 'animal':
            toy = ToyAnimal(name, color)
            return toy
        elif toy_type == 'cartoon character':
            toy = CartoonToy(name, color)
            return toy


toy_factory = ToyFactory
print(toy_factory.creation('animal', 'bear', 'red'))