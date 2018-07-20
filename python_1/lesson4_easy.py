# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [- 10, -8, 0, 1, 2, 9]
numbers_sq = [i**2 for i in numbers]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ['strawberry', 'blueberry', 'apple', 'apricot', 'pear', 'watermelon', 'melon', 'apple', 'orange']
fruit2 = ['lemon', 'strawberry', 'mango', 'pear', 'banana', 'raspberry', 'watermelon', 'apple']
common_fruit = [i for i in fruit1 if i in fruit2]
for fruit in common_fruit:
    while common_fruit.count(fruit) > 1:
        common_fruit.remove(fruit)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers1 = [15, -5, 18, 2, 30, 4, 0, 54, 5, 7, 8, -99, 10, 88, 11, -24, 12, 13, 14, 99]
selection = [i for i in numbers1 if i % 3 == 0 and i >= 0 and i%4 != 0]
