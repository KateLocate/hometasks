# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие атрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed_change):
        self.speed += speed_change
        print('Машина {} движется со скоростью {} км/ч.'.format(self._name, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина останавливается.')

    def turn(self, direction):
        if direction == 'left':
            print('Машина поворачивает влево.')
        elif direction == 'right':
            print('Машина поворачивает вправо.')

    def open_trunk(self):
        print('Открывается багажник')


class SportCar:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed_change):
        self.speed += speed_change
        print('Машина {} движется со скоростью {} км/ч.'.format(self._name, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина останавливается.')

    def turn(self, direction, angle):
        maximum_angle = 90
        if direction == 'left' and angle <= maximum_angle:
            print('Машина поворачивает влево на {} градусов.'.format(angle))
        elif direction == 'right' and angle <= maximum_angle:
            print('Машина поворачивает вправо на {} градусов.'.format(angle))


class WorkCar:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed_change):
        self.speed += speed_change
        print('Машина {} движется со скоростью {} км/ч.'.format(self._name, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина останавливается.')

    def turn(self, direction):
        if direction == 'left':
            print('Машина поворачивает влево.')
        elif direction == 'right':
            print('Машина поворачивает вправо.')

    def bucket_manipulation(self, action):
        if action == 'up':
            print('Ковш двигается по направлению вверх.')
        elif action == 'down':
            print('Ковш двигается по направлению вниз.')
        elif action == 'left':
            print('Ковш двигается по направлению влево.')
        elif action == 'right':
            print('Ковш двигается по направлению вправо.')


class PoliceCar:

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed_change):
        self.speed += speed_change
        print('Машина {} движется со скоростью {} км/ч.'.format(self._name, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина останавливается.')

    def turn(self, direction):
        if direction == 'left':
            print('Машина поворачивает влево.')
        elif direction == 'right':
            print('Машина поворачивает вправо.')

    def siren(self):
        print('Сирена!')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed_change):
        self.speed += speed_change
        print('Машина {} движется со скоростью {} км/ч.'.format(self._name, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина останавливается.')

    def turn(self, direction):
        if direction == 'left':
            print('Машина поворачивает влево.')
        elif direction == 'right':
            print('Машина поворачивает вправо.')


class TownCar1(Car):
    def open_trunk(self):
        print('Открывается багажник')


class SportCar1(Car):
    def turn(self, direction, steering_wheel_angle):
        maximum_angle = 90
        if direction == 'left' and steering_wheel_angle <= maximum_angle:
            print('Машина поворачивает влево на {} градусов.'.format(steering_wheel_angle))
        elif direction == 'right' and steering_wheel_angle <= maximum_angle:
            print('Машина поворачивает вправо на {} градусов.'.format(steering_wheel_angle))

class WorkCar1(Car):
    def bucket_manipulation(self, action):
        if action == 'up':
            print('Ковш двигается по направлению вверх.')
        elif action == 'down':
            print('Ковш двигается по направлению вниз.')
        elif action == 'left':
            print('Ковш двигается по направлению влево.')
        elif action == 'right':
            print('Ковш двигается по направлению вправо.')


class PoliceCar1(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def siren(self):
        print('Сирена!')
