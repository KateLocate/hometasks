# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def personal_data(name, age, city):
    if 10 < age < 15 or 4 < age % 10 < 10 or age % 10 == 0:
        print('{}, {} лет, проживает в городе {}.'.format(name, age, city))
    else:
        print('{}, {} год(а), проживает в городе {}.'.format(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def maximum_number(x, y, z):
    numbers = [x, y, z]
    for number in numbers:
        if type(number) != float and type(number) != int:
            print('Wrong type of data, integer or float expected!')
            break
        else:
            return max(numbers)


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_string_length(*strings):
    strings = sorted(strings, key=len, reverse=True)
    return strings[0]
