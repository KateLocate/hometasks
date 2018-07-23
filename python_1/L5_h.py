# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil


# print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию указанного файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <full_path> - поменять текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    try:
        full_name = input("Введите имя файла:")
        name = full_name.split('.')
        shutil.copyfile(os.getcwd()+'\\'+full_name, os.getcwd()+'\\'+name[0]+'_copy.'+name[1])
        print('Копия файла создана!')
    except IndexError:
        print('Вы не ввели существующее имя файла!')


def rm():
    file_name = input('Введите имя файла, который хотите удалить:')
    agreement = input("Если Вы действительно хотите удалить файл, введите '+':")
    if agreement == '+':
        if file_name in os.listdir(os.getcwd()):
            os.remove(os.getcwd()+'\\'+file_name)
            print('Файл удален.')
        else:
            print('Такого файла нет в текущей директории!')


def cd():
    path = input('Введите путь до нужной директории:')
    try:
        os.chdir(path)
        print('Вы успешно перешли в указанную директорию!')
    except FileNotFoundError:
        print('Вы ввели текущий или несуществующий путь!')
    except OSError:
        print('Вы ввели несуществующий путь!')


def ls():
    print(os.path.abspath(os.getcwd()))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'ls': ls,
    'cd': cd,
    'rm': rm,
    'cp': cp
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
