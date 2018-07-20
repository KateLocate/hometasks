# Easy

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = []
while True:
   fruit = input('Введите название фрукта или, чтобы прекратить ввод, нажите Enter: ')
   if fruit != '':
       fruits.append(fruit)
   else:
       break
n = 1
for i in range(len(fruits)):
   print(str(n)+'.', ('{:>15}'.format(fruits[i])))
   n += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random
n = 1
list1 = []
while True:
    if n > 0:
        list1.append(random.randint(1, 40))
        n = random.randint(-1, 40)
    else:
        break
print(list1)
n = 1
list2 = []
while True:
    if n > 0:
        list2.append(random.randint(1, 40))
        n = random.randint(-1, 40)
    else:
        break
print(list2)
for i in range(0, len(list2)-1):
    while list2[i] in list1:
        list1.remove(list2[i])
print(list1)
print(list2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random
n = 1
list = []
while True:
    if n > 0:
        list.append(random.randint(1, 1000))
        n = random.randint(-1, 40)
    else:
        break
print(list)
new_list = []
for i in range(0, len(list)-1):
    if list[i] % 2 == 0:
        new_list.append(list[i] / 4)
    else:
        new_list.append(list[i] * 2)
print(new_list)
