# Easy

# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

a = float('inf')
b = a ** 2
c = a * a
if b == c and a > 999999:
    print(a, b, c, 'Бесконечность - не предел!:)')

a = input('Пожалуйста, введите значение переменной: ')
print(a)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

a = int(input('Пожалуйста, введите число: '))
a = a + 2
print(a)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Пожалуйста, введите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен!')
else:
    print('Извините, пользование данным ресурсом возможно только с 18 лет.')

# Normal

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете о диапазоне допустимых. И просите ввести заново.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = int(input('Введите число от 0 до 10-ти: '))
while number >= 10 or number <= 0:
    number = int(input('Пожалуйста, введите число от 0 до 10-ти, например 5: '))
else:
    print(number ** 2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Значение первой переменной: '))
b = int(input('Значение второй переменной: '))
a = a + b
b = a - b
a = a - b
print('Новое значение первой переменной:', a, 'Новое значение второй переменной:', b)

# Hard

# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('Enter your name: ')
age = int(input('What is your age? '))
weight = int(input('What is your weight?(in kilos) '))
height = float(input('What is your height?(in meters)'))
bmi = weight / height ** 2

if age < 25:
    if bmi <= 18.5:
        print(name, 'is underweight. It is better to keep a nutritious diet.')
    elif 18.5 < bmi < 25:
        print(name, ', your weight is normal, you are in perfect fit!')
    else:
        print(name, ', please, visit your doctor, he will help you to correct your diet.')
elif 25 < age < 40:
    if bmi <= 18.5:
        print(name, 'is underweight, but still it may be normal. Please, pay attention to this fact.')
    elif 18.5 < bmi < 25:
        print(name, ', your weight is normal, you are in perfect fit!')
    else:
        print(name, ', please, visit your doctor, it`s better for you to pay attention to your weight.')
elif 40 < age < 60:
    if bmi <= 18.5:
        print(name, 'is having underweight. It may be caused by disease.')
    elif 18.5 < bmi < 25:
        print(name, ', your weight is normal, you are in perfect fit! Go on like this!')
    else:
        print(name, ', please, visit your doctor. Being overweight may be harmful for your health.')
elif age > 60:
    if bmi <= 18.5:
        print(name, 'is having underweight. Please, keep an eye to your diet and health.')
    elif 18.5 < bmi < 25:
        print(name, ', your weight is normal, you are in perfect fit! Go on like this!')
    else:
        print(name, ', please, visit your doctor and correct your diet. Being overweight can threaten your health.')
